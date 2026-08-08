"""
Generate SESSION string - Run this in Replit or local Python
"""
from pyrogram import Client

print("=" * 70)
print("TELEGRAM SESSION GENERATOR")
print("=" * 70)

# Get your values from https://my.telegram.org/apps
API_ID = int(input("\nEnter your API_ID: "))
API_HASH = input("Enter your API_HASH: ")
PHONE = input("Enter your Telegram phone number (+country_code): ")

print("\nStarting authentication...")

app = Client("session_gen", api_id=API_ID, api_hash=API_HASH, phone_number=PHONE)

try:
    app.start()
    print("\n✅ Successfully logged in!")
    
    session = app.export_session_string()
    
    print("\n" + "=" * 70)
    print("YOUR SESSION STRING:")
    print("=" * 70)
    print(session)
    print("=" * 70)
    print("\n📋 Copy the above string and add to .env as:")
    print("SESSION=<paste-above-string>")
    
    app.stop()
    
except Exception as e:
    print(f"\n❌ Error: {e}")
