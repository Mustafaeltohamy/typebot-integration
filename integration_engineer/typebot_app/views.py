import json
import requests
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.conf import settings
from django.http import JsonResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from .models import CustomUser, BotSession

# Hardcoded credentials for demo
DEMO_USER = {
    'username': 'demo',
    'password': 'demopassword',
    'email': 'demo@example.com'
}

def custom_login(request):
    """
    Login view with hardcoded credentials for demo purposes
    """
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # Hardcoded authentication - in production use proper auth
        if username == DEMO_USER['username'] and password == DEMO_USER['password']:
            # Get or create user with hardcoded credentials
            user, created = CustomUser.objects.get_or_create(
                username=username,
                defaults={'email': DEMO_USER['email']}
            )
            
            # Generate simple token (in real app, use JWT)
            user.auth_token = f"demo_token_{user.id}"
            user.save()
            
            # Log user in
            login(request, user)
            return redirect('bot_list')
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    
    return render(request, 'login.html')


def bot_list(request):
    """
    Displays list of available Typebot bots
    Mocked for demo - in real app, fetch from Typebot API
    """
    if not request.user.is_authenticated:
        return redirect('login')
    
    # Mocked bot data - replace with actual API call in production
    bots = [
        {
            'id': 'bot1',
            'name': 'Customer Support Bot',
            'description': 'Handles customer inquiries'
        },
        {
            'id': 'bot2',
            'name': 'Lead Generation Bot',
            'description': 'Collects potential customer information'
        },
        {
            'id': 'bot3',
            'name': 'Feedback Collector',
            'description': 'Gathers user feedback'
        }
    ]
    
    # Uncomment to fetch real data when Typebot is running
    """
    try:
        # Fetch bots from Typebot API
        response = requests.get(
            f"{settings.TYPEBOT_API_URL}/typebots",
            headers={"Authorization": f"Bearer {request.user.auth_token}"}
        )
        bots = response.json() if response.status_code == 200 else []
    except Exception as e:
        print(f"Error fetching bots: {e}")
        bots = []
    """
    
    return render(request, 'bot_list.html', {'bots': bots})


def embed_bot(request, bot_id):
    """
    Embeds a Typebot bot in an iframe
    """
    if not request.user.is_authenticated:
        return redirect('login')
    
    # Construct Typebot embed URL
    bot_url = f"{settings.TYPEBOT_VIEWER_URL}/typebots/{bot_id}/embed"
    
    return render(request, 'embed_bot.html', {
        'bot_url': bot_url,
        'bot_id': bot_id
    })


def analytics(request):
    """
    Displays simple analytics from stored bot sessions
    """
    if not request.user.is_authenticated:
        return redirect('login')
    
    # Get all bot sessions from database
    sessions = BotSession.objects.all()
    
    # Aggregate data for display
    total_sessions = sessions.count()
    completed_sessions = sessions.filter(completed=True).count()
    last_sessions = sessions.order_by('-created_at')[:10]
    
    return render(request, 'analytics.html', {
        'total_sessions': total_sessions,
        'completed_sessions': completed_sessions,
        'last_sessions': last_sessions
    })


@csrf_exempt
def typebot_webhook(request):
    """
    Handles incoming webhooks from Typebot to store session data
    """
    if request.method == 'POST':
        try:
            # Parse JSON data from request
            data = json.loads(request.body)
            
            # Extract relevant data
            session_id = data.get('sessionId')
            bot_id = data.get('botId')
            user_email = data.get('email', None)
            completed = data.get('isCompleted', False)
            
            # Validate required fields
            if not session_id or not bot_id:
                return HttpResponseBadRequest("Missing required fields")
            
            # Create or update session in database
            session, created = BotSession.objects.update_or_create(
                session_id=session_id,
                defaults={
                    'bot_id': bot_id,
                    'user_email': user_email,
                    'completed': completed
                }
            )
            
            return JsonResponse({'status': 'success'})
        
        except json.JSONDecodeError:
            return HttpResponseBadRequest("Invalid JSON")
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=500)
    
    return JsonResponse({'status': 'invalid method'}, status=400)