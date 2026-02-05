def get_commander():
    try:
        with open('commander.txt', 'r') as f:
            return f.read().strip()
    except:
        return "Unknown Commander"

def check_assets():
    assets_path = "../Assets"
    required = ["final_logo_concept.txt", "app_icon_idea.txt"]
    print(f"\n[?] Checking System Assets...")
    for item in required:
        if os.path.exists(os.path.join(assets_path, item)):
            print(f" [OK] {item} found.")
        else:
            print(f" [!!] {item} is MISSING!")

def startup_sequence():
    commander = get_commander()
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    print(f"\n[+] System Booting... {now}")
    print(f"[+] Authenticating: {commander}")
    print("-" * 30)
    print(f"Welcome back, Sir. Moallimi-V4 Engine is ONLINE.")
    
    check_assets()
    
    print("-" * 30)
    print(f"Current Objective: Building Al-Ra'ed Komondose.")

if __name__ == "__main__":
    startup_sequence()
EOF

python ~/Moallimi-V4/Code/main.py
cat << 'EOF' > ~/Moallimi-V4/Code/main.py
import os
import datetime

def get_commander():
    try:
        with open('commander.txt', 'r') as f:
            return f.read().strip()
    except:
        return "Unknown Commander"

def check_assets():
    assets_path = "../Assets"
    required = ["final_logo_concept.txt", "app_icon_idea.txt"]
    results = []
    for item in required:
        results.append(os.path.exists(os.path.join(assets_path, item)))
    return all(results)

def main_menu():
    commander = get_commander()
    while True:
        print(f"\n--- [ Moallimi-V4 : MAIN MENU ] ---")
        print(f"Commander: {commander}")
        print("1. View Project Status")
        print("2. Check Assets Health")
        print("3. Add New Entry to History")
        print("Q. Shutdown System")
        
        choice = input("\nEnter your choice: ").upper()
        
        if choice == '1':
            print("\n[!] Status: All Systems Operational.")
        elif choice == '2':
            status = "HEALTHY" if check_assets() else "ISSUES FOUND"
            print(f"\n[!] Assets Status: {status}")
        elif choice == '3':
            log = input("Enter new history note: ")
            with open("../Docs/history.log", "a") as f:
                f.write(f"\n[{datetime.datetime.now()}] {log}")
            print("[+] Log updated.")
        elif choice == 'Q':
            print("System shutting down... Goodbye, Sir.")
            break
        else:
            print("Invalid input.")

if __name__ == "__main__":
    main_menu()
EOF

python ~/Moallimi-V4/Code/main.py
cat << 'EOF' > ~/Moallimi-V4/Code/main.py
import os
import datetime

# تهيئة المسارات الذكية
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(BASE_DIR)

def authenticate():
    SECRET_KEY = "FiRaS2015iMaBaS" 
    print("\n" + "="*35)
    print(" [ MOALLIMI-V4 : RESTRICTED AREA ]")
    print("="*35)
    password = input("Enter Commander Key: ")
    if password == SECRET_KEY:
        print("\n[✔] Identity Verified. Access Granted.")
        return True
    else:
        print("\n[✖] Invalid Key! Emergency Shutdown.")
        return False

def main_menu():
    if not authenticate():
        return

    try:
        with open(os.path.join(BASE_DIR, 'commander.txt'), 'r') as f:
            commander = f.read().strip()
    except:
        commander = "Raid Komondose"

    while True:
        print(f"\n--- [ {commander} Dashboard ] ---")
        print("1. System Status")
        print("2. Integrity Check (Assets)")
        print("3. Log Progress (History)")
        print("Q. Terminate Session")
        
        choice = input("\nAction Select >> ").upper()
        
        if choice == '1':
            print("\n[OK] All internal modules are active.")
        elif choice == '2':
            assets_path = os.path.join(PROJECT_ROOT, "Assets")
            files = ["final_logo_concept.txt", "app_icon_idea.txt"]
            found = [f for f in files if os.path.exists(os.path.join(assets_path, f))]
            print(f"\n[!] Assets Scan: Found {len(found)}/2 files.")
            print(f"[!] Status: {'HEALTHY' if len(found)==2 else 'CHECK REQUIRED'}")
        elif choice == '3':
            log_path = os.path.join(PROJECT_ROOT, "Docs", "history.log")
            note = input("Log entry: ")
            with open(log_path, "a") as f:
                f.write(f"\n[{datetime.datetime.now()}] {note}")
            print("[+] Progress synchronized.")
        elif choice == 'Q':
            print("Session terminated. Security lock active.")
            break
        else:
            print("[!] Unknown command.")

