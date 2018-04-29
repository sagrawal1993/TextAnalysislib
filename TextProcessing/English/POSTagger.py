from TextProcessing.AbstractTextProcessing import AbstractPOSTags
class nltkTagger(AbstractPOSTags):

    def posTags(self,token_list):
        import nltk
        return nltk.pos_tag(token_list)