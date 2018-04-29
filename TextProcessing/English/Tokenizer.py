from TextProcessing.AbstractTextProcessing import AbstractTokenize
class StandfordTokenizer(AbstractTokenize):
    def __init__(self):
        from stanfordcorenlp import StanfordCoreNLP
        self.nlp = StanfordCoreNLP('/home/suraj/stanford-corenlp-full-2018-02-27')

    def tokenize(self,text):
        return self.nlp.word_tokenize(text)

#std = StandfordTokenizer()
#print(std.tokenize("test text"))