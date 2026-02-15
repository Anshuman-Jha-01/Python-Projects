import time
import win32com.client as wincl

curr_time = time.strftime("%I")

spk = wincl.Dispatch("SAPI.SpVoice")
spk.Speak(f"It's {curr_time}'o clock. Please Drink Water.")

while True:
    time.sleep(3600) #Reminder interval in seconds
    spk.Speak(f"It's {curr_time}'o clock. Please Drink Water.")