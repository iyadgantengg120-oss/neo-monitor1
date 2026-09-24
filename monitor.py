import psutil
import time
import requests
from datetime import datetime

BOT_TOKEN = "ISI_TOKEN_BOT_TELEGRAM_LU"
CHAT_ID = "ISI_CHAT_ID_LU"

def send_alert(msg):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    requests.post(url, data={"chat_id": CHAT_ID, "text": msg})

print("NEO-MONITOR1 AKTIF...")

while True:
    cpu = psutil.cpu_percent()
    ram = psutil.virtual_memory().percent
    print(f"[{datetime.now()}] CPU: {cpu}% | RAM: {ram}%")
    if cpu > 90 or ram > 90:
        send_alert(f"SERVER OVERLOAD! CPU:{cpu}% RAM:{ram}%")
    time.sleep(60)
