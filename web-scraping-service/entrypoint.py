import requests

SERVICE1_URL = "http://hashing-service:8080/"
WEB_PAGE_URL = "https://www.google.com/"

# message = requests.get(sys.stdin.readline()).text
# the line above reads the string from the keyboard and not from a website as per the instructions
# so I've changed it to read from a website instead and send that to the other service for hashing

try:
    response = requests.get(WEB_PAGE_URL)
    web_page_content = response.text
    
    message = web_page_content
    data = ["md5", message]

    response = requests.post(SERVICE1_URL, data="\n".join(data))

    print(response.text.strip())

# added error handling which we need in case the website is unavailable or we don't have internet
except requests.exceptions.RequestException as e:
    print("Error: {}".format(e))
