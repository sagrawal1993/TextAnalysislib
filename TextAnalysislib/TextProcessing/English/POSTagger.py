from TextAnalysislib.TextProcessing.AbstractTextProcessing import AbstractPOSTags

def getPOSTagger(pos_tagger="nltk", param_map={}):
    """
    give the POSTagger instance to POSTag the token list.
    :param pos_tagger: name of the postagger to be used.
    :type pos_tagger: string
    :param param_map: paramters requires to instantiate the param_map
    :type param_map: dict
    :return: POSTagger instance
    :rtype: AbstractPOSTags
    """
    if pos_tagger == "standford":
        return standfordTagger()
    return nltkTagger()


class nltkTagger(AbstractPOSTags):

    def posTags(self, token_list):
        import nltk
        return nltk.pos_tag(token_list)

#standford tagger takes whole text as a string.
class standfordTagger(AbstractPOSTags):

    def __init__(self):
        from stanfordcorenlp import StanfordCoreNLP
        self.nlp = StanfordCoreNLP('/home/suraj/stanford-corenlp-full-2018-02-27')

    def posTags(self, text):
        token_tag = self.nlp.pos_tag(text)
        return token_tag


# test = standfordTagger()
# #test = nltkTagger()
# print(test.posTags("This is a test string. \n\nAnother string is also given along with it."))
# #print(test.posTags(["this", "is", "a", "test string"]))