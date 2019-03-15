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

def getLemmatizer(lemmatizer_name = "wordnet", parm_map={}):
    """
    It will provide the lemmatizer .
    :param lemmatizer_name: name of the lemmatizer, for which the instance need to be created.
    :type lemmatizer_name: string
    :param parm_map: parameters required for instantiating Lemmatizer.
    :type parm_map: dict
    :return: Instance of Lemmatizer.
    :rtype: AbstractLemmatizer
    """
    from TextAnalysislib.TextProcessing.English import Lemmatizer
    return Lemmatizer.WordNet()



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
    from TextAnalysislib.TextProcessing.English import POSTagger
    if pos_tagger == "standford":
        return POSTagger.standfordTagger()
    return POSTagger.nltkTagger()



def getStemmer(stemmer_name="porter", paramter_map={}):
    """
    This will provide the stemmer instances to all of the text processing tools.
    :param stemmer_name: name of the stemmer to be used.
    :type stemmer_name: string
    :param paramter_map: pass the paramters required for porter instances.
    :type paramter_map: dict
    :return: Stemmer's instance.
    :rtype: AbstractStemmer sub class
    """
    from TextAnalysislib.TextProcessing.English import Stemmer
    if stemmer_name is "porter":
        return Stemmer.PorterStemmer()
    return Stemmer.PorterStemmer()

def getAnalyser(analyser_name="tag_token", parameter_map={}):
    """

    :param analyser_name: name of the analyser, whose instance required to process.
    :type analyser_name: String.
    :param parameter_map: parameters required by the analyser.
    :type parameter_map: dict
    :return: object of type anlayzer.
    :rtype: Analyser
    """
    if analyser_name == "tag_token":
        from TextAnalysislib.TextProcessing.English.Analyser import POSTagToken
        return POSTagToken(**parameter_map)
    return None