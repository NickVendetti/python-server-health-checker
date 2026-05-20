# python-server-health-checker

Checks status of server, returns health check and timestamp for accurate record keeping

This program was built while preparing for an automation engineering role.

Technology Used:
         Python 3
         subprocess module
         datetime module

How it works;
    import needed modules
    initialize the array
    define function
    initialize time and result from ping
    pings each server in array, removed not needed data

  depending on return code from ping, Server Status is listed with log.
  record keeping log appends each loop to text file.

How to run:
  python3 server_health_checker.py

Sample Output:
  2026-05-20 01:59:20.675072 - google.com Is Online
  2026-05-20 01:59:20.711791 - github.com Is Online
  2026-05-20 01:59:20.753717 - cloudflare.com Is Online
  2026-05-20 01:59:20.783579 - nickvendetti.dev Is Online
  2026-05-20 01:59:20.896776 - fakeserver12345.com Is Offline

Future Improvements
  Add HTTP checks instead of ping
  Email alerts when a server goes offline
  Support for reading server list from a config file
    
