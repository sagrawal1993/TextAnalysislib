from TextAnalysislib.TopicExtraction.AbstractTopicExtraction import AbstractFindTopicList
from nltk import FreqDist

class HighFrequency(AbstractFindTopicList):
    def __init__(self, analyzer=None, n_gram_boost_map={}):
        self.analyzer = analyzer
        self.n_gram_boost_map = n_gram_boost_map

    def getTopicList(self, doc_list, parm):
        from sklearn.feature_extraction.text import CountVectorizer
        if self.analyzer==None:
            print("No custom Analyser given")
            self.vectorizer = CountVectorizer(ngram_range=(1, 3), lowercase=True,
                                                  stop_words='english')
            self.analyzer = self.vectorizer.build_analyzer()
        All_token_list = []
        for doc in doc_list:
            token_list = self.analyzer(doc)
            All_token_list += token_list
        freqDist = FreqDist(All_token_list)
        freqDist = self.__get_boosted_freq(freqDist)
        return freqDist.most_common(parm)

    def __get_boosted_freq(self, freqDist):
        for token in freqDist:
            ngram_size = len(token.split(" "))
            if ngram_size in self.n_gram_boost_map:
                freqDist[token] *= self.n_gram_boost_map[ngram_size]
        return freqDist


    def get_filter_topic(self, freq_dist):
        curr_map = {}
        for key, value in freq_dist:
            curr_map[key] = value

        query_map = {}
        curr_set = list(curr_map.keys())
        while len(curr_set) > 0:
            key = curr_set[0]
            value = 0.0
            q_set = curr_map.keys()
            keys_to_delete = []
            for query in q_set:
                current_set = set(key.split(" "))
                prev_query = set(query.split(" "))
                if len(prev_query.intersection(current_set)) == len(prev_query):
                    value = curr_map[query] + value
                    keys_to_delete.append(query)
                elif len(current_set.intersection(prev_query)) == len(current_set):
                    key = query
                    value = curr_map[query] + value
                    keys_to_delete.append(query)
            query_map[key] = value
            for k in keys_to_delete:
               del curr_map[k]
            curr_set = list(curr_map.keys())
        return query_map


class AssociationRuleBased(AbstractFindTopicList):
    def __init__(self, analyzer=None, n_gram_boost_map={}):
        self.analyzer = analyzer
        self.n_gram_boost_map = n_gram_boost_map

    def getTopicList(self, doc_list, parm):
        from sklearn.feature_extraction.text import CountVectorizer
        from analysislib.datamining import AssociationRuleMining

        self.rule_miner = AssociationRuleMining.getAssociationRuleMiner("aprior")
        if self.analyzer==None:
            print("No custom Analyser given")
            self.vectorizer = CountVectorizer(lowercase=True,
                                                  stop_words='english')
            self.analyzer = self.vectorizer.build_analyzer()
        tokenize_doc_list = []
        for doc in doc_list:
            token_list = self.analyzer(doc)
            tokenize_doc_list.append(token_list)
        associatoin_rules = self.rule_miner.getRule(tokenize_doc_list)
        return self.__get_filter_topic_from_rule(associatoin_rules)

    def __get_filter_topic_from_rule(self, association_rules):
        topic_list = []
        for item in association_rules:
            topic_list.append(str(item[0]))
        return topic_list


"""class TfIdfBased(AbstractFindTopicList):

    def getTopicList(self,doc_list,parm):
        from sklearn.feature_extraction.text import Tf
"""