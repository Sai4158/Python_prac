from gtts import gTTS
from playsound import playsound

# audio file
audio = "speech.mp3"

# choose the lan and pass in
# Spanish
language = "es"

# English
language = "es"

# Create function for the words 
sp = gTTS(text="Hello World, I am Sai ", lang=language, slow=True)

# Save into the audio file 
sp.save(audio)


# playsoud using the text function
playsound(audio)