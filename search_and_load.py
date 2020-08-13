def search(letters, key_letter):
    a = set()
    word_list = load_words()
    print(f"Total of {len(word_list)} words found.")
    count = 0
    for word in word_list:
        count = count + 1
        if len(word) > 3:
            print(f"Checking word {count} of {len(word_list)}. {get_pct(count,len(word_list))}%")
            dict_word_letters = list(word)
            step1 = True
            has_key_letter = False
            keep_checking = True
            for letter in dict_word_letters:
                while keep_checking:
                    if letter not in letters:
                        step1 = False
                        keep_checking = False
                    if letter == key_letter:
                        has_key_letter = True
                if step1 and has_key_letter:
                    a.add(word)

    result_write = open("out.txt","w")
    for word in a:
        result_write.write(word + "\n")
    result_write.close()



def get_pct(score, max):
    r = score / max
    r = r * 100
    r = int(r)
    return r


def load_words():
    with open("words.txt") as word_file:
        valid_words = set(word_file.read().split())
    return valid_words