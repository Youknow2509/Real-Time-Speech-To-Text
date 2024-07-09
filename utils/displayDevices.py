import speech_recognition as sr

# Initialize recognizer class
recognizer = sr.Recognizer()

# Get list of all audio input devices
all_microphones = sr.Microphone.list_microphone_names()

# Print all available audio input devices
print("Available Microphones:")
for index, microphone_name in enumerate(all_microphones):
    print(f"{index}: {microphone_name}")

# Get list of all audio output devices (if supported by the library)
all_speakers = sr.AudioFile.list_devices()

# Print all available audio output devices
print("\nAvailable Speakers:")
for index, speaker_name in enumerate(all_speakers):
    print(f"{index}: {speaker_name}")
