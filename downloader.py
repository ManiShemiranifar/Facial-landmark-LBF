import urllib.request as urlreq
import os

haarcascade_URL = "https://raw.githubusercontent.com/opencv/opencv/master/data/haarcascades/haarcascade_frontalface_alt2.xml"
haarcascade = "haarcascade_frontalface_alt2.xml"


def download_haarcascade():
    if haarcascade not in os.listdir(os.curdir):
        try:
            print("Downloading ...")
            urlreq.urlretrieve(haarcascade_URL, haarcascade)
            print("Download complete :)")
        except:
            print("Download failed :(, please try again")


    else:
        print("You already have haarcascade file")


def haarcascade_path():
    return haarcascade
