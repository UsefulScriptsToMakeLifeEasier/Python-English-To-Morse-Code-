import time
import winsound

# Define the Morse code dictionary using a dictionary comprehension
MORSE_CODE = {char: code for char, code in [
    ('A', '.-'), ('B', '-...'), ('C', '-.-.'), ('D', '-..'), ('E', '.'),
    ('F', '..-.'), ('G', '--.'), ('H', '....'), ('I', '..'), ('J', '.---'),
    ('K', '-.-'), ('L', '.-..'), ('M', '--'), ('N', '-.'), ('O', '---'),
    ('P', '.--.'), ('Q', '--.-'), ('R', '.-.'), ('S', '...'), ('T', '-'),
    ('U', '..-'), ('V', '...-'), ('W', '.--'), ('X', '-..-'), ('Y', '-.--'),
    ('Z', '--..'), ('0', '-----'), ('1', '.----'), ('2', '..---'),
    ('3', '...--'), ('4', '....-'), ('5', '.....'), ('6', '-....'),
    ('7', '--...'), ('8', '---..'), ('9', '----.'), ('.', '.-.-.-'),
    (',', '--..--'), ('?', '..--..'), ("'", '.----.'), ('!', '-.-.--'),
    ('/', '-..-.'), ('(', '-.--.'), (')', '-.--.-'), ('&', '.-...'),
    (':', '---...'), (';', '-.-.-.'), ('=', '-...-'), ('+', '.-.-.'),
    ('-', '-....-'), ('_', '..--.-'), ('"', '.-..-.'), ('$', '...-..-'),
    ('@', '.--.-.')
]}

# Define the unit time for Morse code playback, in milliseconds
UNIT_TIME = 100

# Define the dot and dash lengths in terms of the unit time
DOT_LENGTH = UNIT_TIME
DASH_LENGTH = UNIT_TIME * 3

# Define the length of a space between letters and words in terms of the unit time
LETTER_SPACE_LENGTH = UNIT_TIME
WORD_SPACE_LENGTH = UNIT_TIME * 3

# Define the function to convert a message to Morse code
def message_to_morse(message):
    # Convert the message to upper case
    message = message.upper()
    # Convert the message to Morse code
    morse_message = ''
    for char in message:
        morse_char = MORSE_CODE.get(char, ' ')
        morse_message += morse_char + ' '
    return morse_message

# Define the function to play a Morse code message as sound
def play_morse_message(morse_message):
    # Add a short delay before playing the first sound
    time.sleep(0.5)
    # Play the Morse code message as sound
    for char in morse_message:
        if char == '.':
            winsound.Beep(440, DOT_LENGTH)
        elif char == '-':
            winsound.Beep(440, DASH_LENGTH)
        elif char == ' ':
            time.sleep(LETTER_SPACE_LENGTH / 1000)
        elif char == '/':
            time.sleep(WORD_SPACE_LENGTH / 1000)
        else:
            continue
        time.sleep(UNIT_TIME / 1000)

# Prompt the user for input and play the corresponding Morse code
while True:
    message = input("Enter a message to convert to Morse code: ")
    if message == "exit":
        break
    morse_message = message_to_morse(message)
    print(morse_message)
    play_morse_message(morse_message)

