import subprocess
import datetime

servers = ["google.com", "github.com", "cloudflare.com", "nickvendetti.dev", "fakeserver12345.com"]

def server_status(server):
  time = datetime.datetime.today()
  result = subprocess.run(
    ["ping", "-c", "1", server],
    stdout=subprocess.DEVNULL,
    stderr=subprocess.DEVNULL
  )
  if result.returncode == 0:
      with open("ServerStatus.txt", "a") as f:
        f.write(str(time) + " - " + server + " Is Online" + "\n")
  else: 
      with open("ServerStatus.txt", "a") as f:
        f.write(str(time) + " - " + server + " Is Offline" + "\n")

for server in servers:
  server_status(server)
