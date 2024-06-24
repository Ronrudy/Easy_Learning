""" Test delete feature
"""
from models.engine.file_storage import FileStorage
from models.activity import Activity
from models.game import Game

fs = FileStorage()

# All Activities
all_activities = fs.all(Activity)
print("All Activity: {}".format(len(all_activities.keys())))
for activity_key in all_activities.keys():
    print(all_activities[activity_key])

# Create a new Activity
new_activity = Activity()
new_activity.name = "Reading"
fs.new(new_activity)
fs.save()
print("New Activity: {}".format(new_activity))


# Delete the new Activity
fs.delete(new_activity)

# All Activity
all_states = fs.all(Activity)
print("All Activities: {}".format(len(all_activities.keys())))
for activity_key in all_activities.keys():
    print(all_activities[activity_key])
    