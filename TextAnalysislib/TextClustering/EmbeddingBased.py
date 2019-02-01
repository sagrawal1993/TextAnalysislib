class TextEmbeddingBased:
    """
    Take the embedding for encoding the text and clustering algorithm to user and will return the list of doc with cluster_ids.

    """
    def __init__(self, embedding=None, clustering=None):
        if embedding is None:
            from TextAnalysislib import TextEmbedding
            self.__embedding = TextEmbedding.getTextEmbedder()
        else:
            self.__embedding = embedding

        if clustering is None:
            from analysislib import clustering
            self.__clustering = clustering.getClustering()
        else:
            self.__clustering = clustering

    def fit(self, doc_list):
        self.vector_list = self.__embedding.fit_transform(doc_list)
        self.__clustering.fit(self.vector_list)
        self.label = self.__clustering.labels_

    def cluster_scores(self):
        cluster_index_map = {}
        cluster_score_map = {}
        for i, cluster_id in enumerate(self.label):
            if cluster_id not in cluster_index_map:
                cluster_index_map[cluster_id] = []
            cluster_index_map[cluster_id].append(i)

        from analysislib.clustering import ClusterRepresentative
        from scipy.spatial import distance
        for cluster_id in cluster_index_map:
            vector_list = [self.vector_list[i] for i in cluster_index_map[cluster_id]]
            index_score_list = ClusterRepresentative.closer_to_centroid(vector_list, distance.euclidean)
            for tuple in index_score_list:
                tuple[1] = cluster_index_map[cluster_id][tuple[1]]
            cluster_score_map[cluster_id] = index_score_list
        return cluster_score_map
