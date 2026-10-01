import sys
import random
from pyfiglet import Figlet

figlet = Figlet()
available_fonts = figlet.getFonts()
if len(sys.argv) not in [1, 3]:
    sys.exit("Invalid usage")
if len(sys.argv) == 3:
    if sys.argv[1] not in ["-f", "--font"]:
        sys.exit("Invalid usage")
    font = sys.argv[2]
    if font not in available_fonts:
        sys.exit("Invalid font")
else:
    font = random.choice(available_fonts)
figlet.setFont(font=font)
text = input("Text: ")
print(figlet.renderText(text))
