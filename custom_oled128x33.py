#gpio12 nut di chuyen
#gpio14 nut back
#gpio21 nut chon
from gpiozero import Button, LED
from datetime import date
import time
import os
import subprocess
from datetime import datetime
from board import SCL, SDA
import busio
from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306
bup = Button(12)
bback = Button(14)
bselect  =  Button(21)
i2c = busio.I2C(SCL, SDA)
l1 = LED(16)

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
down = 0
font = ImageFont.load_default()
while True:
    while True:
        if bup.is_pressed:
            time.sleep(0.1)
            down = down + 10
        if down >= 21:
          down = 0
        elif down < 0:
            down = 0
        else:
            time.sleep(0)
        draw.rectangle((0, 0, width, height), outline=0, fill=0)
        draw.text((x, top + 0), "Trang  Thai", font=font, fill=255)
        draw.text((x, top + 10), "Cai Dat", font=font, fill=255)
        draw.text((x, top + 20), "Credits", font=font, fill=255)
        draw.text((100, top + down), "<=", font=font, fill=255)
        if bselect.is_pressed:
            time.sleep(0.1)
            if down == 0:
                disp.fill(0)
                disp.show()
                draw.rectangle((0, 0, width, height), outline=0, fill=0)
                while True:
                 today = date.today()
                 draw.rectangle((0, 0, width, height), outline=0, fill=0)
                 cmd = "hostname -I | cut -d' ' -f1"
                 IP = subprocess.check_output(cmd, shell=True).decode("utf-8")
                 cmd = "top -bn1 | grep load | awk '{printf \"CPU Load: %.2f\", $(NF-2)}'"
                 CPU = subprocess.check_output(cmd, shell=True).decode("utf-8")
                 cmd = 'df -h | awk \'$NF=="/"{printf "Disk: %d/%d GB  %s", $3,$2,$5}\''
                 Disk = subprocess.check_output(cmd, shell=True).decode("utf-8")
                 d1 = today.strftime("%d/%m/%Y")
                 # Write four lines of text.
                 now = datetime.now()
                 nowtime = now.strftime("%H:%M:%S")
                 draw.text((x, top + 9), "IP: " + IP, font=font, fill=255)
                 draw.text((x, top + 17), CPU+'%', font=font, fill=255)
                 draw.text((x, top + 0), d1+'  '+nowtime, font=font, fill=255)
                 draw.text((x, top + 25), Disk, font=font, fill=255)
                 disp.image(image)
                 disp.show()
                 if bback.is_pressed:
                     break
            if down == 10:
                disp.fill(0)
                disp.show()
                draw.rectangle((0, 0, width, height), outline=0, fill=0)
                down = 0
                while True:
                    draw.rectangle((0, 0, width, height), outline=0, fill=0)
                    if bup.is_pressed:
                        time.sleep(0.1)
                        down = down + 10
                    if down >= 21:
                        down =  0
                    draw.text((x, top + 0), "Cap Nhat He Thong ", font=font, fill=255)
                    draw.text((x, top + 10), "Tat Nguon ", font=font, fill=255)
                    draw.text((x, top + 20), "Khoi Dong Lai", font=font, fill=255)
                    draw.text((110, top + down), "<=", font=font, fill=255)
                    disp.image(image)
                    disp.show()
                    if bback.is_pressed:
                        break
                    if bselect.is_pressed:
                        time.sleep(0.1)
                        if down == 0:
                            disp.fill(0)
                            disp.show()
                            draw.rectangle((0, 0, width, height), outline=0, fill=0)
                            draw.text((0, top + 0), "Dang Cap Nhat He Thong", font=font, fill=255)
                            disp.image(image)
                            disp.show()
                            os.system("sudo apt update && sudo apt upgrade")
                            break
                        if down == 10:
                            disp.fill(0)
                            disp.show()
                            draw.rectangle((0, 0, width, height), outline=0, fill=0)
                            draw.text((0, top + 0), "Dang Tat He Thong", font=font, fill=255)
                            disp.image(image)
                            disp.show()
                            time.sleep(1)
                            disp.fill(0)
                            disp.show()
                            draw.rectangle((0, 0, width, height), outline=0, fill=0)
                            os.system('sudo shutdown now')
                        if down == 20:
                            disp.fill(0)
                            disp.show()
                            draw.rectangle((0, 0, width, height), outline=0, fill=0)
                            draw.text((0, top + 0), "Dang KDL He Thong", font=font, fill=255)
                            disp.image(image)
                            disp.show()
                            time.sleep(1)
                            disp.fill(0)
                            disp.show()
                            draw.rectangle((0, 0, width, height), outline=0, fill=0)
                            os.system('sudo shutdown -r now')
            if down == 20:
                disp.fill(0)
                disp.show()
                draw.rectangle((0, 0, width, height), outline=0, fill=0)
                while True:
                    draw.rectangle((0, 0, width, height), outline=0, fill=0)
                    draw.text((0, top + 0), "Code By RYZEN30xx", font=font, fill=255)
                    disp.image(image)
                    disp.show()
                    if bback.is_pressed:
                        break
        
        disp.image(image)
        disp.show()
