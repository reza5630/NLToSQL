from nltk.corpus import wordnet as wn


def sentence_similarity(attributes, query):

    synsets1=[]
    synsets2=[]

    for word in attributes:
        for syn in wn.synsets(word):
            synsets1.append( wn.synset(syn.name()))



    for word in query:
        for syn in wn.synsets(word):
            synsets2.append( wn.synset(syn.name()))

    score, count = 0.0, 0
    # For each word in the first sentence
    sims =[]
    for synset1 in synsets1:
        for synset2 in synsets2:
            x = synset2.wup_similarity(synset1)
            if x is not None:
                sims.append(x)
        if len(sims)>0:
            best_score = max(sims)
        else:
            best_score=0

        # Check that the similarity could have been computed
        score += best_score
        if score > 0:
            count += 1
    try:
        score /= count
        return score
    except ZeroDivisionError:
        return 0


def measure_similarity(sentence1, sentence2):
    return (sentence_similarity(sentence1, sentence2) + sentence_similarity(sentence2, sentence1)) / 2
