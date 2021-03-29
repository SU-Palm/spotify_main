from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from .models import Account, MyAccountManager
import os
from django.conf import settings

# Test Function
def hello_django():
    print("Hello Django!")
hello_django()

# Match function
def updateMatches(user): 
    # Check whether user is in database

    # Access user's info 
    user = Account.objects.get(name=user)

    # Update user's score matrix file 
    updateScoreMatrix(user)

    # Update and return user's match list and unknowns list
    user.match_list, user.unknowns_list = updateMatchList(user)
    return user.match_list, user.unknowns_list

def updateScoreMatrix(user):
    # set path to a variable
    path = user.match_matrix.path

    # erase info from file
    open(path, 'w').close()

    # open file
    f_score_matrix = open(path, 'w')
    file_score_matrix = File(f)

    # get user's info 
    gender = user.get_gender()
    age = user.get_age()
    match_radius, age_range, gender_preference = user.get_preferences()
    songs = user.get_top_tracks_names()
    artists = user.get_top_artist_names()    

    # convert age range to integer values (assume age format is as follows: '## - ##')
    age_range_min = int(age_range[:1])
    age_range_max = int(age_range[-2:])

    # use for loop to cycle through users in database
    for user_compared in database:
        gender_compared = user_compared.get_gender()
        age_compared = user_compared.get_age()
        match_radius_compared, age_range_compared, gender_preference_compared = user_compared.get_preferences()
        songs_compared = user_compared.get_top_tracks_names()
        artists_compared = user_compared.get_top_artist_names()   

        # convet age to integer value (assume age format is as follows: '##')
        age_compared = int(age_compared)

        # access and populate 
        file_score_matrix.write('{0}: '.format(user_compared.username)

        if ((age_range_min > age_compared) || (age_range_max < age_compared)):
            file_score_matrix.write('00 ')
            
        (elif ((age_range_max >= age_compared) && (age_range_min <= age_compared)):
            file_score_matrix.write('01 '))
    
        [else:
            file_score_matrix.write('-1 ')]

        if (gender_preference != gender_compared):
            file_score_matrix.write('00 ')

        (elif (gender_preference == gender_compared):
            file_score_matrix.write('01 '))

        [else:
            file_score_matrix.write('-1 ')]
        
        score = calculateScore(user, user_compared)

        if ((score > 0) && (score < 161)):
            file_score_matrix.write(char(score))
        [else:
            file_score_matrix.write('000')]
    
    # close file
    file_score_matrix.close()
    f_score_matrix.close()
    
def calculateScore(user, user_compared):
    # initialize variables for keeping track of match score 
    score = 0
    same_songs = 0
    same_artists = 0

    # assign user's and compared user's top songs and artists to variables
    song_list = user.get_top_tracks_names()
    song_list_compared = user_compared.get_top_tracks_names()
    artist_list = user.get_top_artist_names()
    artist_list_compared = user_compared.get_top_artist_names()

    # check that none of the following are empty: the user's song list or artist list, the compared user's song list or artist list
    if (song_list == ''):
        score = -1
    (elif (song_list_compared == ''):
        score = -1)
    (elif (artist_list == ''):
        score = -1)
    (elif (artist_list_compared == '')
        score = -1)
    [else:
        # compute values for score, same songs, and same artists
        for song in song_list: 
            for song_compared in song_list_compared:
                if (song == song_compared):
                    score = score + 5
                    same_songs = same_songs + 1
        for artist in artist_list:
            for artist_compared in artist_list_compared:
                if (artist == artist_compared):
                    score = score + 10
                    same_artists = same_artists + 1 
        
        # calculate score 
        # (if 10 songs and 10 artists are taken from each user, possible scores range from 0 to 160)
        same_songs_score = ((same_songs/5)*1.5) + (same_songs/2)
        same_artist_score = (same_artist/5)*1.5 + (same_artist/2)
        score = score * ((same_songs_score + same_artist_score)/2)]

    # return score
    return score
    
def updateMatchList(user): 
    # set paths to variables
    path_match_list = user.match_list.path
    path_unknowns_list = user.unknowns_list.path
    path_score_matrix = user.score_matrix.path

    # erase info from match list and unknowns list
    open(path_match_list, 'w').close()
    open(path_unknowns_list, 'w').close()

    # open score matrix and reopen match list and unknowns list
    f_match_list = open(path_match_list, 'w')
    file_match_list = File(f_match_list)
    f_unknowns_list = open(path_unknowns_list, 'w')
    file_unknowns_list = File(f_unknowns_list)
    f_score_matrix = open(path_score_matrix, 'w')
    file_score_matrix = File(f_score_matrix)

    # initialize list of suggested matches
    unsorted_match_list = []

    # access info in score matrix (info is formatted on each line as follows: 'username: ## ## ###')
    for line in file_score_matrix:
        if ((line[-9:-8] == '-1') || (line[-6:-5] == '-1') || (line[-3:] == '-1')):
            file_unknowns_list.write(username + '/n')
        (elif ((line[-9:-8] == '01') && (line[-6:-5] == '01') && (line[-3:] == '01')): 
            unsorted_match_list.append(line))

    # sort suggested matches list based on score (sorted from highest to lowest score)
    sorted_match_list = [0]

    for match in unsorted_match_list: 
        score = int(match[-3:])
        for j in sorted_score_list: 
            if (score > sorted_match_list[j]):
                sorted_match_list.insert(j, score)

    # append suggested matches to match list file     
    for match in sorted_match_list:
        file_match_list.write(match + '/n')

    # close files
    f_match_list.close()
    file_match_list.close()
    f_unknowns_list.close()
    file_unknowns_list.close()
    f_score_matrix.close()
    file_score_matrix.close()
