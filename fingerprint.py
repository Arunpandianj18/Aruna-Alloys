# import serial
# import time
# import os

# # Replace with your fingerprint sensor's serial port
# SERIAL_PORT = '/dev/ttyUSB0'  # For Linux
# # SERIAL_PORT = 'COM3'  # For Windows
# BAUD_RATE = 57600

# def initialize_sensor():
#     try:
#         ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)
#         time.sleep(2)  # Allow time for the serial connection to initialize
#         return ser
#     except Exception as e:
#         print(f"Error initializing sensor: {e}")
#         return None

# def capture_fingerprint(ser):
#     print("Place your finger on the sensor...")
#     # Wait for the fingerprint to be placed
#     while True:
#         if ser.in_waiting > 0:
#             fingerprint_data = ser.read(512)  # Read fingerprint data
#             if fingerprint_data:  # Check if data is received
#                 return fingerprint_data
#         time.sleep(0.1)

# def store_fingerprint(fingerprint_data, user_id):
#     filename = f"fingerprint_{user_id}.bin"
#     with open(filename, 'wb') as f:
#         f.write(fingerprint_data)
#     print(f"Fingerprint stored as {filename}")

# def identify_fingerprint(ser):
#     print("Place your finger on the sensor for identification...")
#     fingerprint_data = capture_fingerprint(ser)
    
#     # Here you would typically compare the captured fingerprint with stored fingerprints
#     # This is a placeholder for the identification logic
#     for user_id in os.listdir('.'):
#         if user_id.startswith('fingerprint_'):
#             with open(user_id, 'rb') as f:
#                 stored_fingerprint = f.read()
#                 if fingerprint_data == stored_fingerprint:  # Simplified comparison
#                     print(f"Fingerprint matched with {user_id}")
#                     return user_id
#     print("No match found.")
#     return None

# def main():
#     ser = initialize_sensor()
#     if ser is None:
#         return

#     while True:
#         action = input("Enter 'capture' to capture a fingerprint or 'identify' to identify: ").strip().lower()
#         if action == 'capture':
#             user_id = input("Enter user ID for the fingerprint: ")
#             fingerprint_data = capture_fingerprint(ser)
#             store_fingerprint(fingerprint_data, user_id)
#         elif action == 'identify':
#             identify_fingerprint(ser)
#         else:
#             print("Invalid action. Please enter 'capture' or 'identify'.")

# if __name__ == "__main__":
#     main()

import serial
from PyFingerprint import PyFingerprint
port = 'COM3'  # Replace with the actual port
baudrate = 115200
ser = serial.Serial(port, baudrate) 
fp = PyFingerprint(ser) 

# Get fingerprint data from the sensor 
fingerprint_data = fp.get_image()

#  Process fingerprint data for enrollment (specific details depend on the sensor model)
fp.enroll(fingerprint_data) 
# Get fingerprint data from the sensor 
fingerprint_data = fp.get_image()

# Verify the fingerprint against enrolled data (details depend on sensor model)
result = fp.verify(fingerprint_data) 

if result:
    print("Fingerprint matched!") 
else:
    print("Fingerprint doesn't match.")