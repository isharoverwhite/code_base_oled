import time
import subprocess
 
from board import SCL, SDA
import busio
from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306
import os

i2c = busio.I2C(SCL, SDA)
 
# Create the SSD1306 OLED class.
# The first two parameters are the pixel width and pixel height.  Change these
# to the right size for your display!
disp = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c)
 
# Clear display.
disp.fill(0)
disp.show()
 
# Create blank image for drawing.
# Make sure to create image with mode '1' for 1-bit color.
width = disp.width
height = disp.height
image = Image.new("1", (width, height))
 
# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)
 
# Draw a black filled box to clear the image.
draw.rectangle((0, 0, width, height), outline=0, fill=0)
 
# Draw some shapes.
# First define some constants to allow easy resizing of shapes.
padding = -2
top = padding
bottom = height - padding
# Move left to right keeping track of the current x position for drawing shapes.
x = 0
 
delay = 0
# Load default font.
font = ImageFont.load_default()
 
while True:
                draw.rectangle((0, 0, width, height), outline=0, fill=0)
                f = open("/sys/class/thermal/thermal_zone0/temp", "r")
                t = f.readline ()
                cputemp = ""+t[0:2]
                minitemp = t[3]
                voltcore = 'vcgencmd measure_volts core'
                volt = subprocess.check_output(voltcore, shell=True).decode("utf-8")
                v = volt[5:9]
                cmd = "hostname -I | cut -d' ' -f1"
                IP = subprocess.check_output(cmd, shell=True).decode("utf-8")
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
                draw.text((100, top + 10), str(cputemp)+'°C', font=font, fill=255)
                draw.text((57, top + 0), IP, font=font, fill=255)
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
                    draw.text((76, top + 9), "!", font=font, fill=255)
                if cputemp >='81':
                    os.system("sudo shutdown now")
                disp.image(image)
                disp.show()
                time.sleep(0.1)