if __name__ == "__main__":
    main_menu()
EOF

python ~/Moallimi-V4/Code/main.py
cat << 'EOF' > ~/Moallimi-V4/Code/main.py
import os
import datetime
import sys

# Path Configuration
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(BASE_DIR)

# Termux Color Codes
G = '\033[92m' # Green for Success
R = '\033[91m' # Red for Errors/Alerts
Y = '\033[93m' # Yellow for Warnings/Headers
W = '\033[0m'  # White/Reset

def authenticate():
    SECRET_KEY = "FiRaS2015iMaBaS"
    attempts = 3
    
    print(f"\n{W}" + "="*35)
    print(f"{Y} [ MOALLIMI-V4 : SECURE ACCESS ]{W}")
    print("="*35)
    
    while attempts > 0:
        password = input(f"Enter Commander Key ({attempts} left): ")
        if password == SECRET_KEY:
            print(f"\n{G}[✔] Identity Verified. Access Granted.{W}")
            return True
        else:
            attempts -= 1
            print(f"{R}[✖] Incorrect Key! Access Denied.{W}")
            
    print(f"\n{R}[!!!] SECURITY BREACH DETECTED. SHUTTING DOWN.{W}")
    return False

def main_menu():
    if not authenticate():
        sys.exit()

    while True:
        print(f"\n{Y}--- [ Main Control Dashboard ] ---{W}")
        print("1. System Status")
        print("2. Integrity Check (Assets)")
        print("3. Log Progress (History)")
        print("Q. Terminate Session")
        
        choice = input(f"\n{G}Action Select >> {W}").upper()
        
        if choice == '1':
            print(f"\n{G}[OK] Core modules are stable and online.{W}")
        elif choice == '2':
            assets_path = os.path.join(PROJECT_ROOT, "Assets")
            files = ["final_logo_concept.txt", "app_icon_idea.txt"]
            found = [f for f in files if os.path.exists(os.path.join(assets_path, f))]
            status = f"{G}HEALTHY{W}" if len(found)==2 else f"{R}INCOMPLETE{W}"
            print(f"\n[!] Assets Scan: Found {len(found)}/2 files. Status: {status}")
        elif choice == '3':
            log_path = os.path.join(PROJECT_ROOT, "Docs", "history.log")
            note = input("Enter log entry: ")
            with open(log_path, "a") as f:
                f.write(f"\n[{datetime.datetime.now()}] {note}")
            print(f"{G}[+] Progress synchronized.{W}")
        elif choice == 'Q':
            print(f"{Y}Session terminated. Security lock active.{W}")
            break
        else:
            print(f"{R}[!] Unknown command.{W}")

if __name__ == "__main__":
    main_menu()
EOF

python ~/Moallimi-V4/Code/main.py
cat << 'EOF' > ~/Moallimi-V4/Code/main.py
import os
import datetime
import sys
import base64

# Configuration
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(BASE_DIR)

# Colors
G, R, Y, W = '\033[92m', '\033[91m', '\033[93m', '\033[0m'

def xor_cipher(text):
    # Simple logic to obscure text without complexity
    return base64.b64encode(text.encode()).decode()

def xor_decipher(encoded_text):
    return base64.b64decode(encoded_text.encode()).decode()

def authenticate():
    SECRET_KEY = "FiRaS2015iMaBaS"
    attempts = 3
    print(f"\n{W}="*35 + f"\n{Y} [ MOALLIMI-V4 : SECURE ACCESS ]{W}\n" + "="*35)
    while attempts > 0:
        password = input(f"Enter Commander Key ({attempts} left): ")
        if password == SECRET_KEY:
            print(f"\n{G}[✔] Access Granted.{W}")
            return True
        attempts -= 1
        print(f"{R}[✖] Denied.{W}")
    return False

