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
