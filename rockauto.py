from bs4 import BeautifulSoup
import requests

def task():

    partn = input("Enter Part # to search in RockAuto: ")
    base_url = "https://www.rockauto.com/en/partsearch/?partnum="
    request_to_send = (f"{base_url}{partn}")
    req = requests.get(request_to_send)
    req_code = req.status_code
    
    
    if req_code == 200:
        print(f"Response code: {req_code}, good connection")
    else:
        print(f"Response code: {req_code}, connection failed!")



    soup = BeautifulSoup(req.text, features= "html.parser")
    try:
        price = soup.find('span', id=lambda x: x and x.startswith('dtotal')).text
    except:
        print("No price found")
    try:
        print(f"Cheapest price found in RockAuto is: {price}")
    except:
        pass
    
    x = input("Press 'c' to close, or 'enter to try another part number.")
    if x == "c":
        pass
    else:
        task()

task()