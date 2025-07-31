from django.db import models

# Create your models here.
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.models import AbstractUser
class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, password=None, user_type=None, **extra_fields):
        if not email:
            raise ValueError('Email is required')
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, user_type=user_type, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
class CustomUser(AbstractUser):
    USER_TYPE_CHOICES = (
        ('jobseeker', 'Job Seeker'),
        ('recruiter', 'Recruiter'),
    )

    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES)
    email = models.EmailField(unique=True)
    USERNAME_FIELD = 'email' 
    REQUIRED_FIELDS = ['username']
    
    objects = CustomUserManager()
    
    def __str__(self):
        return f"{self.username} ({self.get_user_type_display()})"
    

    

    



