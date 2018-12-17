from TextAnalysislib.TopicExtraction.AbstractTopicExtraction import AbstractCandidateTopicScore
from nltk import FreqDist

class FreqBased(AbstractCandidateTopicScore):
    def __init__(self,doc_list,tokenizer):
        self.doc_list = doc_list
        self.tokenizer = tokenizer
        tokens = []
        for doc in doc_list:
            tokens += self.tokenizer.tokenize(doc)
        self.freqDist = FreqDist(tokens)

    def getCandidateTopicScore(self,topic_list):
        limitDist = FreqDist()
        for topic in topic_list:
            if topic in self.freqDist:
                limitDist[topic] = self.freqDist[topic]
            else:
                limitDist[topic] = 0
        return limitDist.most_common(100)