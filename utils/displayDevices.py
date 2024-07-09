import pyaudio

# Initialize PyAudio
pa = pyaudio.PyAudio()

# Print general information
print("General Information:")
print(f"Default Input Device Index: {pa.get_default_input_device_info()['index']}")
print(f"Default Output Device Index: {pa.get_default_output_device_info()['index']}")
print()

# Print detailed information about input devices (microphones)
print("Input Devices (Microphones):")
for i in range(pa.get_device_count()):
    device_info = pa.get_device_info_by_index(i)
    if device_info["maxInputChannels"] > 0:
        print(f"Device {i}: {device_info['name']}")
        print(f"  Channels: {device_info['maxInputChannels']}")
        print(f"  Sample Rate: {int(device_info['defaultSampleRate'])}")
        if 'inputLatency' in device_info:
            print(f"  Input Latency: {device_info['inputLatency']}")
        else:
            print("  Input Latency: Not available")
        print()

# Print detailed information about output devices (speakers)
print("Output Devices (Speakers):")
for i in range(pa.get_device_count()):
    device_info = pa.get_device_info_by_index(i)
    if device_info["maxOutputChannels"] > 0:
        print(f"Device {i}: {device_info['name']}")
        print(f"  Channels: {device_info['maxOutputChannels']}")
        print(f"  Sample Rate: {int(device_info['defaultSampleRate'])}")
        if 'outputLatency' in device_info:
            print(f"  Output Latency: {device_info['outputLatency']}")
        else:
            print("  Output Latency: Not available")
        print()
