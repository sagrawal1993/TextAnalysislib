from TextAnalysislib.TextProcessing.AbstractTextProcessing import AbstractLemmatizer


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
    return WordNet()

#word net also take postag along with tokens that will give different result.
class WordNet(AbstractLemmatizer):
    def __init__(self):
        from nltk.stem import WordNetLemmatizer
        self.wordnet = WordNetLemmatizer()

    def lemmatize(self, tokens_list):
        lemma_list = []
        flag = True
        for token in tokens_list:
            if len(token)!=2:
                flag = False
                break

        if flag:
            for token in tokens_list:
                try:
                    print(token)
                    lemma_list.append(self.wordnet.lemmatize(token[0],token[1]))
                except:
                    lemma_list.append(token[0])
        else:
            for token in tokens_list:
                try:
                    lemma_list.append(self.wordnet.lemmatize(token))
                except:
                    lemma_list.append(token)
        return lemma_list