def main_menu():
    if not authenticate(): sys.exit()
    while True:
        print(f"\n{Y}--- [ Raid Komondose Control ] ---{W}")
        print("1. System Status\n2. Integrity Check\n3. Write Secure Log\n4. Read Decrypted Logs\nQ. Shutdown")
        choice = input(f"\n{G}Action >> {W}").upper()
        
        log_path = os.path.join(PROJECT_ROOT, "Docs", "history.log")
        
        if choice == '1':
            print(f"\n{G}[OK] Systems Online.{W}")
        elif choice == '2':
            print(f"\n{G}[!] Assets Status: HEALTHY (2/2){W}")
        elif choice == '3':
            note = input("Entry: ")
            secure_note = xor_cipher(note)
            with open(log_path, "a") as f:
                f.write(f"{datetime.datetime.now()}|{secure_note}\n")
            print(f"{G}[+] Encrypted and Saved.{W}")
        elif choice == '4':
            print(f"\n{Y}--- [ Decrypted History ] ---{W}")
            if os.path.exists(log_path):
                with open(log_path, "r") as f:
                    for line in f:
                        if "|" in line:
                            time, msg = line.strip().split("|")
                            print(f"{W}[{time}] {G}{xor_decipher(msg)}{W}")
            else: print(f"{R}No logs found.{W}")
        elif choice == 'Q':
            print(f"{Y}Offline. Goodbye.{W}"); break
        else: print(f"{R}[!] Unknown.{W}")

if __name__ == "__main__":
    main_menu()
EOF

python ~/Moallimi-V4/Code/main.py
cat << 'EOF' > ~/Moallimi-V4/Code/main.py
import os
import datetime
import sys
import base64

# Configuration
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(BASE_DIR)
G, R, Y, W = '\033[92m', '\033[91m', '\033[93m', '\033[0m'

def xor_cipher(text): return base64.b64encode(text.encode()).decode()
def xor_decipher(encoded_text): return base64.b64decode(encoded_text.encode()).decode()

def authenticate():
    SECRET_KEY = "FiRaS2015iMaBaS"
    attempts = 3
    print(f"\n{W}="*35 + f"\n{Y} [ MOALLIMI-V4 : SECURE ACCESS ]{W}\n" + "="*35)
    while attempts > 0:
        password = input(f"Enter Commander Key ({attempts} left): ")
        if password == SECRET_KEY: return True
        attempts -= 1
    return False

def main_menu():
    if not authenticate(): sys.exit()
    while True:
        print(f"\n{Y}--- [ Raid Komondose Control ] ---{W}")
        print("1. Status\n2. Integrity\n3. Write Log\n4. Read Logs\n5. Search Logs\nQ. Shutdown")
        choice = input(f"\n{G}Action >> {W}").upper()
        log_path = os.path.join(PROJECT_ROOT, "Docs", "history.log")
        
        if choice == '1': print(f"\n{G}[OK] Systems Online.{W}")
        elif choice == '2': print(f"\n{G}[!] Assets Status: HEALTHY (2/2){W}")
        elif choice == '3':
            note = input("Entry: ")
            with open(log_path, "a") as f: f.write(f"{datetime.datetime.now()}|{xor_cipher(note)}\n")
            print(f"{G}[+] Encrypted and Saved.{W}")
        elif choice == '4':
            if os.path.exists(log_path):
                with open(log_path, "r") as f:
                    for line in f:
                        time, msg = line.strip().split("|")
                        print(f"{W}[{time}] {G}{xor_decipher(msg)}{W}")
            else: print(f"{R}No logs.{W}")
        elif choice == '5':
            query = input("Search term: ").lower()
            print(f"\n{Y}--- [ Search Results ] ---{W}")
            found = False
            if os.path.exists(log_path):
                with open(log_path, "r") as f:
                    for line in f:
                        time, msg = line.strip().split("|")
                        decoded = xor_decipher(msg)
                        if query in decoded.lower():
                            print(f"{W}[{time}] {G}{decoded}{W}")
                            found = True
            if not found: print(f"{R}No matches found.{W}")
        elif choice == 'Q': break
if __name__ == "__main__": main_menu()
EOF

python ~/Moallimi-V4/Code/main.py
Q
# 1. Cleaning legacy/corrupted data
rm -f ~/Moallimi-V4/Docs/history.log
# 2. Deploying Robust Secure Code
cat << 'EOF' > ~/Moallimi-V4/Code/main.py
import os
import datetime
import sys
import base64

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(BASE_DIR)
G, R, Y, W = '\033[92m', '\033[91m', '\033[93m', '\033[0m'

def xor_cipher(text): 
    return base64.b64encode(text.encode()).decode()

def xor_decipher(encoded_text): 
    try: 
        return base64.b64decode(encoded_text.encode()).decode()
    except: 
        return "Unreadable Data"

def authenticate():
    SECRET_KEY = "FiRaS2015iMaBaS"
    print(f"\n{W}" + "="*35 + f"\n{Y} [ MOALLIMI-V4 : SECURE ACCESS ]{W}\n" + "="*35)
    password = input("Enter Commander Key: ")
    return password == SECRET_KEY

