from selenium import webdriver
import time
from bs4 import BeautifulSoup
import requests
from urllib.request import urlopen

### Dont forgrt to change the download directory under step 5



def downloadVideo(link, id):
# To make the code work, go to https://ssstik.io/en paste any link of a tiktok video (Dont click donload)
# Right click on the screen and select "inspect" and go to the network tab
# click the download button
# in the network tab right click on "abc?url=dl" copy and then copy as cURL(bash)
# go to curlconverter.com and past the cURL that was copied and convert it to python code
# Past the python code here
## This only has to be done once 



    print(f"Downloading video {id} from: {link}")
    cookies = {
    
       '__cflb': '02DiuEcwseaiqqyPC5reXswsgyrfhBQeoD3wFEjTw7vr7',
    '_ga': 'GA1.2.881723693.1680622848',
    '__gads': 'ID=165f83562d16ec01-225460254fdc0085:T=1680622848:RT=1680622848:S=ALNI_MYqVKkwu_LEXG3A2tDM08XeS182xw',
    '_gid': 'GA1.2.946762191.1681034888',
    '__gpi': 'UID=00000bfbcddd0267:T=1680622848:RT=1681034888:S=ALNI_MbJMsBtBiNqnXCwXMqVwd29x-XoeQ',
    '_gat_UA-3524196-6': '1',
}

    headers = {
    
    'authority': 'ssstik.io',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'cookie': '__cflb=02DiuEcwseaiqqyPC5reXswsgyrfhBQeoD3wFEjTw7vr7; _ga=GA1.2.881723693.1680622848; __gads=ID=165f83562d16ec01-225460254fdc0085:T=1680622848:RT=1680622848:S=ALNI_MYqVKkwu_LEXG3A2tDM08XeS182xw; _gid=GA1.2.946762191.1681034888; _gat_UA-3524196-6=1; __gpi=UID=00000bfbcddd0267:T=1680622848:RT=1681034888:S=ALNI_MbJMsBtBiNqnXCwXMqVwd29x-XoeQ',
    'hx-current-url': 'https://ssstik.io/en',
    'hx-request': 'true',
    'hx-target': 'target',
    'hx-trigger': '_gcaptcha_pt',
    'origin': 'https://ssstik.io',
    'referer': 'https://ssstik.io/en',
    'sec-ch-ua': '"Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
}

    params = {
        'url': 'dl',
    }

    data = {
        'id': link,
        'locale': 'en',
        'tt': 'dmp0TW0_', 
    }
    
    print("STEP 4: Getting the download link")
    print("If this step fails, PLEASE read the steps above")
    response = requests.post('https://ssstik.io/abc', params=params, cookies=cookies, headers=headers, data=data)
    downloadSoup = BeautifulSoup(response.text, "html.parser")

    downloadLink = downloadSoup.a["href"]
    videoTitle = downloadSoup.p.getText().strip()

    print("STEP 5: Saving the video :)")
    mp4File = urlopen(downloadLink)
    # change the download directory by replacing ****** eg -> D:/test1//vid{id}.mp4
    with open(f"******/vid{id}.mp4", "wb") as output:  
        while True:
            data = mp4File.read(4096)
            if data:
                output.write(data)
            else:
                break

print("STEP 1: Open Chrome browser")
username = input("Please type the tiktok username :")
driver = webdriver.Chrome()
# Change the tiktok link
driver.get(f"https://www.tiktok.com/@{username}") 

# IF YOU GET A TIKTOK CAPTCHA, CHANGE THE TIMEOUT HERE to 60 seconds, just enough time for you to complete the captcha yourself.
time.sleep(20)

scroll_pause_time = 1
screen_height = driver.execute_script("return window.screen.height;")
i = 1

print("STEP 2: Scrolling page")
while True:
    driver.execute_script("window.scrollTo(0, {screen_height}*{i});".format(screen_height=screen_height, i=i))  
    i += 1
    time.sleep(scroll_pause_time)
    scroll_height = driver.execute_script("return document.body.scrollHeight;")  
    if (screen_height) * i > scroll_height:
        break 

soup = BeautifulSoup(driver.page_source, "html.parser")

videos = soup.find_all("div", {"class": "tiktok-yz6ijl-DivWrapper"})

print(f"STEP 3: Time to download {len(videos)} videos")
for index, video in enumerate(videos):
    print(f"Downloading video: {index}")
    downloadVideo(video.a["href"], index)
    time.sleep(10)