# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 14:15:59 2021

@author: erika
"""

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.
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
    age_range       = models.CharField(verbose_name='age preference', max_length=7)
    gender_preference = models.CharField(max_length=15)

# Spotibae's added fields: Potential dummy variables
    # User's song info: 
    top_tracks_ids      = models.CharField(max_length = 250)        #array of 10 max, encoded as JSON 
    top_tracks_names    = models.CharField(max_length = 500)        #array of 10 max, encoded as JSON
    top_artist_ids      = models.CharField(max_length = 250)        #array of 10 max, encoded as JSON
    top_artist_names    = models.CharField(max_length = 500)        #array of 10 max, encoded as JSON
    time_frame          = models.DurationField(max_length = 30)    #3 possible options: long_term=years, medium_term=6mo, short_term=4mo
       
    # User's Spotify access authorization info
    spotify_token  = models.CharField(max_length = 250) 
    client_id      = models.CharField(max_length = 250)
    client_secret  = models.CharField(max_length = 250)
    response_type  = models.CharField(max_length = 250)
    redirect_uri   = models.CharField(max_length = 250) 
    state          = models.CharField(max_length = 250)
    scopes         = models.CharField(max_length = 250)
    grant_type     = models.CharField(max_length = 250)
    code           = models.CharField(max_length = 250)

    # Fields used for matching
    match_matrix   = models.CharField(max_length = 10000)
    score_matrix   = models.CharField(max_length = 10000)
    match_list     = models.CharField(max_length = 10000)
    unknowns_list  = models.CharField(max_length = 10000)

# Use email to sign in
    USERNAME_FIELD = 'email'
    
# Required fields to create account
    REQUIRED_FIELDS = ['username', 'password']
    
# Django's required functions
    def __str__(self):
        return self.email
    
    def has_perm(self, perm, obj=None):
        return self.is_admin
    
    def has_module_perms(self, app_label):
        return True