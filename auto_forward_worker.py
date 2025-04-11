import asyncio
import json
import time
from pyrogram import Client

# Load akun dan jadwal
with open("data/accounts.json") as f:
    accounts = json.load(f)

with open("data/schedules.json") as f:
    schedules = json.load(f)

# Worker untuk setiap akun
async def forward_worker(account):
    session_name = f"sessions/{account['phone']}"
    app = Client(session_name, api_id=21568771, api_hash="67c02cbc7ba43b88a717fc3019cf3771")
    await app.start()
    print(f"[{account['phone']}] started")

    while True:
        for job in [j for j in schedules if j['phone'] == account['phone']]:
            try:
                source = job['source'] if 'source' in job else "me"
                target = job['target']
                interval = job['interval']

                # Ambil chat terakhir dari source
                async for msg in app.get_chat_history(source, limit=1):
                    await app.forward_messages(chat_id=target, from_chat_id=source, message_ids=msg.message_id)
                    print(f"[{account['phone']}] Forwarded from {source} to {target}: {msg.message_id}")
                    break

                await asyncio.sleep(interval * 60)
            except Exception as e:
                print(f"[{account['phone']}] Error: {e}")
                await asyncio.sleep(10)

# Main entry
async def main():
    tasks = []
    for acc in accounts:
        tasks.append(asyncio.create_task(forward_worker(acc)))
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())