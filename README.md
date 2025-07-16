# Typebot Integration Demo with Django

## Assignment Overview
This project completes the Integration Engineer assignment for Typebot integration. The goal was to demonstrate the ability to integrate Typebot into a custom web application with a focus on embedding, authentication handling, and data access.

### Original Assignment Requirements
1. **Clone and Run Typebot**
2. **Build a Web App that:**
   - Lists Typebot bots
   - Embeds one bot
   - Displays simple analytics:
     - Total sessions started
     - Bot usage stats
     - Last run per user
3. **Authentication:**
   - Hardcoded login → generate token → access both apps (mocked)
   - Bridge authentication without modifying Typebot's auth

## Implementation Details

### What Has Been Implemented
- **Typebot Integration:**
  - Bot listing (with mocked data for demo)
  - Bot embedding via iframe
  - Webhook endpoint for session data capture
- **Authentication System:**
  - Hardcoded credentials (demo/demopassword)
  - Token generation (demo_token_<id>)
  - Session management
- **Analytics Dashboard:**
  - Total sessions tracking
  - Completed sessions count
  - Recent session history
- **Responsive UI:**
  - Clean, modern interface
  - Card-based layout
  - Consistent styling across pages

### Tech Stack
- **Backend:** Django 5.1
- **Database:** SQLite
- **Frontend:** HTML5, CSS3
- **Dependencies:** Django, Requests


## Application Features
### 1. Authentication
    -Hardcoded credentials for demo access
    -Session-based authentication
    -Token generation for API access
### 2. Bot Management
    -View list of available bots (mocked data)
    -Embed any bot in an iframe
    -Responsive design for all screen sizes
### 3. Analytics Dashboard
    -Total sessions count
    -Completed sessions percentage
    -Recent session history with:
        -Bot ID
        -User email
        -Start time
        -Completion status
### 4. Webhook Integration
    -Endpoint: /webhook/typebot/
    -Handles POST requests from Typebot
    -Stores session data in database
    -Supports:
        -sessionId
        -botId
        -email
        -isCompleted

## Known Limitations
### 1. Authentication
    -Uses hardcoded credentials (not production-ready)
    -Tokens are simplistic (should use JWT in production)
### 2. Bot Listing:
    -Currently uses mocked data (uncomment API code in views.py for real integration)
### 3. Analytics
    -Basic metrics only
    -No visualization charts
### 4. Security
    -No CSRF protection for webhook
    -No input validation for webhook data

## Setup and Installation
### Prerequisites
- Python 3.8+
- Django 5.1
- Requests

### Step-by-Step Instructions

1. **clone or download the project:**
   git clone https://github.com/Mustafaeltohamy/typebot-integration.git
   cd typebot-integration/integration_engineer
   
2. **Set up virtual environment**:

    # Linux/Mac
    python -m venv venv
    source venv/bin/activate

    # Windows
    python -m venv venv
    venv\Scripts\activate
3. **Install dependencies:**
    pip install requirements.txt
4. **Migrate the local database:**
    python manage.py makemigrations
    python manage.py migrate
    python manage.py createsuperuser
5. **Run the server:**
    python manage.py runserver
6. **Access the application:**
    - Open: http://localhost:8000
    - Login with: demo / demopassword

