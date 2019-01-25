from TextAnalysislib.TextProcessing.AbstractTextProcessing import AbstractTokenize


def getTokenizer(tokenizer_name="nltk", param_map={}):
    """
    It will provide the tokenizer instance to get the token out of text.
    :param tokenizer_name: the tokenizer need to be used.
    :type tokenizer_name: string
    :param param_map: the parameter requires to instantiate the Tokenizer instance.
    :type param_map: dict
    :return: Tokenizer instance need to do tokenization.
    :rtype: AbstractTokenize
    """
    if tokenizer_name == "standford":
        return StandfordTokenizer()
    else:
        return NltkTokenizer()


class StandfordTokenizer(AbstractTokenize):
    def __init__(self):
        from stanfordcorenlp import StanfordCoreNLP
        self.nlp = StanfordCoreNLP('/home/suraj/stanford-corenlp-full-2018-02-27')

    def tokenize(self, text):
        return self.nlp.word_tokenize(text)


class NltkTokenizer(AbstractTokenize):

    def tokenize(self,text):
        from nltk import word_tokenize
        tokens = word_tokenize(text)
        return tokens

#std = StandfordTokenizer()
#print(std.tokenize("test text"))