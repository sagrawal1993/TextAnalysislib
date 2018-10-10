from TopicExtraction.AbstractTopicExtraction import AbstractCandidateTopic

"""
This will cosider tokens which are Noun or NP as a candidate set.
"""
class NounOrNPAsCandidateTopic(AbstractCandidateTopic):
    def __init__(self, tokenizer, pos_tagger, tag_to_consider):
        self.pos_tagger = pos_tagger
        self.tokenizer = tokenizer
        self.tags = tag_to_consider

    def getCandidateTopic(self,doc_list):
        tag_word_map = {}
        for doc in doc_list:
            tokens = self.tokenizer.tokenize(doc)
            word_tag_list = self.pos_tagger.posTags(tokens)
            for word_tag in word_tag_list:
                if word_tag[1] not in tag_word_map:
                    tag_word_map[word_tag[1]] = []
                tag_word_map[word_tag[1]].append(word_tag[0])
            for key in tag_word_map:
                tag_word_map[key] = list(set(tag_word_map[key]))

        topics = []
        for tag in self.tags:
            if tag in tag_word_map:
                topics += tag_word_map[tag]
        return list(set(topics))