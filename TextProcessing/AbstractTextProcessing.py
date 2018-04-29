class AbstractExtractData:
    def extract(self,file_path):
        pass

class AbstractDecoder:
    def decode(self,text):
        pass

class AbstractTokenize:
    def tokenize(self,text):
        pass

class AbstractDocumentize:
    def documentize(self,text):
        pass

class AbstractNormalizeToken:
    def normalize_token(self, tokens_list):
        pass

class AbstractNormalizeList:
    def getNormalizeTokenList(self):
        pass

class AbstractStemmer:
    def stem(self,tokens_list):
        pass

class AbstractLemmatizer:
    def lemmatize(self,tokens_list):
        pass

class AbstractStopword:
    def getStopword(self):
        pass

class AbstractDiacriticAndAccent:
    def normalize(self, text):
        pass

class AbstractCaseFolding:
    def caseFold(self, text):
        pass

class AbstractPOSTags:
    def posTags(self,token_list):
        pass

""" 
It will take text as input and return the processed list of token, After all of the processing.
"""
class AbstractAnalyzer:
    def analyze(self, text):
        pass