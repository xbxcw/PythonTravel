from selenium import webdriver
from time import sleep
import os
URL = r'http://tool.chinaz.com/dns/?type=1&host=github.com&ip='
HOSTS = r"C:\Windows\System32\drivers\etc\hosts"
chrome_opts = webdriver.ChromeOptions()
chrome_opts.add_argument("--headless")

browser = webdriver.Chrome(chrome_options=chrome_opts)
browser.get(URL)
while True:
    try:
        info = browser.find_element_by_xpath('/html/body/div[2]/div[2]/ul/li[11]/div[2]/p').text.split(' ', 1)
        if info:
            break
    except:
        print('---')
    sleep(1)
    
browser.quit()

data = info[0]+' '+'github.com # hyc'

with open(HOSTS,'r',encoding='utf8') as f:
    lines = f.readlines()


with open(HOSTS,'w',encoding='utf8')as f_w:
    for line in lines:
        if 'github.com # hyc' in line:
            continue
        f_w.write(line)
    f_w.write(data)

os.system('ipconfig /flushdns')