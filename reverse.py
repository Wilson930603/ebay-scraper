# Genymotion Desktop
import os, subprocess
import time

# Create Genymotion Device

# Open Genymotion Device 
os.system("open -a /Applications/Genymotion.app/Contents/MacOS/player.app --args --vm-name 'S10'")
print("======= Opening Genymotion Device ====== ")

while 'device' not in os.popen("adb get-state").read():
    time.sleep(10)
print('Opened')
time.sleep(20)
# Install Ebay app 
print("======= Installing Ebay App ====== ")
apk_path = "/Users/info/Downloads/com.ebay.kleinanzeigen_2021-02-11.apk"

os.system(f'''adb install {apk_path} ''')
# Raunning Frida server
FRIDA_SERVER = "/Users/info/Downloads/frida-server-14.2.12-android-x86"

print("======= Pushing Frida Server ====== ")
os.system(f'''adb push {FRIDA_SERVER} /data/local/tmp/frida''')

os.system(f"adb shell \"su -c 'chmod 755 /data/local/tmp/frida'\"")
subprocess.Popen(['adb', 'shell', "su -c'/data/local/tmp/frida -l 0.0.0.0'"])

print("======= Frida Running ======  ")

print("======= Opening Ebay App ====== ")
os.system(f'adb shell am start -n com.ebay.kleinanzeigen')
time.sleep(2)
print("======= Reverse the App ====== ")
os.system(f'objection --gadget "com.ebay.kleinanzeigen" explore')
# 
print("======= Capture the Traffic ====== ")
os.system(f'android sslpinning disable')

print("======= Store the AppKey ====== ")
os.system(f'')

# ps -e | grep frida
# kill -9 PID

#os.system("open /Applications/Genymotion.app")
# Close Genymotion
#os.system("pkill /Applications/Genymotion.app")
# Open Genymotion shell
#os.system("/Applications/Genymotion Shell.app/Contents/MacOS/genyshell")