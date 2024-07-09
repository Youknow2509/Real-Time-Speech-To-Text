import atexit
import speech_recognition as sr
import whisper
import numpy as np
import torch
import psutil
import os
import gc

def cleanup():
    # Clean up resources
    if torch.cuda.is_available():
        torch.cuda.empty_cache()  # Clear GPU memory if CUDA is available
    else:
        torch.cuda.empty_cache()

    psutil.Process(os.getpid()).memory_full_info().rss  # Get the current memory usage
    gc.collect()  # Perform garbage collection to release unreferenced memory

def main():
    # Load the model
    model = whisper.load_model("base")
    
    # Initialize recognizer class (for recognizing speech)
    recognizer = sr.Recognizer()

    DEVICE_INDEX = 0  # Index of device you use for input (microphone)

    # Capture audio from the microphone
    with sr.Microphone(sample_rate=16000, device_index=DEVICE_INDEX) as source:
        print("Say something...")
        recognizer.adjust_for_ambient_noise(source)
        recognizer.energy_threshold = 1000

        try:
            while True:
                audio_data = recognizer.listen(source, phrase_time_limit=2)

                try:
                    # Convert AudioData to raw bytes
                    raw_audio = audio_data.get_raw_data(convert_rate=None, convert_width=None)

                    # Convert raw audio to numpy array
                    audio_np = np.frombuffer(raw_audio, dtype=np.int16).astype(np.float32) / 32768.0

                    # Read the transcription
                    result = model.transcribe(audio_np, fp16=torch.cuda.is_available())
                    text = result['text'].strip()

                    print("You said:", text)
                except sr.UnknownValueError:
                    print("Could not understand audio")
                except sr.RequestError as e:
                    print(f"Could not request results; {e}")
        except KeyboardInterrupt:
            print("\nStopping...")

if __name__ == "__main__":
    atexit.register(cleanup)  # Register cleanup function to be called when the script exits
    main()
