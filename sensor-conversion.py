thresholds = {
    'index': 500,   # These values are going to be changed once I learn the characteristics of the flex sensors.
    'middle': 500,
    'ring': 500,
    'pinky': 500
}

# Mapping of finger positions
""""
Mapping is extremely important here: The technology will need to correctly
interpret which notes correspond to which finger, an integral part of playing the piano.
Depending on the song however, this will change and a new algorithm might be needed. 
"""
finger_note_mapping = {
    'index': 'C',
    'middle': 'D',
    'ring': 'E',
    'pinky': 'F'
}

# Detect finger positions based on sensor readings
def detect_finger_positions(sensor_readings):
    finger_positions = {} # This will be read from the flex sensors.
    for finger, threshold in thresholds.items():
        if sensor_readings[finger] > threshold:
            finger_positions[finger] = True  # Finger is bent/playing a note
        else:
            finger_positions[finger] = False  # Finger is straight
    return finger_positions

# Function to then connect finger positions to piano notes
def map_finger_positions_to_notes(finger_positions):
    played_notes = []
    for finger, bent in finger_positions.items():
        if bent:
            played_notes.append(finger_note_mapping[finger])
    return played_notes

# Sample sensor readings (replace with actual sensor data)
sensor_readings = {
    'index': 600,
    'middle': 400,
    'ring': 550,
    'pinky': 300
}

# Detect finger positions
finger_positions = detect_finger_positions(sensor_readings)

# Map finger positions to piano notes
played_notes = map_finger_positions_to_notes(finger_positions)

# Print the detected piano notes
print("Detected Piano Notes:", played_notes)
