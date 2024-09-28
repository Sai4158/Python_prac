from text_to_speech import save

text = "This is a slow speech example."
language = "en"
output_file = "slow_speech.mp3"

save(text, language, slow=True, file=output_file)