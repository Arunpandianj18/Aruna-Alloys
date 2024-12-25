# import speech_recognition as sr
# import pyttsx3
# from pymodbus.client import ModbusTcpClient
# import time
# TesleadSmartSyncX = None
# def hmi_sync():
#     global TesleadSmartSyncX
#     ip_address = '127.0.0.1'
#     TesleadSmartSyncX = ModbusTcpClient(ip_address)
#     TesleadSmartSyncX.connect()
# hmi_sync()

# def speak(text):
#     engine = pyttsx3.init()
#     engine.say(text)
#     engine.runAndWait()

# def recognize_speech():
#     recognizer = sr.Recognizer()
#     with sr.Microphone() as source:
#         print("Listening...")
#         audio = recognizer.listen(source)
#         try:5
#             command = recognizer.recognize_google(audio)
#             print(f"You said: {command}")
#             return command.lower()
#         except sr.UnknownValueError:
#             return ""
#         except sr.RequestError:
#             print("Sorry, my speech service is down.")
#             return ""

# def main():
#     global TesleadSmartSyncX
#     speak("How can I help you?")
#     while True:
#         command = recognize_speech()
#         if "start cycle" in command:
#             TesleadSmartSyncX.write_register(2000, 1)
#             time.sleep(1)
#             speak("Cycle started.")
#         elif "stop cycle" in command:
#             TesleadSmartSyncX.write_register(2000, 0)
#             speak("Cycle stopped.")
#         else:
#             # speak("Sorry, I didn't catch that.")
#             pass

# if __name__ == "__main__":
#     main()


# import speech_recognition as sr
# import pyttsx3
# from pymodbus.client import ModbusTcpClient
# import time

# TesleadSmartSyncX = None

# def hmi_sync():
#     global TesleadSmartSyncX
#     ip_address = '127.0.0.1'
#     TesleadSmartSyncX = ModbusTcpClient(ip_address)
#     TesleadSmartSyncX.connect()

# hmi_sync()

# def speak(text):
#     engine = pyttsx3.init()
#     engine.say(text)
#     engine.runAndWait()

# def process_command(command):
#     global TesleadSmartSyncX
#     if "start cycle" in command:
#         TesleadSmartSyncX.write_register(2000, 1)
#         time.sleep(1)
#         speak("Cycle started.")
#     elif "stop cycle" in command:
#         TesleadSmartSyncX.write_register(2000, 0)
#         speak("Cycle stopped.")
#     elif "start filling water" in command:
#         TesleadSmartSyncX.write_register(2001, 1)
#         speak("Prefilling Started.")
#     elif "stop filling water" in command:
#         TesleadSmartSyncX.write_register(2001, 0)
#         speak("Prefilling stopped.")
#     elif "turn on booster" in command:
#         TesleadSmartSyncX.write_register(2002, 1)
#         speak("Booster Started.")
#     elif "turn off booster" in command:
#         TesleadSmartSyncX.write_register(2002, 0)
#         speak("Booster stopped.")
#     else:
#         # speak("Sorry, I didn't catch that.")
#         pass

# def recognize_speech(recognizer, audio):
#     try:
#         command = recognizer.recognize_google(audio)
#         print(f"You said: {command}")
#         process_command(command.lower())
#     except sr.UnknownValueError:
#         pass
#     except sr.RequestError:
#         print("Sorry, my speech service is down.")

# def main():
#     recognizer = sr.Recognizer()
#     mic = sr.Microphone()
#     speak("How can I help you?")
#     stop_listening = recognizer.listen_in_background(mic, recognize_speech)

#     # Keep the program running indefinitely
#     while True:
#         time.sleep(0)

# if __name__ == "__main__":
#     main()





# import pyaudio
# import wave

# # Parameters for audio recording
# FORMAT = pyaudio.paInt16
# CHANNELS = 1
# RATE = 44100
# CHUNK = 1024
# RECORD_SECONDS = 5
# WAVE_OUTPUT_FILENAME = "output.wav"

# audio = pyaudio.PyAudio()

# # Start Recording
# stream = audio.open(format=FORMAT, channels=CHANNELS,
#                 rate=RATE, input=True,
#                 frames_per_buffer=CHUNK)
# print("Recording...")

# frames = []

# try:
#     while True:
#         data = stream.read(CHUNK)
#         frames.append(data)
# except KeyboardInterrupt:
#     print("Recording stopped")

