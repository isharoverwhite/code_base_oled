from datetime import date
from datetime import datetime
today = date.today()
from board import SCL, SDA
import busio
import os
import subprocess
import requests
import json
import time
from gpiozero import Button
from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306
i2c = busio.I2C(SCL, SDA)
bup = Button(21)
bdown = Button(18)
bselect = Button(24)
disp = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c)
disp.fill(0)
disp.show()
width = disp.width
height = disp.height
image = Image.new("1", (width, height))
draw = ImageDraw.Draw(image)
draw.rectangle((0, 0, width, height), outline=0, fill=0)
padding = -2
top = padding
bottom = height - padding
x = 0
arrow = 0
New = 58
List = 0
powerarrow = 0
os.system('clear')
font = ImageFont.load_default()
#load
draw.rectangle((0, 0, width, height), outline=0, fill=0)
draw.text((58, top + 0), "__ +", font=font, fill=255)
draw.text((58, top + 9), '__)', font=font, fill=255)
draw.text((58, top + 17), "__)", font=font, fill=255)
disp.image(image)
disp.show()
time.sleep(0.2)
draw.rectangle((0, 0, width, height), outline=0, fill=0)
draw.text((58, top + 0), "__ +", font=font, fill=255)
draw.text((58, top + 9), '__)', font=font, fill=255)
draw.text((58, top + 17), "__)", font=font, fill=255)
draw.text((0, top + -1), "-", font=font, fill=255)
draw.text((0, top + 0), "-", font=font, fill=255)
draw.text((0, top + 1), "-", font=font, fill=255)
draw.text((0, top + 2), "-", font=font, fill=255)
draw.text((0, top + 3), "-", font=font, fill=255)
draw.text((0, top + 4), "-", font=font, fill=255)
draw.text((0, top + 5), "-", font=font, fill=255)
draw.text((2, top + -1), "-", font=font, fill=255)
draw.text((2, top + 0), "-", font=font, fill=255)
draw.text((2, top + 1), "-", font=font, fill=255)
draw.text((2, top + 2), "-", font=font, fill=255)
draw.text((2, top + 3), "-", font=font, fill=255)
draw.text((2, top + 4), "-", font=font, fill=255)
draw.text((2, top + 5), "-", font=font, fill=255)
disp.image(image)
disp.show()
time.sleep(0.4)
draw.rectangle((0, 0, width, height), outline=0, fill=0)
draw.text((58, top + 0), "__ +", font=font, fill=255)
draw.text((58, top + 9), '__)', font=font, fill=255)
draw.text((58, top + 17), "__)", font=font, fill=255)
draw.text((0, top + 19), "-", font=font, fill=255)
draw.text((0, top + 20), "-", font=font, fill=255)
draw.text((0, top + 21), "-", font=font, fill=255)
draw.text((0, top + 22), "-", font=font, fill=255)
draw.text((0, top + 23), "-", font=font, fill=255)
draw.text((0, top + 24), "-", font=font, fill=255)
draw.text((0, top + 25), "-", font=font, fill=255)
draw.text((2, top + 19), "-", font=font, fill=255)
draw.text((2, top + 20), "-", font=font, fill=255)
draw.text((2, top + 21), "-", font=font, fill=255)
draw.text((2, top + 22), "-", font=font, fill=255)
draw.text((2, top + 23), "-", font=font, fill=255)
draw.text((2, top + 24), "-", font=font, fill=255)
draw.text((2, top + 25), "-", font=font, fill=255)
disp.image(image)
disp.show()
time.sleep(0.4)
draw.rectangle((0, 0, width, height), outline=0, fill=0)
draw.text((58, top + 0), "__ +", font=font, fill=255)
draw.text((58, top + 9), '__)', font=font, fill=255)
draw.text((58, top + 17), "__)", font=font, fill=255)
draw.text((120, top + -1), "-", font=font, fill=255)
draw.text((120, top + 0), "-", font=font, fill=255)
draw.text((120, top + 1), "-", font=font, fill=255)
draw.text((120, top + 2), "-", font=font, fill=255)
draw.text((120, top + 3), "-", font=font, fill=255)
draw.text((120, top + 4), "-", font=font, fill=255)
draw.text((120, top + 5), "-", font=font, fill=255)
draw.text((119, top + -1), "-", font=font, fill=255)
draw.text((119, top + 0), "-", font=font, fill=255)
draw.text((119, top + 1), "-", font=font, fill=255)
draw.text((119, top + 2), "-", font=font, fill=255)
draw.text((119, top + 3), "-", font=font, fill=255)
draw.text((119, top + 4), "-", font=font, fill=255)
draw.text((119, top + 5), "-", font=font, fill=255)
disp.image(image)
disp.show()
time.sleep(0.4)
draw.rectangle((0, 0, width, height), outline=0, fill=0)
draw.text((58, top + 0), "__ +", font=font, fill=255)
draw.text((58, top + 9), '__)', font=font, fill=255)
draw.text((58, top + 17), "__)", font=font, fill=255)
draw.text((120, top + 19), "-", font=font, fill=255)
draw.text((120, top + 20), "-", font=font, fill=255)
draw.text((120, top + 21), "-", font=font, fill=255)
draw.text((120, top + 22), "-", font=font, fill=255)
draw.text((120, top + 23), "-", font=font, fill=255)
draw.text((120, top + 24), "-", font=font, fill=255)
draw.text((120, top + 25), "-", font=font, fill=255)
draw.text((119, top + 19), "-", font=font, fill=255)
draw.text((119, top + 20), "-", font=font, fill=255)
draw.text((119, top + 21), "-", font=font, fill=255)
draw.text((119, top + 22), "-", font=font, fill=255)
draw.text((119, top + 23), "-", font=font, fill=255)
draw.text((119, top + 24), "-", font=font, fill=255)
draw.text((119, top + 25), "-", font=font, fill=255)
disp.image(image)
disp.show()
#end
time.sleep(0.5)
draw.text((New, top + 0), "__ +", font=font, fill=255)
draw.text((New, top + 9), '__)', font=font, fill=255)
draw.text((New, top + 17), "__)", font=font, fill=255)
disp.image(image)
disp.show()
while True:
    powerarrow = 0
    if New >= 104:
        New = 104
    draw.rectangle((0, 0, width, height), outline=0, fill=0)
    draw.text((New, top + 0), "__ +", font=font, fill=255)
    draw.text((New, top + 9), '__)', font=font, fill=255)
    draw.text((New, top + 17), "__)", font=font, fill=255)
    disp.image(image)
    disp.show()
    New = New + 2
    if New >= 104:
        New = 104
        break
