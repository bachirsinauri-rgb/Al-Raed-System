import os
VERSION = "V23.0 - Sovereignty"
KEY = os.getenv("SECRET_LIFE_KEY")

def activate():
    print(f"🚀 [SYSTEM]: {VERSION} Activated.")
    print("🛰️ [X7]: Satellite Link Secure.")
    if KEY: print("🔓 [AUTH]: Life Key Injected Successfully.")

if __name__ == "__main__":
    activate()
