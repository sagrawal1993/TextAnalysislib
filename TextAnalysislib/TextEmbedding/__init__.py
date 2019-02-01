def getTextEmbedder(embedding_type="sklearn_countvector", parms={}):
    if embedding_type is "sklearn_countvector":
        from sklearn.feature_extraction.text import CountVectorizer
        return CountVectorizer(parms)
    elif embedding_type is "sklearn_hashingvector":
        from sklearn.feature_extraction.text import HashingVectorizer
        return HashingVectorizer(parms)
    elif embedding_type is "sklearn_tfidf_transformer":
        from sklearn.feature_extraction.text import TfidfTransformer
        return TfidfTransformer(parms)
    elif embedding_type is "sklearn_tfidf_vector":
        from sklearn.feature_extraction.text import TfidfVectorizer
        return TfidfVectorizer(parms)
    elif embedding_type is "word_embedding":
        from TextAnalysislib.TextEmbedding.embedding import Word2VecWordEmbedding
        return Word2VecWordEmbedding(parms)
    else:
        return None
