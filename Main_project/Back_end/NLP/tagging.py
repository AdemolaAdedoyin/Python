# from Back_end.NLP.ConsecutiveNPChunkTagger import ConsecutiveNPChunker
from nltk.tokenize import sent_tokenize,word_tokenize, wordpunct_tokenize
from nltk import ne_chunk,pos_tag
from nltk import FreqDist
# from nltk.corpus import conll2000
from nltk import WordNetLemmatizer, PorterStemmer


def tag_arrange(sent):
    sent = sent[:1].upper() + sent[1:] + "."
    toked_sentence = sent_tokenize(sent)
    toked_words = word_tokenize(toked_sentence[0])
    taged_words = pos_tag(toked_words)
    typed = ""
    universal_taged_words = pos_tag(toked_words, tagset="universal")
    if toked_words[0].lower() == "what" or toked_words[0].lower() == "where"\
            or toked_words[0].lower() == "who" \
            or toked_words[0].lower() == "when" or toked_words[0].lower() == "do" \
            or toked_words[0].lower() == "are" or toked_words[0].lower() == "can" \
            or toked_words[0].lower() == "how" or toked_words[0].lower() == "have":
        typed = "it is a question"
    tag = []
    for word, tagg in taged_words:
        tag.append(tagg)
    freq_dist = FreqDist(tag)
    most_common_fre_dist = freq_dist.most_common()
    lis = {}
    used_freq_dist = {}
    for i, y in most_common_fre_dist:
        lis[i] = y
        used_freq_dist[i] = y
    used_freq_dist = FreqDist(tag)
    for y, taggg in enumerate(tag):
        if taggg != ".":
            tag[y] = taggg + str((lis[taggg] - used_freq_dist[taggg]) + 1)
            used_freq_dist[taggg] = used_freq_dist[taggg] - 1

    not_arranged_universal_tag = []
    for word, tagg in universal_taged_words:
        not_arranged_universal_tag.append(tagg)

    universal_tag = []
    for word, tagg in universal_taged_words:
        universal_tag.append(tagg)
    freq_dist = FreqDist(universal_tag)
    most_common_fre_dist = freq_dist.most_common()
    lis = {}
    used_freq_dist = {}
    for i, y in most_common_fre_dist:
        lis[i] = y
        used_freq_dist[i] = y
    used_freq_dist = FreqDist(universal_tag)
    for y, taggg in enumerate(universal_tag):
        if taggg != ".":
            universal_tag[y] = taggg + str((lis[taggg] - used_freq_dist[taggg]) + 1)
            used_freq_dist[taggg] = used_freq_dist[taggg] - 1
    # stemming the words
    porter_stemmer = PorterStemmer()
    stemmed_tokens = [porter_stemmer.stem(token) for token in toked_words]
    # lamentizing the words
    lamentizer = WordNetLemmatizer()
    lemmatized_tokens = [lamentizer.lemmatize(token) for token in toked_words]

    # test_sents = conll2000.chunked_sents('test.txt')
    # train_sents = conll2000.chunked_sents('train.txt')
    # print(test_sents[:10])
    # chunker = ConsecutiveNPChunker(train_sents)
    # print(chunker.parse("I am feeling fine"))
    # print(chunker.evaluate(test_sents))

    return {'sentence':sent, 'toked_sentence':toked_sentence, 'words':toked_words, 'tag':tag, 'universal_tag':universal_tag,
            'not_arranged_universal_tag':not_arranged_universal_tag, 'type':typed}


sentence = "are you cold"
# print(tag_arrange(sentence)['sentence'])
# print(tag_arrange(sentence)['words'])
print(tag_arrange(sentence)['tag'])