#Importing the libraries
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import tkinter as ttk
from colorama import Fore, Back, Style
from selenium.webdriver.chrome.options import Options

#Starting timer 
start_time = time.time()
print(Fore.RED + str(start_time))


#Defining the path of the chrome driver and chrome path
path = "C:\chromedriver_win32\chromedriver.exe"
chrome_path = "C:\Program Files (x86)\Google\Chrome\Application"
window_size = "1920,1080"


#Setting the options for the chrome driver
chrome_options = Options()
chrome_options.add_argument("--headless")


#Input the fight id
print(Style.RESET_ALL)
fid = input("Enter the flight id: ")


#Starting the chrome driver
driver = webdriver.Chrome(executable_path=path, options=chrome_options)


#Getting the url
driver.get(f"https://flightaware.com/live/flight/{fid}")


#Getting the data by xpath 
from_loc = driver.find_element(By.XPATH, '//*[@id="flightPageTourStep1"]/div[1]/div[1]/span[2]').text
to_loc = driver.find_element(By.XPATH, '//*[@id="flightPageTourStep1"]/div[1]/div[2]/span[2]/span').text
ariving = driver.find_element(By.XPATH, '//*[@id="mainBody"]/div[1]/div[2]/div[3]/div[1]/div[1]/div[1]/div[2]/div[2]/div').text
time_elap = driver.find_element(By.XPATH, '//*[@id="flightPageTourStep1"]/div[4]/div[2]/span[1]/strong').text
distance_left = driver.find_element(By.XPATH, '//*[@id="flightPageTourStep1"]/div[4]/div[3]/span[2]/strong').text
altitude = driver.find_element(By.XPATH, '//*[@id="mainBody"]/div[1]/div[2]/div[4]/div[9]/div[3]/div/div/div[2]/div[2]').text
speed = driver.find_element(By.XPATH, '//*[@id="mainBody"]/div[1]/div[2]/div[4]/div[9]/div[3]/div/div/div[1]/div[2]').text
airline = driver.find_element(By.XPATH, '//*[@id="mainBody"]/div[1]/div[2]/div[4]/div[9]/div[2]/div/div/div[2]/span').text
aircraft_type = driver.find_element(By.XPATH, '//*[@id="mainBody"]/div[1]/div[2]/div[4]/div[9]/div[1]/div/div[1]/div[2]').text
speed = driver.find_element(By.XPATH, '//*[@id="mainBody"]/div[1]/div[2]/div[4]/div[9]/div[3]/div/div/div[1]/div[2]').text


#Printing the data in terminal 
print(Fore.GREEN + f"Flight id: {fid}")
print(Fore.GREEN + "From: " + from_loc)
print(Fore.GREEN + "To: " + to_loc)
print(Fore.GREEN + "Arriving: " + ariving)
print(Fore.GREEN + "Time elapsed: " + time_elap)
print(Fore.GREEN + "Distance left: " + distance_left)
print(Fore.GREEN + "Altitude: " + altitude)
print(Fore.GREEN + "Speed: " + speed)
print(Fore.GREEN + "Airline: " + airline)
print(Fore.GREEN + "Aircraft type: " + aircraft_type)


#Closing the chrome driver
driver.quit()


#Configuring the tkinter window
screen = ttk.Tk()
screen.title("Flight Details")
screen.geometry("500x500")


#Creating the labels
fid = ttk.Label(text=f"Flight id: {fid}")
from_locc = ttk.Label(text="From: " + from_loc)
to_locc = ttk.Label(text="To: " + to_loc)
ariving_ = ttk.Label(text="Arriving: " + ariving)
time_elap_ = ttk.Label(text="Time elapsed: " + time_elap)
distance_left_ = ttk.Label(text="Distance left: " + distance_left)
altitude_ = ttk.Label(text="Altitude: " + altitude)
speed__ = ttk.Label(text="Speed: " + speed)
airline_ = ttk.Label(text="Airline: " + airline)
airecraft_type_ = ttk.Label(text="Aircraft type: " + aircraft_type)


#Packing the labels
fid.pack()
from_locc.pack()
to_locc.pack()
ariving_.pack()
time_elap_.pack()
distance_left_.pack()
altitude_.pack()
speed__.pack()
airline_.pack()
airecraft_type_.pack()


#Running the tkinter window
screen.mainloop()


#Printing the execution time
print(Fore.RED + "Execution time: " + str(time.time() - start_time) + " seconds")
print(Style.RESET_ALL)