while True:
    draw.rectangle((0, 0, width, height), outline=0, fill=0)
    draw.text((104, top + 0), "__ +", font=font, fill=255)
    draw.text((104, top + 9), '__)', font=font, fill=255)
    draw.text((104, top + 17), "__)", font=font, fill=255)
    draw.text((0, top + 1), "Press Select To", font=font, fill=255)
    draw.text((0, top + 10), "      Unlock", font=font, fill=255)
    disp.image(image)
    disp.show()
    if bselect.is_pressed:
        break
while True:
    cmd = 'cat /proc/net/wireless'
    ping =  subprocess.check_output(cmd, shell=True).decode("utf-8")
    wifisignal = (ping[182:185])
    New = 104
    draw.rectangle((0, 0, width, height), outline=0, fill=0)
    draw.text((104, top + 0), "__ +", font=font, fill=255)
    draw.text((104, top + 9), '__)', font=font, fill=255)
    draw.text((104, top + 17), "__)", font=font, fill=255)
    if List <= -30:
        List = -30
    elif List >= 0:
        List = 0
    if New >= 104:
        New = 104
        if wifisignal == "" or wifisignal == " ":
            draw.text((90, top + 0), "\ ", font=font, fill=255)
            draw.text((89, top + 0), "/", font=font, fill=255)
        else:
            if wifisignal <= '-55':
                draw.text((86, top + -5), "__", font=font, fill=255)
                draw.text((89, top + -3), "_", font=font, fill=255)
                draw.text((90, top + 1), ".", font=font, fill=255)
            if wifisignal >= '-55' and wifisignal <= '-70':
                draw.text((89, top + -3), "_", font=font, fill=255)
                draw.text((90, top + 1), ".", font=font, fill=255)
            if wifisignal >= '-70':
                draw.text((90, top + 1), ".", font=font, fill=255)
        draw.text((0, top + List), "IP", font=font, fill=255)
        draw.text((0, top + List + 10), "Dianostic", font=font, fill=255)
        draw.text((0, top + List + 20), "2FA", font=font, fill=255)
        draw.text((0, top + List + 30), "Clock", font=font, fill=255)
        draw.text((0, top + List + 40), "Blank Scr", font=font, fill=255)
        draw.text((0, top + List + 50), "Power", font=font, fill=255)
        #arrow
        draw.text((62, top + arrow), "<=", font=font, fill=255)
        draw.text((56, top + 0), "|  |", font=font, fill=255)
        draw.text((56, top + 7), "|  |", font=font, fill=255)
        draw.text((56, top + 14), "|  |", font=font, fill=255)
        draw.text((56, top + 21), "|  |", font=font, fill=255)
        draw.text((56, top + 23), "|  |", font=font, fill=255)
        disp.image(image)
        disp.show()
        print("List"+str(List)+'   arrow: '+str(arrow),end='\r')
    disp.image(image)
    disp.show()
    New = New + 2
    if bup.is_pressed:
        time.sleep(0.1)
        arrow = arrow - 10
        if arrow < 0:
            arrow = 0
            List = List + 10
    elif bdown.is_pressed:
        time.sleep(0.1)
        arrow = arrow + 10
        if arrow >= 21:
            arrow = 20
            List = List - 10
    if bselect.is_pressed:
        if List == 0 and arrow == 20 or List == -10 and arrow == 10 or arrow == 0 and List == 0 or arrow == -20 and List == 20 or List == -30 and arrow == 20:
            time.sleep(0)
        else:
            while True:
                if New <= 58:
                    New = 58
                    break
                draw.rectangle((0, 0, width, height), outline=0, fill=0)
                draw.text((New, top + 0), "__ +", font=font, fill=255)
                draw.text((New, top + 9), '__)', font=font, fill=255)
                draw.text((New, top + 17), "__)", font=font, fill=255)
                disp.image(image)
                disp.show()
                New = New - 2
        if arrow == 10 and List == 0 or arrow == 0 and List == -10:
            while True:
                f = open("/sys/class/thermal/thermal_zone0/temp", "r")
                t = f.readline ()
                cputemp = ""+t[0:2]
                minitemp = t[3]
                voltcore = 'vcgencmd measure_volts core'
                volt = subprocess.check_output(voltcore, shell=True).decode("utf-8")
                v = volt[5:9]
                cmd = 'df -h | awk \'$NF=="/"{printf "%s/%d", $3,$2,$5}\''
                Disk = subprocess.check_output(cmd, shell=True).decode("utf-8")
                cmd = "free -m | awk 'NR==2{printf \"%s/%s\", $3,$2,$3*100/$2 }'"
                MemUsage = subprocess.check_output(cmd, shell=True).decode("utf-8")
                cmd = 'cut -f 1 -d " " /proc/loadavg'
                CPU = subprocess.check_output(cmd, shell=True).decode("utf-8")
                draw.rectangle((0, 0, width, height), outline=0, fill=0)
                draw.text((0, top + 0), v+"V", font=font, fill=255)
                draw.text((58, top + 0), "__", font=font, fill=255)
                draw.text((58, top + 9), '__)', font=font, fill=255)
                draw.text((0, top + 10), CPU, font=font, fill=255)
                draw.text((58, top + 17), "__)" ,font=font, fill=255)
                draw.text((0, top + 21), Disk+"", font=font, fill=255)
                draw.text((80, top + 21), MemUsage, font=font, fill=255)
                draw.text((100, top + 0), str(cputemp)+'°C', font=font, fill=255)
                if v <= '1.20':
                    draw.text((40, top + 0), '!', font=font, fill=255)
                if cputemp >= '45':
                    draw.text((87, top + 0), '!', font=font, fill=255)
                cmd = 'df -h | awk \'$NF=="/"{printf "Disk: %d/%d GB  %s", $3,$2,$5}\''
                percent = subprocess.check_output(cmd, shell=True).decode("utf-8")
                pdisk = percent[14:16]
                if pdisk >= '80':
                    draw.text((40, top + 21), '!', font=font, fill=255)
                if CPU >= '5.00':
                    draw.text((40, top + 10), '!', font=font, fill=255)
                if pdisk >= '80' and v <= '1.20' and cputemp >= '45' and CPU >= '2.00' and MemUsage[0:3] >= '500':
                    draw.text((76, top + 0), "!", font=font, fill=255)
                else:
                    draw.text((76, top + 0), "+", font=font, fill=255)
            #vertical
                disp.image(image)
                disp.show()
                if bselect.is_pressed:
                    time.sleep(0.3)
                    break
        if arrow == 20 and List == 0:
                while True:
                    if New >= 104:
                        New = 104
                        draw.rectangle((0, 0, width, height), outline=0, fill=0)
                        draw.text((New, top + 0), "__ +", font=font, fill=255)
                        draw.text((New, top + 9), '__)', font=font, fill=255)
                        draw.text((New, top + 17), "__)", font=font, fill=255)
                        disp.image(image)
                        disp.show()
                        New = New + 2
                        if New >= 104:
                            New = 104
                            break
    #2FA
        if List == 0 and arrow == 20 or List == -10 and arrow == 10 or List == -20 and arrow == 0:
                while True:
                    url = 'https://2fa.live/tok/'
                    nick = 'ZRXPWLTDW2I2QOA642EDNJO776AIYKDA'
                    get2fa =  requests.get(url+nick)
                    if bselect.is_pressed:
                        time.sleep(0.4)
                        break
                    fa = json.loads(get2fa.text)
                    fa4oled = fa["token"]
                    draw.rectangle((0, 0, width, height), outline=0, fill=0)
                    draw.text((104, top + 0), "__ +", font=font, fill=255)
                    draw.text((104, top + 9), '__)', font=font, fill=255)
                    draw.text((104, top + 17), "__)", font=font, fill=255)
                    draw.text((0, top + 0),"2FA:"+str(fa4oled) , font=font, fill=255)
                    disp.image(image)
                    disp.show()
                    if bselect.is_pressed:
                        time.sleep(0.4)
                        break
    #Clock
        if List == -10 and arrow == 20 or List == -20 and arrow == 10 or List == -30 and arrow == 0:
                while True:
                    Day = today.strftime("%d-%m")
                    year =today.strftime("%Y")
                    now = datetime.now()
                    nowtimen = now.strftime("%H:%M")
                    sec = now.strftime("%S")
                    draw.rectangle((0, 0, width, height), outline=0, fill=0)
                    draw.text((58, top + 0), "__ +", font=font, fill=255)
                    draw.text((58, top + 9), '__)', font=font, fill=255)
                    draw.text((58, top + 17), "__)", font=font, fill=255)
                    draw.text((0, top + 0),nowtimen, font=font, fill=255)
                    draw.text((0, top + 10),'   '+sec, font=font, fill=255)
                    draw.text((0, top + 21),Day, font=font, fill=255)
                    draw.text((105, top + 21),year, font=font, fill=255)
                    disp.image(image)
                    disp.show()
                    if bselect.is_pressed:
                        break
    #IP
        if arrow == 0 and List == 0:
                while True:
                    cmd = "hostname -I | cut -d' ' -f1"
                    IP = subprocess.check_output(cmd, shell=True).decode("utf-8")
                    cmd = 'cat /proc/net/wireless'
                    ping =  subprocess.check_output(cmd, shell=True).decode("utf-8")
                    wifisignal = (ping[183:185])
                    if IP == "":
                        IP = "Non Wifi Of Lan"
                    draw.rectangle((0, 0, width, height), outline=0, fill=0)
                    draw.text((104, top + 0), "__ +", font=font, fill=255)
                    draw.text((104, top + 9), '__)', font=font, fill=255)
                    draw.text((104, top + 17), "__)", font=font, fill=255)
                    draw.text((0, top + 0),'IP:'+IP, font=font, fill=255)
                    draw.text((0, top + 10),'Signal:'+(wifisignal)+' dBm', font=font, fill=255)
                    draw.text((0, top + 10),'', font=font, fill=255)
                    disp.image(image)
                    disp.show()
                    if bselect.is_pressed:
                        time.sleep(0.4)
                        break
    #blank screen
        if arrow == 20 and List == -20 or List == -30 and arrow == 10:
                while True:
                    draw.rectangle((0, 0, width, height), outline=0, fill=0)
                    disp.image(image)
                    disp.show()
                    if bselect.is_pressed:
                        break
    #shutdown_option
        if List == -30 and arrow == 20:
            powerarrow = 0
            while True:
                if powerarrow <= 0:
                    powerarrow = 0
                if powerarrow >= 21:
                    powerarrow = 20
                draw.rectangle((0, 0, width, height), outline=0, fill=0)
                draw.text((104, top + 0), "__ +", font=font, fill=255)
                draw.text((104, top + 9), '__)', font=font, fill=255)
                draw.text((104, top + 17), "__)", font=font, fill=255)
                draw.text((0, top + 0), "Shutdown", font=font, fill=255)
                draw.text((0, top + 10), "Reboot", font=font, fill=255)
                draw.text((0, top + 20), "back", font=font, fill=255)
                draw.text((62, top + powerarrow), "<=", font=font, fill=255)
                draw.text((56, top + 0), "|  |", font=font, fill=255)
                draw.text((56, top + 7), "|  |", font=font, fill=255)
                draw.text((56, top + 14), "|  |", font=font, fill=255)
                draw.text((56, top + 21), "|  |", font=font, fill=255)
                draw.text((56, top + 23), "|  |", font=font, fill=255)
                disp.image(image)
                disp.show()
                time.sleep(0.1)
                if bup.is_pressed:
                    powerarrow = powerarrow - 10
                if bdown.is_pressed:
                    powerarrow = powerarrow + 10
                if bselect.is_pressed:
                    if powerarrow == 0:
                        draw.rectangle((0, 0, width, height), outline=0, fill=0)
                        draw.text((0, top + 0), "Shutting Down...", font=font, fill=255)
                        disp.image(image)
                        disp.show()
                        New = 0
                        while True:
                            draw.text((New, top + 20), "_", font=font, fill=255)
                            disp.image(image)
                            disp.show()
                            New = New + 4
                            if New >= 130:
                                New = 130
                                draw.rectangle((0, 0, width, height), outline=0, fill=0)
                                disp.image(image)
                                disp.show()
                                os.system('sudo shutdown now')
                    if powerarrow == 10:
                        draw.rectangle((0, 0, width, height), outline=0, fill=0)
                        draw.text((0, top + 0), "Rebooting", font=font, fill=255)
                        disp.image(image)
                        disp.show()
                        New = 0
                        while True:
                            draw.text((New, top + 20), "_", font=font, fill=255)
                            disp.image(image)
                            disp.show()
                            New = New + 4
                            if New >= 130:
                                New = 130
                                draw.rectangle((0, 0, width, height), outline=0, fill=0)
                                disp.image(image)
                                disp.show()
                                os.system('sudo reboot')
                    if powerarrow == 20:
                        break