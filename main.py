""" A simple string to Morse code converter.


International Morse code is composed of five elements:

1. short mark, dot or dit (  ▄ ): "dit duration" is one time unit long
2. long mark, dash or dah (  ▄▄▄ ): three time units long
3. inter-element gap between the dits and dahs within a character: one dot duration or one unit long
4. short gap (between letters): three time units long
5. medium gap (between words): seven time units long"""

import ascii_text

from morse_converter import MorseConverter

print(ascii_text.greeting)


def run():
    while True:
        text = input("Enter the text to convert into morse code (or \"EXIT\" to quit): ")
        if text == "EXIT":
            print(ascii_text.farewell)
            break

        morse = MorseConverter(text)
        print(morse.get_visual() + "\n")


if __name__ == '__main__':
    run()
