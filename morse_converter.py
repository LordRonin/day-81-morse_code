from audio_creator import AudioCreator

MORSE_CODE_ITU_STANDARD = {
    'A': '▄ ▄▄▄',
    'B': '▄▄▄ ▄ ▄ ▄',
    'C': '▄▄▄ ▄ ▄▄▄ ▄',
    'D': '▄▄▄ ▄ ▄',
    'E': '▄',
    'F': '▄ ▄ ▄▄▄ ▄',
    'G': '▄▄▄ ▄▄▄ ▄',
    'H': '▄ ▄ ▄ ▄',
    'I': '▄ ▄',
    'J': '▄ ▄▄▄ ▄▄▄ ▄▄▄',
    'K': '▄▄▄ ▄ ▄▄▄',
    'L': '▄ ▄▄▄ ▄ ▄',
    'M': '▄▄▄ ▄▄▄',
    'N': '▄▄▄ ▄',
    'O': '▄▄▄ ▄▄▄ ▄▄▄',
    'P': '▄ ▄▄▄ ▄▄▄ ▄',
    'Q': '▄▄▄ ▄▄▄ ▄ ▄▄▄',
    'R': '▄ ▄▄▄ ▄',
    'S': '▄ ▄ ▄',
    'T': '▄▄▄',
    'U': '▄ ▄ ▄▄▄',
    'V': '▄ ▄ ▄ ▄▄▄',
    'W': '▄ ▄▄▄ ▄▄▄',
    'X': '▄▄▄ ▄ ▄▄▄ ▄▄▄',
    'Y': '▄▄▄ ▄ ▄▄▄ ▄▄▄',
    'Z': '▄▄▄ ▄▄▄ ▄ ▄',
    '1': '▄ ▄▄▄ ▄▄▄ ▄▄▄ ▄▄▄',
    '2': '▄ ▄ ▄▄▄ ▄▄▄ ▄▄▄',
    '3': '▄ ▄ ▄ ▄▄▄ ▄▄▄',
    '4': '▄ ▄ ▄ ▄ ▄▄▄',
    '5': '▄ ▄ ▄ ▄ ▄',
    '6': '▄▄▄ ▄ ▄ ▄ ▄',
    '7': '▄▄▄ ▄▄▄ ▄ ▄ ▄',
    '8': '▄▄▄ ▄▄▄ ▄▄▄ ▄ ▄',
    '9': '▄▄▄ ▄▄▄ ▄▄▄ ▄▄▄ ▄',
    '0': '▄▄▄ ▄▄▄ ▄▄▄ ▄▄▄ ▄▄▄',
    ' ': '    ',
    '.': '▄ ▄▄▄ ▄ ▄▄▄ ▄ ▄▄▄',
    ',': '▄▄▄ ▄▄▄ ▄ ▄ ▄▄▄ ▄▄▄',
    '?': '▄ ▄ ▄▄▄ ▄▄▄ ▄ ▄',
    '\'': '▄ ▄▄▄ ▄▄▄ ▄▄▄ ▄▄▄ ▄',
    '!': '▄▄▄ ▄ ▄▄▄ ▄ ▄▄▄ ▄▄▄',
    '/': '▄▄▄ ▄ ▄ ▄▄▄ ▄',
    '(': '▄▄▄ ▄ ▄▄▄ ▄▄▄ ▄',
    ')': '▄▄▄ ▄ ▄▄▄ ▄▄▄ ▄ ▄▄▄',
    '&': '▄ ▄▄▄ ▄ ▄ ▄',
    ':': '▄▄▄ ▄▄▄ ▄▄▄ ▄ ▄ ▄',
    ';': '▄▄▄ ▄ ▄▄▄ ▄ ▄▄▄ ▄',
    '=': '▄▄▄ ▄ ▄ ▄ ▄▄▄',
    '+': '▄ ▄▄▄ ▄ ▄▄▄ ▄',
    '-': '▄▄▄ ▄ ▄ ▄ ▄ ▄▄▄',
    '_': '▄ ▄ ▄▄▄ ▄▄▄ ▄ ▄▄▄',
    '\"': '▄ ▄▄▄ ▄ ▄ ▄▄▄ ▄',
    '$': '▄ ▄ ▄ ▄▄▄ ▄ ▄ ▄▄▄',
    '@': '▄ ▄▄▄ ▄▄▄ ▄ ▄▄▄ ▄',

}
UNIT_DURATION = 150
SAMPLE_RATE = 8000
FREQUENCY = 220


class MorseConverter:
    """
    Class to convert string into sound and visual Morse code.
    """

    def __init__(self, text: str):
        self._text = text.upper()
        self._visual_morse_code = self._generate_visual()
        self._simplified_visual = self._simplify_visual()
        self.audio = AudioCreator(
            sample_rate=SAMPLE_RATE, duration=UNIT_DURATION, frequency=FREQUENCY)
        self._generate_audio()

    def get_visual(self):
        return self._visual_morse_code

    def get_text(self):
        return self._text

    def _generate_visual(self):
        morse_code_string = ""
        for character in self._text:
            morse_code_string += self._encode_character(character) + "   "
        return morse_code_string

    def _simplify_visual(self):
        simplified_visual = self._visual_morse_code
        # Replace spaces after unknown symbols represented with '#' and symbols themselves.
        simplified_visual = simplified_visual.replace("# ", "").replace("#", "")
        # Replace dashes (▄▄▄) with simplified (-)
        simplified_visual = simplified_visual.replace("▄▄▄", "-")
        # Replace dots (▄) with simplified (.)
        simplified_visual = simplified_visual.replace("▄", ".")
        return simplified_visual

    def _generate_audio(self):
        for sign in self._simplified_visual:
            if sign == '.':
                self._add_dot()
            elif sign == '-':
                self._add_dash()
            elif sign == ' ':
                self._add_gap()
        self.audio.save_file('morse.wav')

    def _add_dot(self):
        self.audio.add_unit_sound()

    def _add_dash(self):
        # Dash is 3 units long
        for _ in range(3):
            self._add_dot()

    def _add_gap(self):
        self.audio.add_unit_gap()

    @staticmethod
    def _encode_character(char: str) -> str:
        # In case character not in dictionary add pound sign to a string.
        return MORSE_CODE_ITU_STANDARD.get(char, '#')