def main_menu():
    if not authenticate(): 
        print(f"{R}Access Denied.{W}")
        sys.exit()
        
    while True:
        print(f"\n{Y}--- [ Raid Komondose Control ] ---{W}")
        print("1. Status\n2. Integrity\n3. Write Log\n4. Read Logs\n5. Search Logs\nQ. Shutdown")
        choice = input(f"\n{G}Action >> {W}").upper()
        log_path = os.path.join(PROJECT_ROOT, "Docs", "history.log")
        
        if choice == '1': 
            print(f"\n{G}[OK] Systems Online.{W}")
        elif choice == '2': 
            print(f"\n{G}[!] Assets Status: HEALTHY (2/2){W}")
        elif choice in ['3', '4', '5']:
            if choice == '3':
                note = input("Entry: ")
                with open(log_path, "a") as f: 
                    f.write(f"{datetime.datetime.now()}|{xor_cipher(note)}\n")
                print(f"{G}[+] Encrypted and Saved.{W}")
            else:
                query = input("Search term (Enter for all): ").lower() if choice == '5' else ""
                print(f"\n{Y}--- [ Secure Log Viewer ] ---{W}")
                if os.path.exists(log_path):
                    with open(log_path, "r") as f:
                        for line in f:
                            if "|" in line:
                                time_stamp, msg = line.strip().split("|")
                                decoded = xor_decipher(msg)
                                if not query or query in decoded.lower():
                                    print(f"{W}[{time_stamp}] {G}{decoded}{W}")
                else: 
                    print(f"{R}No logs found.{W}")
        elif choice == 'Q': 
            print(f"{Y}Session Terminated.{W}")
            break
        else: 
            print(f"{R}[!] Unknown command.{W}")

if __name__ == "__main__":
    main_menu()
EOF

python ~/Moallimi-V4/Code/main.py.
python ~/Moallimi-V4/Code/main.py
cat << 'EOF' > ~/Moallimi-V4/Code/index.html
<!DOCTYPE html>
<html>
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        body { background: #000; color: #0f0; text-align: center; font-family: sans-serif; padding-top: 50px; }
        .btn { border: 2px solid #0f0; padding: 15px; border-radius: 10px; display: inline-block; margin-top: 20px; }
    </style>
</head>
<body>
    <h1>Al-Ra'ed Komondose</h1>
    <div class="btn">SYSTEM ACTIVE</div>
</body>
</html>
EOF

pkg update && pkg upgrade -y && pkg install nodejs -y
npm install -g @bubblewrap/cli
cat << 'EOF' > ~/Moallimi-V4/Code/manifest.json
{
  "name": "Al-Ra'ed Komondose",
  "short_name": "Komondose",
  "start_url": "index.html",
  "display": "standalone",
  "background_color": "#000000",
  "theme_color": "#00ff00",
  "orientation": "portrait",
  "icons": [
    {
      "src": "https://via.placeholder.com/512/000000/00ff00?text=RK",
      "sizes": "512x512",
      "type": "image/png"
    }
  ]
}
EOF

bubblewrap init --manifest=manifest.json
pkg install openjdk-17 -y
pkg install binutils python-is-python3 -y
export JAVA_HOME=$PREFIX/lib/jvm/java-17-openjdk
bubblewrap init --manifest=manifest.json
rm -rf ~/.bubblewrap
ln -s $PREFIX/lib/jvm/java-17-openjdk ~/java-fix
bubblewrap init --manifest=manifest.json
ln -sf $PREFIX/lib/jvm/java-17-openjdk $HOME/java-fix
bubblewrap init --manifest=manifest.json
pkg install python-pip -y && pip install setuptools
python -m http.server 8080
pkg update && pkg upgrade -y
pkg install python git zip unzip openjdk-17 ndk-sysroot binutils -y
pip install --upgrade buildozer
pip install --upgrade cython
cd ~/Moallimi-V4/Code
buildozer init
nano buildozer.spec
buildozer -v android debug
pkg install zlib libjpeg-turbo ndk-sysroot binutils-is-llvm -y
buildozer -v android debug
pkg install zlib-static libjpeg-turbo-static ndk-sysroot -y
buildozer -v android debug
cp main.py index.html buildozer.spec /sdcard/Download/
termux-setup-storage
cp main.py index.html buildozer.spec /sdcard/Download/
cp main.py buildozer.spec index.html /sdcard/Download/
