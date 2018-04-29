import json

from TopicExtraction import Measure
from TopicExtraction.TermAsTopic import TermAsTopic
from TopicExtraction.TopicDecider import BasedOnBound
from TopicExtraction.FindTopicList import HighFrequency
from AbstractProject import AbstractProject


candMap = json.load(open("ContextualSuggestion/placeToTagCandidatesOnly.json"))
textMap = json.load(open("ContextualSuggestion/test.json"))
annoted_topic_map = {}
for key in textMap.keys():
    annoted_topic_map[key]= candMap[key]

class ContexualSuggestionTopicExtraction(AbstractProject):
    def __init__(self):
        allKey = []
        for key in candMap:
            allKey += candMap[key]
        self.topics = list(set(allKey))
        self.termTopic = TermAsTopic()
        self.topicDecider = BasedOnBound()
        self.name = "ContextualTopic"
        #print(len(candMap.keys()),len(textMap.keys()))

    def get_meta_info(self):
        meta_info = {}
        meta_info['topics'] = self.topics
        meta_info['starting_id'] = 0
        meta_info['ending_id'] = len(annoted_topic_map)
        meta_info['measure'] = self.find_measure_value()
        return meta_info

    def find_measure_value(self):
        self.topicCoveragelist = self.termTopic.getTopicCoverage(textMap.values(), self.topics)
        self.topicList = self.topicDecider.getTopicsList(self.topicCoveragelist, self.topics, 0.01)
        measure = Measure.prec_recall(annoted_topic_map.values(), self.topicList)
        return measure

    def get_doc_info(self,id):
        doc_info = {}
        id = int(id)
        if id<len(textMap):
            doc_info['debug'] = self.termTopic.getDebugInfo(textMap.values()[id])
            doc_info['text'] = textMap.values()[id]
            doc_info['topic_coverage'] = self.topicCoveragelist[id].tolist()
            doc_info['extracted_topic'] = self.topicList[id]
            doc_info['actual_topic'] = annoted_topic_map.values()[id]
        return doc_info

    def find_high_freq_topic(self):
        hfreq_topic = HighFrequency()
        topic_list = hfreq_topic.getTopicList(textMap.values(),1000)
        return topic_list
#cc = ContexualSuggestionTopicExtraction()
#print(cc.get_meta_info())
#print(cc.get_doc_info(0))