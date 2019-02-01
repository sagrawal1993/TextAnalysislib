from TextAnalysislib.TextProcessing.AbstractTextProcessing import AbstractLemmatizer


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