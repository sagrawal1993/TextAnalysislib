from AbstractTopicExtraction import AbstractFindTopicList
from nltk import FreqDist

class HighFrequency(AbstractFindTopicList):
    def __init__(self,analyzer=None ):
        self.analyzer = analyzer

    def getTopicList(self,doc_list,parm):
        from sklearn.feature_extraction.text import CountVectorizer
        if self.analyzer==None:
            print("No custom Analyser given")
            self.vectorizer = CountVectorizer(ngram_range=(1, 4), lowercase=True,
                                                  stop_words='english')
            self.analyzer = self.vectorizer.build_analyzer()
        All_token_list = []
        for doc in doc_list:
            token_list = self.analyzer(doc)
            All_token_list += token_list
        freqDist = FreqDist(All_token_list)
        return freqDist.most_common(parm)

"""class TfIdfBased(AbstractFindTopicList):

    def getTopicList(self,doc_list,parm):
        from sklearn.feature_extraction.text import Tf
"""