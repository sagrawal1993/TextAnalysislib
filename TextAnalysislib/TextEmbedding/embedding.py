from gensim.models import Word2Vec
from analysislib.clustering import ClusterEmbedding
import numpy as np

class AbstractEmbedding:
    def fit(self, doc_list):
        pass

    def fit_transform(self, doc_list):
        pass

    def transform(self, doc_list):
        pass

class Word2VecWordEmbedding(AbstractEmbedding):

    def __init__(self, min_count, size, window, doc_embedding="centroid"):
        print("Started Word2VecEmbedding.")
        self.doc_embedder = ClusterEmbedding.getClusterEmbeddingFromPoints(doc_embedding)
        self.min_count = min_count
        self.size = size
        self.window = window

    def fit(self, sentence_list, model_file=None):

        if model_file is None:
            self.model = Word2Vec(sentence_list, min_count=self.min_count, size=self.size, window=self.window)
        else:
            self.model = Word2Vec.load(model_file)
        return

    def save_model(self, file_name):
        self.model.save(file_name)
        return

    def get_word_embedding(self, word):
        if word not in self.model.wv.vocab:
            return None
        return self.model[word]

    def get_doc_embedding(self, word_list):
        word_vec_list = []
        for word in word_list:
            if word in self.model.wv.vocab:
                word_vec_list.append(self.model[word])
        return self.doc_embedder.getClusterRepresentation(word_vec_list)

    def fit_transform(self, doc_list):
        self.model = Word2Vec(doc_list, min_count=self.min_count, size=self.size, window=self.window)
        return self.transform(doc_list)


    def transform(self, doc_list):
        doc_embedding_list = []
        for doc in doc_list:
            doc_embedding = self.get_doc_embedding(doc)
            doc_embedding_list.append(doc_embedding)
        return doc_embedding_list
