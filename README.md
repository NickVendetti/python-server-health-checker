# python-server-health-checker

Checks status of server, returns health check and timestamp for accurate record keeping. This program was built while preparing for an automation engineering role.

## Technology Used
- Python 3
-s ubprocess module
- datetime module

## How it works
- Imports needed modules
- Initializes the list of servers
- Defines a function that pings each server
- Removes unneeded output data
- Checks return code to determine online or offline status
- Appends timestamped results to a log file

## How to run
  ```bash
python3 server_health_checker.py
```
## Sample Output
-2026-05-20 01:59:20.675072 - google.com Is Online
-2026-05-20 01:59:20.711791 - github.com Is Online
-2026-05-20 01:59:20.753717 - cloudflare.com Is Online
-2026-05-20 01:59:20.783579 - nickvendetti.dev Is Online
-2026-05-20 01:59:20.896776 - fakeserver12345.com Is Offline

## Future Improvements
- Add HTTP checks instead of ping
- Email alerts when a server goes offline
- Support for reading server list from a config file
    
