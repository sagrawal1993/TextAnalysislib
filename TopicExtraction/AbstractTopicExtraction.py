
"""
this class will figure out Topics present in the document collection.
Parameter will denote number of topics/ or other parameters to limit topic list.
"""
class AbstractFindTopicList:
    def getTopicList(self,doc_list,parm):
        pass

class AbstractCandidateTopic:
    def getCandidateTopic(self,doc_list):
        pass

class AbstractCandidateTopicScore:
    #Return map along with score of topics into corpus.
    def getCandidateTopicScore(self,topic_list):
        pass

#Return topic list with top score and remove redundancy.
class AbstractPickTopTopic:
    def getTopTopic(self,topic_score_map,param):
        pass

"""
This class will extract the topics from the given document collection.
The topic list is being passed as an argument.
Topic extraction will return the coverage of topic in each document.
"""
class AbstractExtractTopic:
    #Return the coverage of each topic inside document.
    def getTopicCoverage(self,doc_list, topic_list):
        pass


"""
This class will extract topic given the document along with topics present inside the documents.

"""
class AbstractDocTopicMapping:
    #provide the text of doc along with topics/Keywords names
    def fit(self,X,Y):
        pass

    #Return Topic Names for the topics.
    def transform(self,X):
        pass


"""
This class will define the criteria to select the topic based on it's coverage
inside document.
Parameter and topic list is being passed as an argument.
Cosider topic list to be in same order given the coverage for each doc.
"""
class AbstractTopicDecider:
    def getTopicsList(self, topic_coverage_list, topic_list, parm):
        pass