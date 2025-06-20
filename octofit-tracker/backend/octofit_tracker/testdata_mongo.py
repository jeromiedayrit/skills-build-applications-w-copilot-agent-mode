from pymongo import MongoClient
from datetime import timedelta

client = MongoClient('localhost', 27017)
db = client['octofit_db']

# Drop existing collections
db.users.drop()
db.teams.drop()
db.activity.drop()
db.leaderboard.drop()
db.workouts.drop()

# Insert users
users = [
    {"username": "thundergod", "email": "thundergod@mhigh.edu", "password": "thundergodpassword"},
    {"username": "metalgeek", "email": "metalgeek@mhigh.edu", "password": "metalgeekpassword"},
    {"username": "zerocool", "email": "zerocool@mhigh.edu", "password": "zerocoolpassword"},
    {"username": "crashoverride", "email": "crashoverride@hmhigh.edu", "password": "crashoverridepassword"},
    {"username": "sleeptoken", "email": "sleeptoken@mhigh.edu", "password": "sleeptokenpassword"},
]
user_ids = db.users.insert_many(users).inserted_ids

# Insert teams
blue_team = {"name": "Blue Team", "members": user_ids[:3]}
gold_team = {"name": "Gold Team", "members": user_ids[3:]}
db.teams.insert_many([blue_team, gold_team])

# Insert activities
activities = [
    {"user": user_ids[0], "activity_type": "Cycling", "duration": 60*60},
    {"user": user_ids[1], "activity_type": "Crossfit", "duration": 2*60*60},
    {"user": user_ids[2], "activity_type": "Running", "duration": 90*60},
    {"user": user_ids[3], "activity_type": "Strength", "duration": 30*60},
    {"user": user_ids[4], "activity_type": "Swimming", "duration": 75*60},
]
db.activity.insert_many(activities)

# Insert leaderboard
leaderboard = [
    {"user": user_ids[0], "score": 100},
    {"user": user_ids[1], "score": 90},
    {"user": user_ids[2], "score": 95},
    {"user": user_ids[3], "score": 85},
    {"user": user_ids[4], "score": 80},
]
db.leaderboard.insert_many(leaderboard)

# Insert workouts
workouts = [
    {"name": "Cycling Training", "description": "Training for a road cycling event"},
    {"name": "Crossfit", "description": "Training for a crossfit competition"},
    {"name": "Running Training", "description": "Training for a marathon"},
    {"name": "Strength Training", "description": "Training for strength"},
    {"name": "Swimming Training", "description": "Training for a swimming competition"},
]
db.workouts.insert_many(workouts)

print("Test data successfully inserted into octofit_db.")
