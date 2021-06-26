import requests, subprocess, time, os
from bs4 import BeautifulSoup
import winreg as reg
from datetime import datetime
now = datetime.now()
session = requests.session()
session.proxies = {}
session.proxies['http'] = 'socks5h://localhost:9050'
session.proxies['https'] = 'socks5h://localhost:9050'
paste = ""
paste_name = ""
def uac(cmd):
    reg_uac = reg.CreateKey(reg.HKEY_CURRENT_USER, r'Software\\Classes\\ms-settings\\shell\\open\\command')
    reg_open_uac = reg.OpenKey(reg.HKEY_CURRENT_USER, r'Software\\Classes\\ms-settings\\shell\\open\\command', 0, reg.KEY_SET_VALUE)
    reg.SetValueEx(reg_open_uac, "DelegateExecute", 0,  reg.REG_SZ, "")
    reg.SetValueEx(reg_open_uac, "", 0, reg.REG_SZ, cmd)
    subprocess.Popen(['fodhelper'], shell=True)
    time.sleep(0.5)
    reg.DeleteKey(reg.HKEY_CURRENT_USER, r'Software\\Classes\\ms-settings\\shell\\open\\command')
def params():
    return (
        ('action', 'create_paste'),
    )
def paste_name():
    global paste_name
    paste_name = input("\nInput paste name here > ")
def paste():
    global paste
    paste = input("\nInput paste content here > ")
def data(ticket):
    return {
      'paste': paste,
      'paste_name': paste_name,
      'format': 'txt',
      'ticket': ticket
    }
def url():
    return 'http://torpastezr7464pevuvdjisbvaf4yqi4n7sgz7lkwgqwxznwy5duj4ad.onion/'
def rawdata():
    rawdata = session.get(url())
    return rawdata.content
def date_time():
    return now.strftime("%d-%m-%Y %H.%M.%S")
def file_creation(name, paste, link, token):
    with open(f"{name}.txt", "w") as f:
        f.write(f"Paste_name: {paste}\n\nLink: {link}\n\nEdit-Token: {token}")
paste_name()
paste()
uac('sc start tor')
soup = BeautifulSoup(rawdata(), 'html.parser')
ticket = soup.find('input', {'name': 'ticket'}).get('value')
r = session.post(url(), headers=None, params=params(), data=data(ticket))
soup = BeautifulSoup(r.text, 'html.parser')
link = soup.find('input', {'class': 'paste-created-link-input'}).get('value')
token = soup.find('input', {'class': 'paste-created-token-input'}).get('value')
file_creation(date_time(), paste, link, token)
print(f"\nOperation completed '{date_time()}.txt' created in the script path!")
uac('sc stop tor')
if __name__ == "__main__":
    pass
