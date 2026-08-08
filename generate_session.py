"""
Temporary script to generate Pyrogram session string
Run this ONCE locally to authenticate and get your SESSION token
Then add the output to your .env file
"""

from pyrogram import Client
import sys
import os

# You'll need to input these from https://my.telegram.org/apps
API_ID = int(input("Enter your API_ID: "))
API_HASH = input("Enter your API_HASH: ")
PHONE_NUMBER = input("Enter your Telegram phone number (with country code, e.g., +1234567890): ")

# Create a client
app = Client(
    "session_generator",
    api_id=API_ID,
    api_hash=API_HASH,
    phone_number=PHONE_NUMBER
)

# Start the client (this will prompt for OTP if 2FA is enabled)
try:
    app.start()
    print("\n✅ Successfully logged in!")
    
    # Get the session string
    session_string = app.export_session_string()
    
    print("\n" + "="*70)
    print("📋 YOUR SESSION STRING (Add this to your .env as SESSION=):")
    print("="*70)
    print(session_string)
    print("="*70)
    print("\n✅ Copy the above session string and add it to your .env file")
    print("Format: SESSION=<paste-the-string-above>")
    
    # Stop the client
    app.stop()
    
except Exception as e:
    print(f"\n❌ Error: {e}")
    print("Make sure you:")
    print("1. Entered the correct API_ID and API_HASH from https://my.telegram.org/apps")
    print("2. Used correct phone number format with country code")
    print("3. Have internet connection")
    sys.exit(1)
