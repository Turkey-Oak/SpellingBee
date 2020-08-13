import  search_and_load

def word_len(word):
    r = 0
    while word[r:]:
        r += 1
    #print(f"WL = {r}")
    return r

def main():
    print("Spelling Bee!")
    print("")
    valid_entry = False
    while not valid_entry:
        letters = list(input("Please enter the letters:").lower())
        key_letter = input("Please enter key letter:").lower()
        letter_len = word_len(letters)
        if letter_len == 7 and key_letter in letters:
            valid_entry = True


    search_and_load.search(letters, key_letter)


if  __name__ == '__main__':
    main()