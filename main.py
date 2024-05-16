from gtts import gTTS
import os
file = open("test.txt", "r")
file_text = file.read().replace("\n", " ")
language = "en"
output = gTTS(text=file_text, lang=language, slow=False)
output.save("output.mp3")
file.close()
os.system("start output.mp3")