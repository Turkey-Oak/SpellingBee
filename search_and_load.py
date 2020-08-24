import time


def search(letters, key_letter, wordlist):
    a = set()
    word_list = load_words(wordlist)
    print(f"Total of {len(word_list)} words found.")
    count = 0
    st = 0
    st = time.perf_counter()
    for word in word_list:
        count = count + 1
        if len(word) > 3:
            print(f"Checking word {count} of {len(word_list)}. {get_pct(count, len(word_list))}%")

            dict_word_letters = list(word)
            step1 = True
            has_key_letter = False
            keep_checking = True
            for letter in dict_word_letters:

                if letter not in letters:
                    step1 = False
                    break

                if letter == key_letter:
                    has_key_letter = True

                if step1 and has_key_letter:
                    a.add(word)

    result_write = open("out.txt", "w")
    for word in a:
        result_write.write(word + "\n")
    result_write.close()
    end = time.perf_counter()
    print(f"Checked in {end - st:0.4f} seconds")


def get_pct(score, max):
    r = score / max
    r = r * 100
    r = int(r)
    return r


def load_words(wordlist):
    with open(wordlist) as word_file:
        valid_words = set(word_file.read().split())
    return valid_words
