import string
words_file = open("words.txt")

words_set = set([line.rstrip().lower() for line in words_file.readlines()]) # set, ['trade', 'witch', 'ducat' ... emittance', 'ferromagnet', 'sluice']
                                                                            # Saw list comphrension on tik tok and I thought I
                                                                            # could use it here and it is so cool!!!

print(f"{len(words_set)} words in spelling words\n\n")

story_file = open("sawyer.txt")
for index, line in enumerate(story_file.readlines()):
    for word in line.split():
        word = word.lower()
        word = word.strip()
        word = word.rstrip(".,;")
        if word not in words_set:
            print(f"misspelled word on line {index + 1}:  {word}")