import json
import asyncio
from telethon.sync import TelegramClient
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.tl.functions.messages import ImportChatInviteRequest

with open("accounts.json", "r") as f:
    accounts = json.load(f)

targets = [
    "nama_channel_or_grup",                     # Username publik
    "https://t.me/joinchat/XXXXXXXXXXX"         # Invite link privat
]

async def join_with_account(account):
    client = TelegramClient(f"sessions/{account['session']}", account["api_id"], account["api_hash"])

    async with client:
        if not await client.is_user_authorized():
            print(f"[{account['session']}] Belum login.")
            return

        for target in targets:
            try:
                if "joinchat/" in target or "t.me/+" in target:
                    invite_hash = target.split("/")[-1].replace("+", "")
                    await client(ImportChatInviteRequest(invite_hash))
                else:
                    await client(JoinChannelRequest(target))
                print(f"[{account['session']}] ✅ Join: {target}")
            except Exception as e:
                print(f"[{account['session']}] ❌ Gagal join {target}: {e}")

async def main():
    tasks = [join_with_account(acc) for acc in accounts]
    await asyncio.gather(*tasks)

asyncio.run(main())
