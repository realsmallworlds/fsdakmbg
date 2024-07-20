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
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait



with st.echo():
    service = get_webdriver_service(logpath=logpath)
    with webdriver.Chrome(service=service) as driver:
        driver.get("https://myco.io/")
        wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/nav/div/div[3]/button'))).click()
        print("done")
