"""
Module will contains function which will take two text string as input and output the similarity between strings, using
different methods.

pip install Distance, this contains various method to calculate distance between various text string.

"""
from TextAnalysislib.TextProcessing.English.Stopwords import Stopword
from TextAnalysislib.TextProcessing import English

class CommonToken:
    """
    This will give the percent of tokens common between two strings.
    It will give the score on the scale of [0,1].

    >>tst = CommonToken()
    >>print(tst.similarity("my name is suraj agrawal", "nikhil agrawal is going to hoshiarpur."))
    >>0.14285714285714285

    """
    def __init__(self, toeknizer="nltk", stopwords=["nltk"], analyser=None):
        stopword = Stopword(stopwords)
        if analyser is not None:
            self.tokenize = analyser
        else:
            self.tokenize = English.getTokenizer(toeknizer).tokenize
        self.stopwords = set(stopword.getStopword())


    def similarity(self, string1, string2):
        string1_tokens = set(self.tokenize(string1)).difference(self.stopwords)
        string2_tokens = set(self.tokenize(string2)).difference(self.stopwords)

        common_tokens = string1_tokens.intersection(string2_tokens)
        total_tokens = string1_tokens.union(string2_tokens)
        if max(len(string2_tokens), len(string1_tokens)) == 0:
            return 0.0
        simmilarity = len(common_tokens)/len(total_tokens)
        return simmilarity



