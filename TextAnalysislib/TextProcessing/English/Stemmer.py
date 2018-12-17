from TextAnalysislib.TextProcessing.AbstractTextProcessing import AbstractStemmer

class PorterStemmer(AbstractStemmer):
    def __init__(self):
        from nltk.stem import PorterStemmer
        self.stem = PorterStemmer()

    def stem(self, token_list):
        stem_list = []
        for token in token_list:
            stem_list.append(self.stem.stem(token))
        return stem_list