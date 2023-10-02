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

Tomino’s Hell

Elder sister vomits blood,
younger sister’s breathing fire
while sweet little Tomino
just spits up the jewels.

All alone does Tomino
go falling into that hell,
a hell of utter darkness,
without even flowers.

Is Tomino’s big sister
the one who whips him?
The purpose of the scourging
hangs dark in his mind.

Lashing and thrashing him, ah!
But never quite shattering.
One sure path to Avici,
the eternal hell.

Into that blackest of hells
guide him now, I pray—
to the golden sheep,
to the nightingale.

How much did he put
in that leather pouch
to prepare for his trek to
the eternal hell?

Spring is coming
to the valley, to the wood,
to the spiraling chasms
of the blackest hell.

The nightingale in her cage,
the sheep aboard the wagon,
and tears well up in the eyes
of sweet little Tomino.

Sing, o nightingale,
in the vast, misty forest—
he screams he only misses
his little sister.

His wailing desperation
echoes throughout hell—
a fox peony
opens its golden petals.

Down past the seven mountains
and seven rivers of hell—
the solitary journey
of sweet little Tomino.

If in this hell they be found,
may they then come to me, please,
those sharp spikes of punishment
from Needle Mountain.

Not just on some empty whim
Is flesh pierced with blood-red pins:
they serve as hellish signposts
for sweet little Tomino.
"""

text2 = """

Tomino’s Hell

Elder sister vomits blood,
younger sister’s breathing fire
while sweet little Tomino
just spits up the jewels.

All alone does Tomino
go falling into that hell,
a hell of utter darkness,
without even flowers.

Is Tomino’s big sister
the one who whips him?
The purpose of the scourging
hangs dark in his mind.

Lashing and thrashing him, ah!
But never quite shattering.
One sure path to Avici,
the eternal hell.

Into that blackest of hells
guide him now, I pray—
to the golden sheep,
to the nightingale.

How much did he put
in that leather pouch
to prepare for his trek to
the eternal hell?

Spring is coming
to the valley, to the wood,
to the spiraling chasms
of the blackest hell.

The nightingale in her cage,
the sheep aboard the wagon,
and tears well up in the eyes
of sweet little Tomino.

Sing, o nightingale,
in the vast, misty forest—
he screams he only misses
his little sister.

His wailing desperation
echoes throughout hell—
a fox peony
opens its golden petals.

Down past the seven mountains
and seven rivers of hell—
the solitary journey
of sweet little Tomino.

If in this hell they be found,
may they then come to me, please,
those sharp spikes of punishment
from Needle Mountain.

Not just on some empty whim
Is flesh pierced with blood-red pins:
they serve as hellish signposts
for sweet little Tomino.
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

# Iterate through characters, color them red, and print to the terminal
for char in text2:
    sys.stdout.write(RED_TEXT + char + RESET_COLOR)  # Print character in red
    sys.stdout.flush()      # Flush buffer to ensure immediate display
    time.sleep(0.01)         # Delay for a short duration
print("\n")

# Wait for the audio to finish playing
while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)

