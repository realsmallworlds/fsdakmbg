import json
import os
import shutil
import subprocess
import time
from typing import List, Tuple

import countryflag
import pandas as pd
import requests
import streamlit as st
from lxml import etree, html
import time
import re
import random
import string
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import subprocess

with st.echo():
    def get_chromedriver_path() -> str:
        return shutil.which('chromedriver')

    service = Service(
            executable_path=get_chromedriver_path()        )
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-features=NetworkService")
    options.add_argument("--window-size=1920x1080")
    options.add_argument("--disable-features=VizDisplayCompositor")
    options.add_argument('--ignore-certificate-errors')
    i = 0
    j = 0
    while i < 1:
        driver = webdriver.Chrome(options=options, service=service)
        driver.get("https://myco.io/")
        wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/nav/div/div[3]/button'))).click()
        wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div[1]/div/div[2]/span'))).click()
        wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="firstName"]'))).send_keys(name)
        wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="lastName"]'))).send_keys(name_2)
        wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="email"]'))).send_keys(email.address)
        wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="userName"]'))).send_keys(name)
        wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="password"]'))).send_keys("zxcasdqwe12!A")
        wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="confirmPassword"]'))).send_keys("zxcasdqwe12!A")
        wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="link-checkbox"]'))).click()
        wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="register-btn"]'))).click()
        time.sleep(5)
        msg = email.wait_for_message()
        myCode = msg.body
        link = (re.findall(r'(https?://auth.myco.io?.*\?.*?)\s', myCode))[0]
        link2 = extractor.find_urls(link)[0]
        driver.get(link2)
        #time.sleep(8)
        driver.get("https://myco.io/")
        wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/nav/div/div[3]/button'))).click()
        wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="root"]/div[1]/div/form/div[2]/div[2]/input'))).send_keys(name)
        wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div[1]/div/form/div[2]/div[3]/input'))).send_keys("zxcasdqwe12!A")
        wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="root"]/div[1]/div/form/div[2]/div[4]/button'))).click()
        time.sleep(8)
        driver.get("https://myco.io/videohome?v=64e459e5a9addef12597ac3a")
        wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[2]/div/div/div[1]/div/div[1]/div/video-js/button'))).click()
        j += 1
        if j == 5:
            time.sleep(3700)
            j = 0
            subprocess.run("pkill chromium", shell=True)            