# # Stop Recording
# stream.stop_stream()
# stream.close()
# audio.terminate()

# # Save the recorded data as a WAV file
# wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
# wf.setnchannels(CHANNELS)
# wf.setsampwidth(audio.get_sample_size(FORMAT))
# wf.setframerate(RATE)
# wf.writeframes(b''.join(frames))
# wf.close()




# import speech_recognition as sr
# import pyttsx3
# import time

# # Initialize the speech recognition and text-to-speech engines
# recognizer = sr.Recognizer()
# engine = pyttsx3.init()

# # Function to speak a message
# def speak(message):
#     engine.say(message)
#     engine.runAndWait()

# # Mockup for TesleadSmartSyncX class
# class TesleadSmartSyncX:
#     @staticmethod
#     def write_register(register, value):
#         print(f"Register {register} set to {value}")

# # Continuous listening function
# def listen_for_commands():
#     with sr.Microphone() as source:
#         print("Listening for commands...")
#         while True:
#             try:
#                 # Adjust for ambient noise and listen
#                 recognizer.adjust_for_ambient_noise(source)
#                 audio = recognizer.listen(source)

#                 # Recognize speech using Google Web Speech API
#                 command = recognizer.recognize_google(audio).lower()
#                 print(f"Command received: {command}")

#                 # Check for specific commands
#                 if "start cycle" in command:
#                     TesleadSmartSyncX.write_register(2000, 1)
#                     time.sleep(1)
#                     speak("Cycle started.")
#                 elif "stop cycle" in command:
#                     TesleadSmartSyncX.write_register(2000, 0)
#                     speak("Cycle stopped.")
#                 elif "start filling water" in command:
#                     TesleadSmartSyncX.write_register(2001, 1)
#                     speak("Prefilling Started.")
#                 elif "stop filling water" in command:
#                     TesleadSmartSyncX.write_register(2001, 0)
#                     speak("Prefilling stopped.")
#                 elif "turn on booster" in command:
#                     TesleadSmartSyncX.write_register(2002, 1)
#                     speak("Booster Started.")
#                 elif "turn off booster" in command:
#                     TesleadSmartSyncX.write_register(2002, 0)
#                     speak("Booster stopped.")
#                 else:
#                     print("Command not recognized.")

#             except sr.UnknownValueError:
#                 print("Sorry, I could not understand the audio.")
#                 continue
#             except sr.RequestError as e:
#                 print(f"Could not request results from Google Speech Recognition service; {e}")

# if __name__ == "__main__":
#     listen_for_commands()



import speech_recognition as sr
import pyttsx3
import time

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(message):
    engine.say(message)
    engine.runAndWait()

class TesleadSmartSyncX:
    @staticmethod
    def write_register(register, value):
        print(f"Register {register} set to {value}")

def listen_for_commands():
    with sr.Microphone() as source:
        print("Adjusting for ambient noise. Please wait...")
        recognizer.adjust_for_ambient_noise(source, duration=1)  
        print("Listening for commands...")

        while True:
            try:
                print("Please say a command...")
                audio = recognizer.listen(source, timeout=5) 
                command = recognizer.recognize_google(audio).lower()
                print(f"Command received: {command}")
                if "start cycle" in command:
                    TesleadSmartSyncX.write_register(2000, 1)
                    time.sleep(1)
                    speak("Cycle started.")
                elif "stop cycle" in command:
                    TesleadSmartSyncX.write_register(2000, 0)
                    speak("Cycle stopped.")
                elif "start filling water" in command:
                    TesleadSmartSyncX.write_register(2001, 1)
                    speak("Prefilling Started.")
                elif "stop filling water" in command:
                    TesleadSmartSyncX.write_register(2001, 0)
                    speak("Prefilling stopped.")
                elif "turn on booster" in command:
                    TesleadSmartSyncX.write_register(2002, 1)
                    speak("Booster Started.")
                elif "turn off booster" in command:
                    TesleadSmartSyncX.write_register(2002, 0)
                    speak("Booster stopped.")
                else:
                    print("Command not recognized.")

            except sr.UnknownValueError:
                print("Sorry, I could not understand the audio. Please try again.")
                continue  
            except sr.RequestError as e:
                print(f"Could not request results from Google Speech Recognition service; {e}")
                break 
            except Exception as e:
                print(f"An unexpected error occurred: {e}")
                continue 

if __name__ == "__main__":
    listen_for_commands()