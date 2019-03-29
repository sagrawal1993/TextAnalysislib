from TextAnalysislib.TextProcessing.AbstractTextProcessing import AbstractAnalyzer
from TextAnalysislib.TextProcessing import English
import re

class POSTagToken(AbstractAnalyzer):
    """
    This Analyzer required pos tagger, which will return the list of (tag, word) list
    It also required list of tags regex which required to be include.

    >>test = English.getPOSTagger("spacy")
    >>ana = POSTagToken(test, ["NN*", "JJ*", "VB*"])
    >>print(ana.analyze("This is a test string. \n\nAnother string is also given along with it."))
    ['is', 'test', 'string', 'string', 'is', 'given']

    """

    def __init__(self, pos_tagger_name="nltk", tags_list=["NN*", "JJ*", "VB*"], pos_tagger=None):
        regex_string = ""
        for i, tag in enumerate(tags_list):
            regex_string += tag
            if i < len(tags_list)-1:
                regex_string += "|"
        #print(regex_string)
        self.rematch = re.compile(regex_string)
        if pos_tagger is not None:
            self.pos_tagger = pos_tagger
        else:
            self.pos_tagger = English.getPOSTagger(pos_tagger_name)

    def analyze(self, text):
        tag_token_list = self.pos_tagger.posTags(text)
        final_text_list = []
        for pair in tag_token_list:
            #print(pair)
            if self.rematch.match(pair[1]) != None:
                final_text_list.append(pair[0].lower())
        return final_text_list

