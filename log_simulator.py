import random
import time
from datetime import datetime

# Normal log users/actions
users = ["rohan", "soham", "admin", "guest"]
actions = ["login", "logout", "failed login", "access file", "unauthorized access", "suspicious activity"]
ips = ["192.168.1.1", "10.0.0.2", "172.16.0.3"]

# Apache log paths, methods, and status codes
paths = ["/", "/admin", "/login", "/dashboard", "/.env", "/backup.zip", "/robots.txt"]
methods = ["GET", "POST"]
status_codes = [200, 403, 404, 500]

def generate_normal_log():
    user = random.choice(users)
    action = random.choice(actions)
    ip = random.choice(ips)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return "%s - User: %s - IP: %s - Action: %s" % (timestamp, user, ip, action)

def generate_apache_log():
    ip = random.choice(ips)
    dt = datetime.now().strftime("%d/%b/%Y:%H:%M:%S")
    method = random.choice(methods)
    path = random.choice(paths)
    status = random.choice(status_codes)
    return '%s - - [%s] "%s %s HTTP/1.1" %s' % (ip, dt, method, path, status)

# Create logs.txt
with open("logs.txt", "w") as file:
    for i in range(100):
        if random.random() < 0.5:
            file.write(generate_normal_log() + "\n")
        else:
            file.write(generate_apache_log() + "\n")
        time.sleep(0.01)

print("✅ logs.txt created with mixed normal and Apache logs.")
