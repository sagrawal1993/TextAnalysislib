from nltk.probability import FreqDist

def getBrownCorpus():
    from nltk.corpus import brown
    distro = FreqDist(brown.words())
    return distro