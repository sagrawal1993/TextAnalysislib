from sklearn.feature_extraction.text import CountVectorizer
from TextAnalysislib.TopicExtraction.AbstractTopicExtraction import AbstractExtractTopic


class TermAsTopic(AbstractExtractTopic):
    def __init__(self, analyzer=None):
        self.analyzer = analyzer
        print("Started TermAsTopic")

    def getTopicCoverage(self,doc_list, topics_list):
        self.topic_list = topics_list
        feature_map = {}
        for i in range(len(topics_list)):
            feature_map[topics_list[i].lower()] = i
        self.feature = feature_map
        if self.analyzer==None:
            print("No custom Analyser given")
            self.vectorizer = CountVectorizer(ngram_range=(1, 4), lowercase=True,
                                                  stop_words='english', vocabulary=self.feature)
        else:
            self.vectorizer = CountVectorizer(ngram_range=(1, 4), lowercase=True,
                                                  stop_words='english', vocabulary=self.feature, analyzer=self.analyzer)
        vectors = self.vectorizer.transform(doc_list).toarray()
        output = []
        for vector in vectors:
            if sum(vector)==0:
                output.append(vector)
                continue
            output.append(vector/float(sum(vector)))
        return output

    def getDebugInfo(self, doc):
        vector = self.vectorizer.transform([doc]).toarray()[0]
        term_count = {}
        for i in range(len(self.feature)):
            term_count[self.topic_list[i]] = vector[i]
        return term_count