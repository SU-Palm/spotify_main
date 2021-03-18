# -*- coding: utf-8 -*-
"""
Created on Sun Mar  7 12:29:00 2021
@author: erika
"""
# NOTE: not yet tested 

# Resources: 
    ## Custom User Model: https://www.youtube.com/watch?v=eCeRC7E8Z7Y
    ## Models fields: https://docs.djangoproject.com/en/3.1/ref/models/fields/#field-options
    ## Spotify: https://developer.spotify.com/console/get-current-user-top-artists-and-tracks/ 
    ## Spotify: https://developer.spotify.com/documentation/web-api/reference/#endpoint-get-users-top-artists-and-tracks
    ## Location Field: # https://github.com/caioariede/django-location-field 
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from location_field.models.plain import PlainLocationField

class MyAccountManager(BaseUserManager):
    def create_user(self, email, username, password=None):

        if not email: 
            raise ValueError("Users must have an email address")
        if not username: 
            raise ValueError("Users must have a username")
            
        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, username, password):
        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
            password=password,
        )
        user.is_admin=True
        user.is_staff=True
        user.is_superuser=True
        user.save(using=self._db)
        return user
            
class Account(AbstractBaseUser):
# Django's required fields
    email           = models.EmailField(verbose_name="email", max_length=60, unique=True)
    username        = models.CharField(max_length=30, unique = True)
    date_joined     = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login      = models.DateTimeField(verbose_name='last login', auto_now = True)
    is_admin        = models.BooleanField(default=False)
    is_actve        = models.BooleanField(default=True)
    is_staff        = models.BooleanField(default=False)
    is_superuser    = models.BooleanField(default=False)
    
# Spotibae's added fields
    first_name      = models.CharField(max_length=30,null=True, blank=True)
    last_name       = models.CharField(max_length=30,null=True, blank=True)

    phone           = models.CharField(verbose_name='phone number', max_length=10, unique=True, null=True, blank=True)
    insta           = models.CharField(verbose_name='instagram handle', max_length=40, unique=True,null=True, blank=True)
    
    dob             = models.DateTimeField(verbose_name='date of birth',null=True, blank=True)
    gender          = models.CharField(max_length=15, null=True, blank=True)
    location        = models.CharField(max_length=100, null=True, blank=True)
    # location      = models.PlainLocationField() 
    
    match_radius    = models.CharField(max_length=30,null=True, blank=True)
    #match_radius   = PlainLocationField()
    age_range       = models.CharField(verbose_name='age preference', max_length=7,null=True, blank=True)
    gender_preference = models.CharField(max_length=15,null=True, blank=True)
 
# Spotibae's added fields: Potential dummy variables
    # User's song info: 
    top_tracks_ids      = models.CharField(max_length=50)        #array of 10 max, encoded as JSON 
    top_tracks_names    = models.CharField(max_length=50)        #array of 10 max, encoded as JSON
    top_artist_ids      = models.CharField(max_length=100)        #array of 10 max, encoded as JSON
    top_artist_names    = models.CharField(max_length=100)        #array of 10 max, encoded as JSON
    time_frame          = models.DurationField(null=True, blank=True)    #3 possible options: long_term=years, medium_term=6mo, short_term=4mo
        
    # User's Spotify access authorization info
    spotify_token  = models.CharField(max_length=100) 
    client_id      = models.CharField(max_length=100)
    client_secret  = models.CharField(max_length=100)
    response_type  = models.CharField(max_length=50)
    redirect_uri   = models.CharField(max_length=100) 
    state          = models.CharField(max_length=50)
    scopes         = models.CharField(max_length=100)
    grant_type     = models.CharField(max_length=50)
    code           = models.CharField(max_length=100)
        
# Use email to sign in
    USERNAME_FIELD = 'email'
    
# Required fields to create account
    REQUIRED_FIELDS = ['email', 'username', 'password']
    
# Django's required functions
    def __str__(self):
        return self.email
    
    def has_perm(self, perm, obj=None):
        return self.is_admin
    
    def has_module_perms(self, app_label):
        return True
    
        
    