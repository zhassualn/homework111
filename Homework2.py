CODE = {' ': '_',	"'": '.----.',	'(': '-.--.-',	')': '-.--.-',	',': '--..--',	'-': '-....-',	'.': '.-.-.-',	'/': '-..-.',
 '0': '-----',	'1': '.----',	'2': '..---',	'3': '...--',	'4': '....-',	'5': '.....',	'6': '-....',	'7': '--...',
 '8': '---..',	'9': '----.',	':': '---...',	';': '-.-.-.',	'?': '..--..',	'A': '.-',	'B': '-...',	'C': '-.-.',
 'D': '-..',	'E': '.',	'F': '..-.',	'G': '--.',	'H': '....',	'I': '..',	'J': '.---',	'K': '-.-',	'L': '.-..',
 'M': '--',	'N': '-.',	'O': '---',	'P': '.--.',	'Q': '--.-',	'R': '.-.',	'S': '...',	'T': '-',	'U': '..-',
 'V': '...-',	'W': '.--',	'X': '-..-',	'Y': '-.--',	'Z': '--..',	'_': '..--.-', '':' '}

#inverseMorseAlphabet=dict((v,k) for (k,v) in CODE.items())
inverseMorseAlphabet = {v: k for k, v in CODE.items()}

def convertToMorseCode(sentence):
    sentence = sentence.upper()
    englishcodedSentence = ""
    for character in sentence:
        englishcodedSentence += CODE[character] + " "
    return englishcodedSentence


def convertToEnglish(sentence1):
    b = sentence1.split(' ')
    MorsecodedSentence1 = ""
    for character in range(len(b)):
        MorsecodedSentence1 += inverseMorseAlphabet[b[character]]
    return MorsecodedSentence1

choice=input("Text or morse: ")


if choice == "text":
    given_sentence = input("enter text code: ")
    print(convertToMorseCode(given_sentence))


elif choice == "morse":
    given_sentence = input("enter morse code: ")
    print(convertToEnglish(given_sentence))