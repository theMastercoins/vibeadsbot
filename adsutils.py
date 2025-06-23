import requests
import time
import random
from colorama import init, Fore, Style
from textutils import *


# === Ad Automation Logic ===
def get_adextra_rtb(user_id):
    attempts = 0
    max_attempts = 3
    while attempts < max_attempts:
        url = f"https://partner.adextra.io/rtb?h=0&w=24.75&referrer=&user_id={user_id}&premium=0&fullscreen=0&device=desktop&platform=tdesktop&a=a6c64242065104ee70def8638b1f0038d3ec4ebd"
        loading_bar(f"Connecting to AdExtra RTB [Try {attempts + 1}]")
        try:
            r = requests.get(url, timeout=3)
            if r.status_code == 200:
                return r.json()
        except:
            pass
        attempts += 1
        time.sleep(0.5)
    return None

def extract_ad_info(rtb_response):
    try:
        bid = rtb_response["seatbid"][0]["bid"][0]
        adm = bid["adm"]
        impurl = bid["ext"]["impurl"][0]
        script_id = adm.split("script?id=")[1].split("'")[0]
        return script_id, impurl
    except:
        return None, None

def fetch_gigapub_ad(user_id, username, first_name):
    url = "https://bid-net.gigapub.tech/v1/get-ad"
    payload = {
        "user": {
            "platform": "tdesktop",
            "user": {
                "id": user_id,
                "first_name": first_name,
                "username": username,
                "language_code": "en",
                "allows_write_to_pm": True,
                "photo_url": "https://t.me/i/userpic/320/default.png",
                "version": "9.0"
            }
        }
    }
    loading_bar("Fetching ad from GigaPub")
    r = requests.post(url, json=payload)
    return r.json() if r.status_code == 200 else {}

def track_impression(impurl):
    loading_bar("Tracking ad impression")
    r = requests.get(impurl)
    return r.status_code == 200

def report_ad_error(user_id, username, first_name):
    url = "https://ad.gigapub.tech/v1/ad"
    payload = {
        "method": "adShowError",
        "args": {
            "user": {
                "platform": "tdesktop",
                "user": {
                    "id": user_id,
                    "first_name": first_name,
                    "username": username,
                    "language_code": "en",
                    "allows_write_to_pm": True,
                    "photo_url": "https://t.me/i/userpic/320/default.png",
                    "version": "9.0"
                }
            },
            "placementId": "main",
            "network": "b",
            "rotationType": "bid",
            "showCounter": 0
        }
    }
    type_writer(f"{Fore.RED}Reporting failed ad to GigaPub...")
    r = requests.post(url, json=payload)

def tgads_bid_request(user_id, username, first_name):
    url = "https://bid.tgads.live/bid-request"
    payload = {
        "wid": "6feb25e8-3596-4ad3-b61a-211b342f9f8d",
        "adFormat": "interstitial",
        "af": 0,
        "firstName": first_name,
        "lastName": "",
        "username": username,
        "telegramId": user_id,
        "platform": "tdesktop",
        "isPremium": False,
        "language": "en",
        "motivated": False,
        "tonConnected": False,
        "version": 1.42,
        "from": "window"
    }
    loading_bar("Checking TGAds")
    r = requests.post(url, json=payload)
    return r.json()


