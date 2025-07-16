from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

class CustomUser(AbstractUser):
    """
    Custom user model with token-based authentication
    Resolves conflicts by specifying unique related_names
    """
    auth_token = models.CharField(max_length=100, blank=True, null=True)
    
    # Resolve reverse accessor conflicts
    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name=_('groups'),
        blank=True,
        help_text=_('The groups this user belongs to.'),
        related_name="customuser_set",
        related_query_name="user",
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name=_('user permissions'),
        blank=True,
        help_text=_('Specific permissions for this user.'),
        related_name="customuser_set",
        related_query_name="user",
    )

class BotSession(models.Model):
    """
    Stores session data from Typebot interactions
    """
    session_id = models.CharField(max_length=100, unique=True)
    bot_id = models.CharField(max_length=100)
    user_email = models.EmailField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.bot_id} - {self.user_email or 'Anonymous'}"