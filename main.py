from selenium import webdriver
from selenium.webdriver.common.by import By
import pywhatkit
from datetime import datetime

driver = webdriver.Chrome()
driver.get("https://store.epicgames.com/en-US/free-games")

ele = driver.find_elements(By.CLASS_NAME,"css-17st2kc")
data_list = [i.text for i in ele]
driver.quit()

data_dict_list = [] 
for item in data_list: 
    parts = item.split('\n') 
    if len(parts) == 3: 
        data_dict = { 
            "status": parts[0], 
            "game": parts[1], 
            "availability": parts[2] } 
    elif len(parts) == 2: 
        data_dict = { 
            "status": parts[0], 
            "game": parts[1].split(' in ')[0], 
            "time_left": parts[1].split(' in ')[1] } 
    data_dict_list.append(data_dict)

message = ""
for game in data_dict_list:
    if game["status"] == "FREE NOW":
        message += f"Free game available: {game['game']}"
    if "time_left" in game:
        message += f"\nTime left for next free game: {game['time_left']}"


print(message)
hour = datetime.now().hour
min = datetime.now().minute + 1
# Need to input your phone number
pywhatkit.sendwhatmsg('{Your phone number}', message, hour, min,tab_close=True)
 
