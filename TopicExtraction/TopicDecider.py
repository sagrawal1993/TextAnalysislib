from TopicExtraction.AbstractTopicExtraction import AbstractTopicDecider
class BasedOnBound(AbstractTopicDecider):
    def getTopicsList(self, topic_coverage_list, topic_list, parm):
        doc_topic_list = []
        for topic_coverage in topic_coverage_list:
            tp_lst = []
            for i in range(len(topic_coverage)):
                if topic_coverage[i]>parm:
                    tp_lst.append(topic_list[i])
            doc_topic_list.append(tp_lst)
        return doc_topic_list