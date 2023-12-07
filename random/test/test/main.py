from selenium import webdriver
import os


drive = webdriver.Chrome(service_log_path=os.devnull)
drive.set_window_position(0, 0)

os.system('cls')