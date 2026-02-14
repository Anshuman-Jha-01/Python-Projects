import win32com.client as wincl

participants = ["Ajay", "Rohan", "Sonali"]

spk = wincl.Dispatch("SAPI.SpVoice")
for participant in participants:
    spk.Speak(f"Shoutout to {participant}")
