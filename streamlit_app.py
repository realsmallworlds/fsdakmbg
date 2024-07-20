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
    with webdriver.Chrome(options=options, service=service) as driver:
        driver.get("https://myco.io/")
        wait = WebDriverWait(driver, 30)
        wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/nav/div/div[3]/button'))).click()
        print("done")
