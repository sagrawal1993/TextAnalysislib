from TextAnalysislib.TextProcessing.English.Tokenizer import StandfordTokenizer, NltkTokenizer

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