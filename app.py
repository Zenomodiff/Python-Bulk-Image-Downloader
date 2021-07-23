import urllib.request

from random import *

num = int(input("Number of images (Integer): "))
for i in range(num):
    url = "https://random.imagecdn.app/1920/1080"
    filename = "/Users/USER/Desktop/Wallpapers/image{}.png".format(i)
    urllib.request.urlretrieve(url, filename)