import os

with open("Wallpaper_Control/conf.v", "r") as con:
    wallpaper = con.read()
try:
    os.remove(wallpaper)
except:
    pass