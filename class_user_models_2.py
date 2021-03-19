# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 17:48:27 2021

@author: erika
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Mar  7 12:29:00 2021

@author: erika
"""
# NOTE: not yet tested 

# Create a user model 
    # Folder: apps > models.py

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
    is_superuser    = models.BooelanField(default=False)
    
# Spotibae's additional fields
    first_name      = models.CharField(max_length=30)
    last_name       = models.CharField(max_length=30)

    phone           = models.CharField(verbose_name='phone number', max_length=10, unique=True)
    insta           = models.CharField(verbose_name='instagram handle', max_length=40, unique=True)
    
    dob             = models.DateTimeField(verbose_name='date of birth')
    gender          = models.CharField(max_length=15)
    location        = models.CharField(max_length=100)
    # location      = models.PlainLocationField() 
    
    match_radius    = models.CharField(max_length=30)
    #match_radius   = PlainLocationField()
    age_range       = models.CharField(verbose_name='age preference', max_length='7')
    gender_preference = models.CharField(max_length=15)
 
# Spotibae's added fields: Potential dummy variables
    # User's song info: 
    top_tracks_ids      = models.CharField()        #array of 10 max, encoded as JSON 
    top_tracks_names    = models.CharField()        #array of 10 max, encoded as JSON
    top_artist_ids      = models.CharField()        #array of 10 max, encoded as JSON
    top_artist_names    = models.CharField()        #array of 10 max, encoded as JSON
    time_frame          = models.DurationField()    #3 possible options: long_term=years, medium_term=6mo, short_term=4mo
        
    # User's Spotify access authorization info
    spotify_token  = models.CharField() 
    client_id      = models.CharField()
    client_secret  = models.CharField()
    response_type  = models.CharField()
    redirect_uri   = models.CharField() 
    state          = models.CharField()
    scopes         = models.CharField()
    grant_type     = models.CharField()
    code           = models.CharField()
      
    # Fields used for matching
    match_matrix   = models.CharField()
    score_matrix   = models.CharField()
    match_list     = models.CharField()
    unknowns_list  = models.CharField()
    
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
    