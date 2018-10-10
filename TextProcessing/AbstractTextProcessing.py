#Extract text data from different format of file.
class AbstractExtractData:
    def extract(self,file_path):
        pass

#Decode the data in on format so that it can be processed.
class AbstractDecoder:
    def decode(self,text):
        pass

#Break the text into tokens.
class AbstractTokenize:
    def tokenize(self,text):
        pass

#Define the technique to break the text into list of documents that will be index as one document.
class AbstractDocumentize:
    def documentize(self,text):
        pass

#It define the heuristic or rule based approach to map token to the equivanlance class of tokens.
class AbstractNormalizeToken:
    def normalize_token(self, tokens_list):
        pass

#It will provide the list to tokens corresponds to a token that can be given as the recommendation for that word.
class AbstractNormalizeList:
    def getNormalizeTokenList(self):
        pass

#Stemmer to map similar word to same tokens. Use heuristics to get this.
class AbstractStemmer:
    def stem(self,tokens_list):
        pass

#It is a well defined mechanism to map word to its root word. wordnet is an exammple of it.
class AbstractLemmatizer:
    def lemmatize(self,tokens_list):
        pass

#It define different schema to define the stopwords for text
class AbstractStopword:
    def getStopword(self):
        pass

#Normalize words from different accent and diacritics.
class AbstractDiacriticAndAccent:
    def normalize(self, text):
        pass

#Define different mechanism to change casing of the alphabets into english.
class AbstractCaseFolding:
    def caseFold(self, text):
        pass

#this will provide part of speech tags for each tokens.
class AbstractPOSTags:
    def posTags(self,token_list):
        pass

#this will provide syntactic parsing tree for the sentences.
class AbstractParser:
    def parse(self,text):
        pass

""" 
It will take text as input and return the processed list of token, After all of the processing.
"""
class AbstractAnalyzer:
    def analyze(self, text):
        pass