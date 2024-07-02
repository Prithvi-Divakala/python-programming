# Function that takes a string s, representing a sentence,and returns a copy of the string with all punctuation removed.
def remove_punctuation(sentence: str):
    punctuation = ["'", ",", ".", "-", "_", "?", ";", ":"]
    sent_list = list(sentence)
    for i in punctuation:
        for j in sent_list:
            if i == j:
                sent_list.remove(j)
    return ''.join(sent_list)


print(remove_punctuation("Lets try, Mike."))
