from music21 import environment

# Create a UserSettings object
us = environment.UserSettings()

# Print all the settings
print("Music21 User Settings:")
for key, value in us.items():
    print(f"  {key}: {value}")
