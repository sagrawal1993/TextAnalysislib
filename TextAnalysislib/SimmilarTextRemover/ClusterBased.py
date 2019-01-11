
class ClusterBased():

    def __init__(self, embedding, clustering):
        self.embedding = embedding
        self.model = clustering

    def fit(self, doc_list):
        return []

    def _get_cluster_doc(self, doc_list):
        try:
            #vectorizer = TfidfVectorizer(stop_words='english')
            X = self.embedding.fit_transform(doc_list)
            true_k = 4
            if (len(doc_list)<true_k):
                true_k= max(len(doc_list)/2,1)
            #model = KMeans(n_clusters=true_k, init='k-means++', max_iter=100, n_init=1)
            self.model.fit(X)
            return list(self.model.labels_.tolist())
        except :
            return [0]*len(doc_list)