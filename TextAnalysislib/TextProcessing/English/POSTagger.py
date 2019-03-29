from TextAnalysislib.TextProcessing.AbstractTextProcessing import AbstractPOSTags

class nltkTagger(AbstractPOSTags):

    def posTags(self, text):
        import nltk
        token_list = nltk.tokenize.word_tokenize(text,'en')
        return nltk.pos_tag(token_list)

#standford tagger takes whole text as a string.
class standfordTagger(AbstractPOSTags):

    def __init__(self):
        from stanfordcorenlp import StanfordCoreNLP
        self.nlp = StanfordCoreNLP('/home/suraj/stanford-corenlp-full-2018-10-05')

    def posTags(self, text):
        token_tag = self.nlp.pos_tag(text)
        return token_tag

class spacyTagger(AbstractPOSTags):
    """
    This pos tagger will use spacy to get the POS tag from the text.
    """
    def __init__(self):
        import spacy
        self.nlp = spacy.load('en')

    def posTags(self, text):
        doc = self.nlp(text)
        tag_list = []
        for token in doc:
            tag_list.append((token.text, token.tag_))
        return tag_list

"""
test = standfordTagger()
test = spacyTagger()
print(test.posTags("This is a test string. \n\nAnother string is also given along with it."))
# #print(test.posTags(["this", "is", "a", "test string"]))
"""
