from TextAnalysislib.TextProcessing.AbstractTextProcessing import AbstractAnalyzer
import re

class POSTagToken(AbstractAnalyzer):
    """
    This Analyzer required pos tagger, which will return the list of (tag, word) list
    It also required list of tags regex which required to be include.

    """
    def __init__(self, pos_tagger, tags_list):
        regex_string = ""
        for i, tag in enumerate(tags_list):
            regex_string += tag
            if i < len(tags_list)-1:
                regex_string += "|"
        self.rematch = re.compile(regex_string)
        self.pos_tagger = pos_tagger

    def analyze(self, text):
        tag_token_list = self.pos_tagger.posTags(text)
        final_text_list = []
        for pair in tag_token_list:
            if self.rematch.match(pair[0]) != None:
                final_text_list.append(pair[1])
        return final_text_list