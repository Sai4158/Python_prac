from playsound import playsound
from gtts import gTTS

audio = "spa.mp3"

# lets play the text now using the playsound
playsound(audio)

sp = gTTS(text="Welcome to the spa, we offer lot of services", lang="en", slow=False)


sp.save(audio)



# Text is now playing
print("Text is now playing")