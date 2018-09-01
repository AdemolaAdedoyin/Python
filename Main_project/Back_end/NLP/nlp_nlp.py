from NLP.tagging import tag_arrange
import nltk
from nltk import WordNetLemmatizer, PorterStemmer
from NLP.weights import weight
from NLP.checking_for_sentence import checking
from NLP.universal_checking import universal_check
from back_end_v2.DB import  English_Db as DB
from back_end_v2.DB import ASL_Db as A_DB, Database
from back_end_v2.DB import  ASL_Structure_DB
from NLP.distance_checker import similar, levenshteinDistance, iterative_levenshtein


def thesis(sent):
    # print(sent)
    toked_sentence = tag_arrange(sent)['toked_sentence']

    if DB.get_sentence_where(toked_sentence[0]) is not None:
        step = "I found a full sentence"
        # print(DB.get_sentence_where(toked_sentence[0])['linked_to'])
        val = DB.get_sentence_where(toked_sentence[0])['linked_to']
        value = A_DB.get_one_where(val)['url']
        gloss = A_DB.get_one_where(val)['Sentence']

    elif DB.get_sentence_where(toked_sentence[0]) is None:
        tag = tag_arrange(sent)['tag']
        typed = tag_arrange(sent)['type']
        # print(tag)
        universal_tag = tag_arrange(sent)['universal_tag']
        not_arranged_universal_tag = tag_arrange(sent)['not_arranged_universal_tag']
        words = tag_arrange(sent)['words']
        if DB.get_tag_where(tag) is not None:
            step = "I found a natural tag"
            value = checking(words, tag, universal_tag, not_arranged_universal_tag)['value']
            gloss = checking(words, tag, universal_tag, not_arranged_universal_tag)['gloss']
            if typed == "it is a question":
                gloss = gloss[:-1]
                gloss = gloss + "?"

        elif ASL_Structure_DB.get_one_where(universal_tag) is not None:
            step = "I found a universal tag"
            value = universal_check(words, tag, universal_tag, not_arranged_universal_tag)['value']
            gloss = universal_check(words, tag, universal_tag, not_arranged_universal_tag)['gloss']
            if typed == "it is a question":
                gloss = gloss[:-1]
                gloss = gloss + "?"
        else:
            step = "I had to use weights to swap positions"
            lowest = 0
            lowest1 = 0
            id1 = 0
            id2 = 0
            main_lowest = 0
            main_lowest1 = 100
            for id,eng,asl in ASL_Structure_DB.getAll():
                lowest = similar(str(universal_tag), str(eng))
                if lowest > main_lowest and not (lowest > 1):
                    main_lowest = lowest
                    id1 = id
                lowest1 = levenshteinDistance(str(universal_tag), str(eng))
                # lowest1 = nltk.edit_distance(str(universal_tag), str(eng))
                if lowest1 < main_lowest1:
                    main_lowest1 = lowest1
                    id2 = id
            a = ASL_Structure_DB.get_one_where_id(id1)
            b = ASL_Structure_DB.get_one_where_id(id2)
            print(str("sentence sent from the system is " + toked_sentence[0]))
            print(str("Tag for the sentence sent from system is " + str(universal_tag)))
            print(str("English sentence in database matching is " + b['English']))
            print(str("ASL sentence in database is " + b['ASL']))
            r = {}
            [second_value] = [b['ASL'].split()]
            for i, tag1 in enumerate(second_value):
                r[i] = "None"
                for tag2 in universal_tag:
                    if tag1 == tag2:
                        r[i] = tag2
            # print(r)
            total = 0
            for i in r:
                if r[i] == 'None':
                    lowest = 100
                    second_lowest = 100
                    val = ""
                    new_we = weight()[second_value[i][:-1]]
                    for tag in universal_tag:
                        for a in new_we:
                            if tag[:-1] == a:
                                # if tag.endswith(second_value[i][-1:]):
                                    new_lowest = new_we[tag[:-1]]
                                    if new_lowest < lowest:
                                        lowest = new_lowest
                                        val = tag
                    # for a in new_we:
                    #     for tag in universal_tag:
                    #         if tag[:-1] == a:
                    #             # if tag.endswith(second_value[i][-1:]):
                    #                 new_lowest = new_we[tag[:-1]]
                    #                 if new_lowest < lowest:
                    #                     lowest = new_lowest
                    #                     val = tag
                    print("What i had to swap " + str(second_value[i]))
                    print("What i had to swap it with " + str(val))
                    a = 1
                    count = 0
                    # print(val)
                    while count == 0:
                        # print(val)
                        if val in r.values():
                            count = 0
                            w = (val[-1:])
                            b = int(w) + a
                            val = str(val[:-1] + str(b))
                        elif val not in r.values():
                            count = 1
                            val = val

                    # print(val)
                    r[i] = val
                    total = total + lowest
            # print(total)
            # print(r)
            if total < 2:
                gloss = ""
                supergloss = []
                for i in r:
                    for tag, words1 in zip(universal_tag, words):
                        if tag == r[i]:
                            lamentizer = WordNetLemmatizer()
                            lemmatized_tokens = lamentizer.lemmatize(words1.lower(), pos='v')
                            if lemmatized_tokens.lower() == "i":
                                lemmatized_tokens = "me"
                            elif lemmatized_tokens.lower() == "n't":
                                lemmatized_tokens = "not"
                            elif lemmatized_tokens.lower() == "'s":
                                lemmatized_tokens = "is"
                            elif lemmatized_tokens.lower() == "bear":
                                lemmatized_tokens = "born"
                            supergloss.append((lemmatized_tokens, tag[:-1]))
                            words1 = lemmatized_tokens
                            gloss += words1 + ","
                gloss = gloss.replace(",", " ").upper()
                gloss = gloss[:-1]
                change = []
                cou = 0
                value = []
                new_new_value = []
                rules = {'1': 'one', '2': 'two', '3': 'three', '4': 'four', '5': 'five', '6': 'six', '7': 'seven',
                         '8': 'eight', '9': 'nine'}
                for word, tag in supergloss:
                    if word != "." and word != ",":
                        if word.isdigit():
                            lamentizer = WordNetLemmatizer()
                            lemmatized_tokens = lamentizer.lemmatize(word.lower(), pos='v')
                            word = lemmatized_tokens
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
                                    if letter != "'":
                                        new_value = Database.get_one_where(letter.capitalize(), '.')
                                        value.append(new_value)
                                        # print(word)
                                        # print(value)
                            new_new_value.append(value)
                            # print(new_new_value)
                            value = []
                        else:
                            new_new_value.append(new_value)
                    cou = cou + 1
                # print(new_new_value)
                new_new_new_value = []

                for i in enumerate(new_new_value):
                    a = 0
                    if isinstance(new_new_value[i[0]], str):
                        new_new_new_value.append(new_new_value[i[0]])
                    else:
                        while a < len(new_new_value[i[0]]):
                            new_new_new_value.append(new_new_value[i[0]][a])
                            a += 1
                    # print(new_new_new_value)
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
            else:
                step = "I used weights but it was too much adjustment"
                gloss = sent.upper()
                rules = {'1': 'one', '2': 'two', '3': 'three', '4': 'four', '5': 'five', '6': 'six', '7': 'seven',
                         '8': 'eight', '9': 'nine'}
                value = ""
                for letter in gloss:
                    # print(letter)
                    if letter != "." and letter != " ":
                        if letter.isdigit():
                            new_letter = rules[letter]
                            for letter1 in new_letter:
                                new_value = Database.get_one_where(letter1.capitalize(), '.')
                                value += new_value + " "
                            # continue
                        else:
                            # print(letter)
                            new_value = Database.get_one_where(letter.capitalize(), '.')
                            # print(new_value)
                            value += new_value + " "
                value = value[:-1]
                # print(value)

    else:
        value = None
        gloss = None
        step = None
    # print(value)
    return {'value': value, 'gloss': gloss, 'step': step}


sentence = "what are we doing tomorrow night"
# print(thesis(sentence))

