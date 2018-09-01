def weight():
    return {
        'ADJ': {'ADP': 1, 'PRON': 5, 'VERB': 2, 'NOUN': 3, 'ADV': 2,
                'CONJ': 4, 'DET': 8, 'NUM': 7, 'PRT': 9, 'X': 4},
        'ADP': {'ADJ': 1, 'PRON': 5, 'VERB': 2, 'NOUN': 3, 'ADV': 2,
                'CONJ': 4, 'DET': 8, 'NUM': 7, 'PRT': 9, 'X': 4},
        'PRON': {'PRON': 2, 'ADP': 4, 'ADJ': 5, 'NOUN': 1, 'VERB': 1, 'ADV': 2,
                 'CONJ': 4, 'DET': 8, 'NUM': 7, 'PRT': 9, 'X': 4},
        'VERB': {'ADP': 4, 'PRON': 2, 'ADJ': 3, 'NOUN': 2, 'ADV': 3,
                 'CONJ': 4, 'DET': 8, 'NUM': 7, 'PRT': 9, 'X': 4},
        'NOUN': {'ADP': 1, 'PRON': 5, 'VERB': 4, 'ADJ': 2, 'ADV': 2,
                 'CONJ': 4, 'DET': 8, 'NUM': 7, 'PRT': 9, 'X': 4},
        'ADV': {'ADP': 1, 'PRON': 5, 'VERB': 4, 'NOUN': 2, 'ADJ': 2,
                'CONJ': 4, 'DET': 8, 'NUM': 7, 'PRT': 9, 'X': 4},
        'CONJ': {'ADP': 1, 'PRON': 5, 'VERB': 4, 'NOUN': 2, 'ADV': 2,
                 'ADJ': 4, 'DET': 8, 'NUM': 7, 'PRT': 9, 'X': 4},
        'DET': {'ADP': 1, 'PRON': 5, 'VERB': 4, 'NOUN': 2, 'ADV': 2,
                'CONJ': 4, 'ADJ': 8, 'NUM': 7, 'PRT': 9, 'X': 4},
        'NUM': {'ADP': 1, 'PRON': 5, 'VERB': 4, 'NOUN': 2, 'ADV': 2,
                'CONJ': 4, 'DET': 8, 'ADJ': 7, 'PRT': 9, 'X': 4},
        'PRT': {'ADP': 1, 'PRON': 5, 'VERB': 4, 'NOUN': 2, 'ADV': 2,
                'CONJ': 4, 'DET': 8, 'NUM': 7, 'ADJ': 9, 'X': 4},
        'X': {'ADP': 1, 'PRON': 5, 'VERB': 4, 'NOUN': 2, 'ADV': 2,
              'CONJ': 4, 'DET': 8, 'NUM': 7, 'PRT': 9, 'ADJ': 4}
            }


'''
VERB - verbs (all tenses and modes)
NOUN - nouns (common and proper)
PRON - pronouns
ADJ - adjectives
ADV - adverbs
ADP - adpositions (prepositions and postpositions)
CONJ - conjunctions
DET - determiners
NUM - cardinal numbers
PRT - particles or other function words
X - other: foreign words, typos, abbreviations
. - punctuation
'''