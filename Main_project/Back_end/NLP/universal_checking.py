from back_end_v2.DB import ASL_Db as A_DB, Database
from back_end_v2.DB import  ASL_Structure_DB
from nltk import WordNetLemmatizer, PorterStemmer



def universal_check(words, tag, universal_tag, not_arranged_universal_tag):
    value = ASL_Structure_DB.get_one_where(universal_tag)['ASL']
    gloss = ""
    supergloss = []
    [second_value] = [value.split()]
    for tag2 in second_value:
        for value, tag1, tag3, tag4 in zip(words, tag, universal_tag, not_arranged_universal_tag):
            # if value == "a":
            #     continue
            if value.lower() == "this":
                value = "ix-that"
            if tag2 == tag3:
                lamentizer = WordNetLemmatizer()
                lemmatized_tokens = lamentizer.lemmatize(value.lower(), pos='v')
                if lemmatized_tokens.lower() == "i":
                    lemmatized_tokens = "me"
                elif lemmatized_tokens.lower() == "n't":
                    lemmatized_tokens = "not"
                elif lemmatized_tokens.lower() == "'s":
                    lemmatized_tokens = "is"
                if value.lower() == "bit":
                    lemmatized_tokens = value
                supergloss.append((lemmatized_tokens, tag4))
                gloss += lemmatized_tokens + ","
    gloss = gloss.replace(",", " ").upper()
    gloss = gloss[:-1]
    value = []
    new_new_value = []
    rules = {'1': 'one', '2': 'two', '3':'three', '4':'four', '5':'five', '6':'six', '7':'seven',
             '8':'eight', '9':'nine'}
    change = []
    cou = 0
    for word, tag in supergloss:
        if word != ".":
            new_value = Database.get_one_where(word.capitalize(), tag)
            if new_value is None:
                if cou < len(gloss.split()):
                    change.append(cou)
                if word.isdigit():
                    new_value = "None"
                    for letter in word:
                        new_letter = rules[letter]
                        for letter in new_letter:
                            new_value = Database.get_one_where(letter.capitalize(), '.')
                            value.append(new_value)
                else:
                    for letter in word:
                        # print(letter)
                        if letter != "'":
                            new_value = Database.get_one_where(letter.capitalize(), '.')
                            value.append(new_value)
                new_new_value.append(value)
                value = []
            else: new_new_value.append(new_value)
        cou = cou + 1
    new_new_new_value = []
    for i in enumerate(new_new_value):
        a = 0
        if isinstance(new_new_value[i[0]], str):
            new_new_new_value.append(new_new_value[i[0]])
        else:
            while a < len(new_new_value[i[0]]):
                new_new_new_value.append(new_new_value[i[0]][a])
                a += 1
    value = " ".join(new_new_new_value)
    gloss = gloss.split()

    for y in change:
        # print(y)
        word1 = ""
        for i, word in enumerate(gloss):
            if i == y:
                if word[:1] == "'":
                    word = word[1:]
                for i in word:
                    word1 += i + "-"
            # print(word1[:-1])
        gloss[y] = word1[:-1]
    gloss = "  ".join(gloss)
    # gloss = str(gloss).replace(",", " ").upper()

    return {'value':value, 'gloss':gloss}

