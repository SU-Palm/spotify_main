# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 09:57:32 2021

@author: erika
"""

# Resources: 
    ## Custom User Model: https://www.youtube.com/watch?v=eCeRC7E8Z7Y
    ## Models fields: https://docs.djangoproject.com/en/3.1/ref/models/fields/#field-options
    ## Spotify: https://developer.spotify.com/console/get-current-user-top-artists-and-tracks/ 
    ## Spotify: https://developer.spotify.com/documentation/web-api/reference/#endpoint-get-users-top-artists-and-tracks
    ## Location Field: # https://github.com/caioariede/django-location-field 
    ## Files: https://docs.djangoproject.com/en/3.1/topics/files/

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Define file upload location
def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.user.id, filename)

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
    is_active       = models.BooleanField(default=True)
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
        # Am I saving these all to the same file? 
    match_matrix   = models.FileField(upload_to = user_directory_path, max_length = 10000)
    score_list     = models.FileField(upload_to = user_directory_path, max_length = 1000)
    score_matrix   = models.FielField(upload_to = user_directory_path, max_length = 10000)
    match_list     = models.FielField(upload_to = user_directory_path, max_length = 10000)
    unknowns_list  = models.FileField(upload_to = user_directory_path, max_length = 10000)

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
    
# Get Django's required fields  
    def get_email(self):
        return self.email
    
    def get_username(self):
        return self.username 
    
    def get_date_joined(self):
        return self.date_joined 
    
    def get_last_login(self):
        return self.last_login
    
    def get_is_active(self):
        return self.is_active
    
    def get_is_staff(self):
        return self.is_staff
    
    def get_is_superuser(self):
        return self.is_superuser 
    
    def get_required_fields(self):
        return self.email, self.username, self.date_joined, self.last_login, self.is_admin, self.is_active, self.is_staff, self.is_superuser
    
# Get user's additional basic information 
    def get_first_name(self):
        return self.first_name

    def get_last_name(self):
        return self.last_name
    
    def get_phone(self):
        return self.phone
           
    def get_insta(self):
        return self.insta
    
    def get_dob(self):
        return self.dob
    
    def get_gender(self):
        return self.gender

    def get_location(self):
        return self.location
    
    def get_match_radius(self):
        return self.match_radius

    def get_age_range(self):
        return self.age_range
    
    def get_gender_preference(self):
        return self.gender_preference
    
    def get_user_info(self):
        return self.first_name, self.last_name, self.phone, self.insta, self.dob, self.gender, self.location
    
    def get_preferences(self):
        return self.match_radius, self.age_range, self.gender_preferences
    
# Get user's Spotify music information
    def get_top_tracks_ids(self):
        return self.top_tracks_ids
    
    def get_top_tracks_names(self):
        return self.top_tracks_names
    
    def get_top_artist_ids(self):
        return self.top_artist_ids
    
    def get_top_artist_names(self):
        return self.top_artist_names
    
    def get_time_frame(self):
        return self.time_frame
    
    def get_music_info(self):
        return self.top_tracks_ids, self.top_tracks_names, self.top_artist_ids, self.top_artist_names, self.time_frame

# Get user's Spotify connection information
    def get_spotify_token(self):
        return self.spotify_token
    
    def get_cliet_id(self):
        return self.client_id
    
    def get_client_secret(self):
        return self.client_secret
    
    def get_response_type(self):
        return self.response_type
    
    def get_redirect_uri(self):
        return self.redirect_uri
    
    def get_state(self):
        return self.state
    
    def get_scopes(self):
        return self.scopes
    
    def get_grant_type(self):
        return self.grant_type
    
    def get_code(self):
        return self.code
    
    def get_spotify_connection_info(self):
        return self.spotify_token, self.client_id, self.client_secret, self.response_type, self.redirect_uri, self.state, self.scopes, self.grant_type, self.code

# Get files used for finding matches
    def get_match_matrix(self):
        return self.match_matrix
    
    def get_score_list(self):
        return self.score_list
    
    def get_score_matrix(self):
        return self.score_matrix
    
    def get_match_list(self):
        return self.match_list 
    
    def get_unknowns_list(self):
        return self.unknowns_list

    def get_match_files(self):
        return self.match_matrix, self.score_list, self.score_matrix, self.match_list, self.unknowns_list
    
# Set Django's required fields  
    def set_email(self, x):
        self.email = x
    
    def set_username(self, x):
        self.username = x
    
    def set_date_joined(self, x):
        self.date_joined = x 
    
    def set_last_login(self, x):
        self.last_login = x
    
    def set_is_active(self, x):
        self.is_active = x
    
    def set_is_staff(self, x):
        self.is_staff = x
    
    def set_is_superuser(self, x):
        self.is_superuser = x
    
# Set user's additional basic information
    def set_first_name(self, x):
        self.first_name = x

    def set_last_name(self, x):
        self.last_name = x
    
    def set_phone(self, x):
        self.phone = x
           
    def set_insta(self, x):
        self.insta = x
    
    def set_dob(self, x):
        self.dob = x
    
    def set_gender(self, x):
        self.gender = x

    def set_location(self, x):
        self.location = x
    
    def set_match_radius(self, x):
        self.match_radius = x

    def set_age_range(self, x):
        self.age_range = x
    
    def set_gender_preference(self, x):
        self.get_gender_preference = x
        
# Set user's Spotify music information 
    def set_top_tracks_ids(self, x):
        self.top_tracks_ids = x
    
    def set_top_tracks_names(self, x):
        self.top_tracks_names = x
    
    def set_top_artist_ids(self, x):
        self.top_artist_ids = x
    
    def set_top_artist_names(self, x):
        self.top_artist_names = x
    
    def set_time_frame(self, x):
        self.time_frame = x
        
# Set user's Spotify connection information
    def set_spotify_token(self, x):
        self.spotify_token = x
    
    def set_cliet_id(self, x):
        self.client_id = x
    
    def set_client_secret(self, x):
        self.client_secret = x
    
    def set_response_type(self, x):
        self.response_type = x
    
    def set_redirect_uri(self, x):
        self.redirect_uri = x
    
    def set_state(self, x):
        self.state = x
    
    def set_scopes(self, x):
        self.scopes = x
    
    def set_grant_type(self, x):
        self.grant_type = x
    
    def set_code(self, x):
        self.code = x
        
# Set files used for finding matches
    def set_match_matrix(self, x):
        self.match_matrix = x
    
    def set_score_list(self, x):
        self.score_list = x
    
    def set_score_matrix(self, x):
        self.score_matrix = x
    
    def set_match_list(self, x):
        self.match_list = x
    
    def set_unknowns_list(self, x):
        self.unknowns_list = x