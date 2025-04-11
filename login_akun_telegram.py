import os
from pyrogram import Client

api_id = 21568771
api_hash = "67c02cbc7ba43b88a717fc3019cf3771"

def main():
    phone = input("Masukkan nomor HP (dengan +62...): ").strip()
    session_dir = "sessions"
    os.makedirs(session_dir, exist_ok=True)
    session_name = os.path.join(session_dir, phone)

    app = Client(session_name, api_id=api_id, api_hash=api_hash)

    with app:
        print(f"Sukses login dan simpan sesi: {session_name}")

if __name__ == "__main__":
    main()