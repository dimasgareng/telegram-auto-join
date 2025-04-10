import json
import os
import asyncio
from telethon.sync import TelegramClient

# Load akun-akun dari accounts.json
with open("accounts.json", "r") as f:
    accounts = json.load(f)

# Buat folder 'sessions' jika belum ada
if not os.path.exists("sessions"):
    os.makedirs("sessions")

# Fungsi login untuk satu akun
async def login_account(account):
    session_path = f"sessions/{account['session']}"
    client = TelegramClient(session_path, account['api_id'], account['api_hash'])

    async with client:
        print(f"\n=== Login untuk: {account['session']} ===")
        await client.start(phone=input(f"Masukkan nomor HP untuk [{account['session']}]: "))
        print(f"[{account['session']}] ✅ Login berhasil dan session disimpan.")
        await client.disconnect()

# Fungsi utama untuk login semua akun
async def main():
    for acc in accounts:
        try:
            await login_account(acc)
        except Exception as e:
            print(f"[{acc['session']}] ❌ Gagal login: {e}")

# Jalankan program
asyncio.run(main())
