from gtts import gTTS
import time
import sys
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame

# Text to be read
text = """
トミノの地獄

姉は血を吐く、妹（いもと）は火吐く、
可愛いトミノは 宝玉（たま）を吐く。
ひとり地獄に落ちゆくトミノ、
地獄くらやみ花も無き。
鞭で叩くはトミノの姉か、
鞭の朱総（しゅぶさ）が 気にかかる。
叩けや叩きやれ叩かずとても、
無間地獄はひとつみち。
暗い地獄へ案内（あない）をたのむ、
金の羊に、鶯に。
皮の嚢（ふくろ）にやいくらほど入れよ、
無間地獄の旅支度。
春が 来て候（そろ）林に谿（たに）に、
暗い地獄谷七曲り。
籠にや鶯、車にや羊、
可愛いトミノの眼にや涙。
啼けよ、鶯、林の雨に
妹恋しと 声かぎり。
啼けば反響（こだま）が地獄にひびき、 
狐牡丹の花がさく。
地獄七山七谿めぐる、
可愛いトミノのひとり旅。
地獄ござらばもて 来てたもれ、 
針の御山（おやま）の留針（とめはり）を。
赤い留針だてにはささぬ、 
可愛いトミノのめじるしに。
"""
# ANSI escape code for red text
RED_TEXT = "\033[31m"
RESET_COLOR = "\033[0m"

# Initialize TTS engine
tts = gTTS(text, lang='ja')

# Save the TTS audio to a file
tts.save("tts_output.mp3")

# Initialize pygame mixer
pygame.mixer.init()

# Load and play the TTS audio file
pygame.mixer.music.load("tts_output.mp3")
pygame.mixer.music.play()

# Iterate through characters, color them red, and print to the terminal
for char in text:
    sys.stdout.write(RED_TEXT + char + RESET_COLOR)  # Print character in red
    sys.stdout.flush()      # Flush buffer to ensure immediate display
    time.sleep(0.01)         # Delay for a short duration
print("\n")

# Wait for the audio to finish playing
while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)

