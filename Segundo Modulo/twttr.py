VOCALES = ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"]


def main():
    Word = input("Enter a word of phrase: ").strip()
    Word = VowelEraser(Word)
    print(Word)


def VowelEraser(Phrase):
    for char in Phrase:
        for vowel in VOCALES:
            if char == vowel:
                Phrase = Phrase.replace(vowel, "")
    return Phrase

main()