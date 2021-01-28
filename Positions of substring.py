def gettingFirstAndLastIndexesOfChars(text, word):
    def act_with_text_parts(text_part):
        for char in text_part:
            if word[0] == char and word[1] == text_part[text_part.index(char) + 1]:
                return text_part.index(char)

    text_first_part = text[:len(text) // 2]
    text_second_part = text[len(text) // 2:]
    return act_with_text_parts(text_first_part), \
           act_with_text_parts(text_second_part) + len(text_first_part)


text = "it is fruit"
word = "it"

print(gettingFirstAndLastIndexesOfChars(text, word))

# print(text.find(word))
# print(text.rfind(word))
