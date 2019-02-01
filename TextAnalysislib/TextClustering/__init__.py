"""
This module will give the text clustering methods.
"""

def getTextCluster(method_name="embedding_based", params={}):
    if method_name is "embedding_based":
        from TextAnalysislib.TextClustering.EmbeddingBased import TextEmbeddingBased
        return TextEmbeddingBased()
    return None

