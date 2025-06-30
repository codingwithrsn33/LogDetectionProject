import random
from datetime import datetime, timedelta

users = ["rohan", "soham", "guest", "admin", "testuser"]
ips = ["10.0.0.2", "172.16.0.3", "192.168.1.1", "192.168.0.5", "10.0.1.3"]
actions = [
    "successful login",
    "failed login for user",
    "GET /admin HTTP/1.1",
    "GET /home HTTP/1.1",
    "unauthorized access",
    "suspicious activity",
    "GET /.env HTTP/1.1",
    "GET /backup.zip HTTP/1.1"
]

start_time = datetime(2025, 6, 25, 16, 0, 0)

with open("logs.txt", "w") as f:
    for i in range(50000):
        timestamp = start_time + timedelta(seconds=i * random.randint(1, 3))
        user = random.choice(users)
        ip = random.choice(ips)
        action = random.choice(actions)
        line = f"{timestamp.strftime('%Y-%m-%d %H:%M:%S')} - User: {user} - IP: {ip} - Action: {action}"
        f.write(line + "\n")

print("✅ logs.txt with 50,000 entries generated!")
