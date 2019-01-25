from TextAnalysislib.TextProcessing.AbstractTextProcessing import AbstractStemmer


def getStemmer(stemmer_name="porter", paramter_map={}):
    """
    This will provide the stemmer instances to all of the text processing tools.
    :param stemmer_name: name of the stemmer to be used.
    :type stemmer_name: string
    :param paramter_map: pass the paramters required for porter instances.
    :type paramter_map: dict
    :return: Stemmer's instance.
    :rtype: AbstractStemmer sub class
    """
    if stemmer_name is "porter":
        return PorterStemmer()
    return PorterStemmer()

class PorterStemmer(AbstractStemmer):
    def __init__(self):
        from nltk.stem import PorterStemmer
        self.stem = PorterStemmer()

    def stem(self, token_list):
        stem_list = []
        for token in token_list:
            stem_list.append(self.stem.stem(token))
        return stem_list