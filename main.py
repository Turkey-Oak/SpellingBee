import  search_and_load
import sys
import os

def word_len(word):
    r = 0
    while word[r:]:
        r += 1
    #print(f"WL = {r}")
    return r

def main():
    wordlist = "words.txt"
    if len(sys.argv) -1 > 0:
        if sys.argv[1].lower() == "-h" or sys.argv[1].lower() == "-help":
            print("-wl wordlist filename")
            sys.exit()
        elif sys.argv[1].lower() == "-wl":
            if len(sys.argv) -1 > 1:
                if os.path.isfile(sys.argv[2]):
                    wordlist = sys.argv[2]
                    print(f"Using {wordlist} as the wordlist file.")
                else:
                    print("Wordlist not found, resorting to default.")
    print("Spelling Bee!")
    print("")
    valid_entry = False
    while not valid_entry:
        letters = list(input("Please enter the letters:").lower())
        key_letter = input("Please enter key letter:").lower()
        letter_len = word_len(letters)
        if letter_len == 7 and key_letter in letters:
            valid_entry = True


    search_and_load.search(letters, key_letter, wordlist)


if  __name__ == '__main__':
    main()