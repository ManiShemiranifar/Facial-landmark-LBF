import urllib.request as urlreq
import os

haarcascade_URL = "https://raw.githubusercontent.com/opencv/opencv/master/data/haarcascades/haarcascade_frontalface_alt2.xml"
haarcascade = "haarcascade_frontalface_alt2.xml"
lbfmodel_url = "https://github.com/kurnianggoro/GSOC2017/raw/master/data/lbfmodel.yaml"
lbfmodel = "lbfmodel.yaml"

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

def download_lbf():
    if lbfmodel not in os.listdir(os.curdir):
        try:
            print("Downloading ...")
            urlreq.urlretrieve(haarcascade_URL, haarcascade)
            print("Download complete :)")
        except:
            print("Download failed :(, please try again")


    else:
        print("You already have LBFmode file")
