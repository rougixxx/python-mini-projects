# Web:
Doing Some Python mini-projects related to Web.
## Requirements
```bash
python3 -m pip install requests
```
```bash
python3 -m pip install bs4
```
## Descreption:
- **Web-Pentest-tools**:
  - ```dirs&files Discovery```: discover directories and files of a domain using a wordlist
  
  ```bash
  python3 discover.py
  ```
  - ```sub-domain Detector```: detect sub-domains of a domain using requests module
  ```bash
  python detect.py
  ```
  - ```robots-reader```: gettings robots.txt content from a domain
  ```bash
  python robots_reader.py
  ```
  - ```xss-scanner```: a simple xss checking tool using requests module
  ```bash
  python xss_scanner.py
  ```
- **Web-scrapping**:
  - ```soq-dz/scrapper```: scrapping products names and prices from [soq-dz](https://www.soq-dz.com/) and store it in a csv format.
    ```bash
    python3 soq-dz/scrapper.py
    ```
- **Web-server**: creating a web server using python with 2 differenet methods
  1. first method: using http package with BaseHTTPRequestHandler, HTTPServer methods
      ```bash
      python3 web.py
      ```
  2. second method: using sockets and http packages
     ```bash
     python3 server.py
     ```
