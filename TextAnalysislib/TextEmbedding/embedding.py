from gensim.models import Word2Vec
from analysislib import clustering

class AbstractEmbedding:
    def fit(self, doc_list):
        pass

    def fit_transform(self, doc_list):
        pass

    def transform(self, doc_list):
        pass

class Word2VecWordEmbedding(AbstractEmbedding):

    def __init__(self, min_count, size, window, doc_embedding="centroid", tokenizer=None, stopword=None, preprocessor=None, analyzer=None, iter=300):
        print("Started Word2VecEmbedding.")
        self.doc_embedder = clustering.getClusterEmbeddingFromPoints(doc_embedding, {"dim": size})
        self.min_count = min_count
        self.size = size
        self.window = window
        self.iter = iter
        if tokenizer is None:
            from TextAnalysislib.TextProcessing import English
            tokenizer = English.getTokenizer("nltk")
            self.tokenizer = tokenizer.tokenize
        else:
            self.tokenizer = tokenizer
        if stopword is None:
            from TextAnalysislib.TextProcessing.English import Stopwords
            self.stopwords = Stopwords.Stopword().getStopword()
        else:
            self.stopwords = stopword
        self.preprocessor = preprocessor
        self.analyzer = analyzer

    def create_token_string(self, text):
        if self.analyzer is not None:
            return self.analyzer(text)
        if self.preprocessor is not None:
            text = self.preprocessor(text)
        token_list = self.tokenizer(text)
        final_token_list = []
        for token in token_list:
            if token not in self.stopwords:
                final_token_list.append(token)
        return final_token_list


    def fit(self, sentence_list=[], model_file=None):
        final_sentence_list = []
        for sentence in sentence_list:
            final_sentence_list.append(self.create_token_string(sentence))
        if model_file is None:
            self.model = Word2Vec(final_sentence_list, min_count=self.min_count, size=self.size, window=self.window, iter=self.iter)
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

    def get_doc_embedding(self, doc):
        word_vec_list = []
        word_list = self.create_token_string(doc)
        for word in word_list:
            if word in self.model.wv.vocab:
                word_vec_list.append(self.model[word])
        return self.doc_embedder.getClusterRepresentation(word_vec_list)

    def fit_transform(self, doc_list):
        self.fit(doc_list)
        return self.transform(doc_list)


    def transform(self, doc_list):
        doc_embedding_list = []
        for doc in doc_list:
            doc_embedding = self.get_doc_embedding(self.create_token_string(doc))
            doc_embedding_list.append(doc_embedding)
        return doc_embedding_list
