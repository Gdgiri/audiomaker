# Import the required module for text 
# to speech conversion
from gtts import gTTS
  
# This module is imported so that we can 
# play the converted audio
import os
  
# The text that you want to convert to audio
mytext = 'கு,ண்,டு,குண்டு'
# Language in which you want to convert
language = 'ta'
  
# Passing the text and language to the engine, 
# here we have marked slow=False. Which tells 
# the module that the converted audio should 
# have a high speed
myobj = gTTS(text=mytext, lang=language, slow=True)
  
# Saving the converted audio in a mp3 file named
# welcome 
myobj.save("kundu.mp3")
  
# Playing the converted file
os.system("kundu.mp3")
