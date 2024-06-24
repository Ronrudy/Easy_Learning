#!/usr/bin/python3
""" Test delete feature
"""
from models.engine.file_storage import FileStorage
from models.activityCategory import ActivityCategory

fs = FileStorage()

# All ActivityCategory
all_activitycategory = fs.all(ActivityCategory)
print("All ActivityCategory: {}".format(len(all_activitycategory.keys())))
for activitycategory_key in all_activitycategory.keys():
    print(all_activitycategory[activitycategory_key])
