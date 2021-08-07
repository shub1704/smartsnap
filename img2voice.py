import os
from gtts import gTTS
from img2text import imagetotext


def imagetovoice(text):
    mytext = text
    language = 'en'
    myobj = gTTS(text=mytext, lang=language, slow=False)
    myobj.save("welcome.mp3")                               #to save audio
    os.system("welcome.mp3")                                #to read audio clip


if __name__ == '__main__':
    text = imagetotext('snip1.png')
    print(text)                                              #to check string
    print(type(text))                                        #to check type of output
    imagetovoice(text)