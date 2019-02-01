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
    """
    def __init__(self, toeknizer="nltk", stopwords=["nltk"]):
        stopword = Stopword(stopwords)
        self.stopwords = set(stopword.getStopword())
        self.tokenizer = English.getTokenizer(toeknizer)

    def similarity(self, string1, string2):
        string1_tokens = set(self.tokenizer.tokenize(string1)).difference(self.stopwords)
        string2_tokens = set(self.tokenizer.tokenize(string2)).difference(self.stopwords)

        common_tokens = string1_tokens.intersection(string2_tokens)
        if min(len(string2_tokens), len(string1_tokens)) == 0:
            return 0.0
        simmilarity = len(common_tokens)/min(len(string2_tokens), len(string1_tokens))
        return simmilarity


# tst = CommonToken()
# print(tst.similarity("my name is suraj agrawal", "nikhil agrawal is going to hoshiarpur."))
