import os
import random
import ctypes
import datetime
 

dt_now = datetime.datetime.now()
local_hour = dt_now.hour


wallpaper_path = "E:/Desktop/Wallpapers/"
wallpapers = []
folder_paths = []

def random_directory():
    for entry_name in os.listdir(wallpaper_path):
        entry_path = os.path.join(wallpaper_path, entry_name)
        if os.path.isdir(entry_path):
            folder_paths.append(entry_path)
    return random.choice(folder_paths)



if local_hour > 22:
    wallpaper_path = "E:/Desktop/Wallpapers/nigth"
elif local_hour >= 6 and local_hour < 17:
    wallpaper_path = "E:/Desktop/Wallpapers/day"
elif local_hour >= 17 and local_hour <= 22:
    wallpaper_path = "E:/Desktop/Wallpapers/nothing"
else:
    wallpaper_path = random_directory



with os.scandir(wallpaper_path) as entries:
    for entry in entries:
        if entry.is_file():
            if not ".ini" in entry.name:
                wallpapers.append(entry.name)

rand = wallpaper_path + "\\" + random.choice(wallpapers)
ctypes.windll.user32.SystemParametersInfoW(20, 0, rand , 0)

with open("conf.v", "w") as con:
    con.write(rand)
