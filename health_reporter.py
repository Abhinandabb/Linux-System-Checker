import psutil
import requests
import json
from datetime import datetime
import os

THRESHOLD = 80

def check_system_health():

    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    cpu_usage = psutil.cpu_percent(interval=1)

    memory_info = psutil.virtual_memory()
    memory_usage = memory_info.percent

    disk_info = psutil.disk_usage('/')
    disk_usage = disk_info.percent

    report = f"[{now}] CPU: {cpu_usage}% | RAM: {memory_usage}% | Disk: {disk_usage}%"
    print(report)

    if cpu_usage > THRESHOLD or memory_usage > THRESHOLD or disk_usage > THRESHOLD:
        send_alert(report)

def send_alert(message):
    #Paste your Discord Webhook URL
    webhook_url = "https://discord.com/api/webhooks/1460270340440850596/ANmcQgargW8c8TBMN0nGl3nmlh1MxGFJdspYvD7_1NKYzPvj2si9oCU0gzKZesY5zBFO"

    if not webhook_url:
         raise ValueError("DISCORD_WEBHOOK_URL environment variable not set")
    payload = {"content" :f" SYSTEM ALERT!\n{message}"}

    try:
        response = requests.post(
            webhook_url, 
            data=json.dumps(payload), 
            headers={'Content-Type': 'application/json'}
        )
        if response.status_code == 204:
            print("Alert send successfully.")
    except Exception as e:
        print(f"Failed to send alert: {e}")

if __name__ == "__main__":
    check_system_health()
