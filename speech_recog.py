from vosk import Model, KaldiRecognizer
import numpy as np
import sounddevice as sd

# Initialize Vosk speech recognition model
# You can get the model from https://alphacephei.com/vosk/models
model_vosk = Model("vosk_model")
recognizer = KaldiRecognizer(model_vosk, 16000)

# Initialize Variable
attempts = 0

while True:
    print(f"\nAttempt {attempts + 1}")

    recognizer.Reset() #Reset before the next attempt

    # Record audio using sounddevice
    duration = 3 # You can change the duration time to record your voice
    sample_rate = 16000
    recording = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1, dtype='int16')
    sd.wait()
                
    # Convert the recorded audio to bytes for Vosk Model
    audio_data = np.array(recording, dtype=np.int16).tobytes()
                
    if recognizer.AcceptWaveform(audio_data):    
        recognition = recognizer.Result()
        text = recognition.split(":")
        recognized_text = text[1].strip().replace('"', '').replace('}', '').replace('\n', '')
        recognized_text = recognized_text[:1].upper() + recognized_text[1:]
        print("Recognized Text:", recognized_text)
                    
    attempts += 1