import os

with open("conf.v", "r") as con:
    wallpaper = con.read()
try:
    os.remove(wallpaper)
except:
    pass
exec('Change.bat')