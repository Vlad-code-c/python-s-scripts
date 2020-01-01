import os
import random
import ctypes

wallpaper_path = "E:/Desktop/Wallpapers"
wallpapers = []

with os.scandir(wallpaper_path) as entries:
    for entry in entries:
        if entry.is_file():
            wallpapers.append(entry.name)

rand = wallpaper_path + "\\" + random.choice(wallpapers)
print(rand)

ctypes.windll.user32.SystemParametersInfoW(20, 0, rand , 0)
