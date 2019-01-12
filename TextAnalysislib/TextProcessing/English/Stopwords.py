from TextAnalysislib.TextProcessing.AbstractTextProcessing import AbstractStopword

def load_stopword(file_name):
    stopword_list = open("StopwordFile/" + file_name).read().strip().split("\n")
    return stopword_list

def get_stopword_list(type_name):   
    if type_name == "nltk":
        stopwords = getNltkStopword()
    elif type_name == "sklearn":
        stopwords = getSklearnStopword()
    elif type_name == "spacy":
        stopwords = getSpacyStopword()
    elif type_name == "yoast":
        stopwords = getYoastStopword()
    elif type_name == "humbolt":
        stopwords = getHumboltStopword()
    elif type_name == "googlehistory":
        stopwords = load_stopword("GoogleHistory")
    elif type_name == "sql":
        stopwords = load_stopword("SQLStopword")
    elif type_name == "longlist":
        stopwords = load_stopword("LongStopword")
    else:
        stopwords = load_stopword("DefaultEnglish")
    return list(set(stopwords))

def getNltkStopword():
    from nltk.corpus import stopwords
    stop_words = set(stopwords.words('english'))
    return list(stop_words)


def getSklearnStopword():
    from sklearn.feature_extraction.stop_words import ENGLISH_STOP_WORDS
    return ENGLISH_STOP_WORDS

def getSpacyStopword():
    from spacy.lang.en.stop_words import STOP_WORDS
    #from spacy.en.language_data import STOP_WORDS
    return STOP_WORDS

def getYoastStopword():
    return ["a", "about", "above", "after", "again", "against", "all", "am", "an", "and", "any", "are", "as", "at",
            "be", "because", "been", "before", "being", "below", "between", "both", "but", "by", "could", "did",
            "do", "does", "doing", "down", "during", "each", "few", "for", "from", "further", "had", "has", "have",
            "having", "he", "he'd", "he'll", "he's", "her", "here", "here's", "hers", "herself", "him", "himself",
            "his", "how", "how's", "i", "i'd", "i'll", "i'm", "i've", "if", "in", "into", "is", "it", "it's", "its",
            "itself", "let's", "me", "more", "most", "my", "myself", "nor", "of", "on", "once", "only", "or",
            "other", "ought", "our", "ours", "ourselves", "out", "over", "own", "same", "she", "she'd", "she'll",
            "she's", "should", "so", "some", "such", "than", "that", "that's", "the", "their", "theirs", "them",
            "themselves", "then", "there", "there's", "these", "they", "they'd", "they'll", "they're", "they've",
            "this", "those", "through", "to", "too", "under", "until", "up", "very", "was", "we", "we'd", "we'll",
            "we're", "we've", "were", "what", "what's", "when", "when's", "where", "where's", "which", "while",
            "who", "who's", "whom", "why", "why's", "with", "would", "you", "you'd", "you'll", "you're", "you've",
            "your", "yours", "yourself", "yourselves"]

def getHumboltStopword():
    return ["a", "about", "above", "above", "across", "after", "afterwards", "again", "against", "all", "almost", "alone", "along", "already", "also","although","always","am","among", "amongst", "amoungst", "amount",  "an", "and", "another", "any","anyhow","anyone","anything","anyway", "anywhere", "are", "around", "as",  "at", "back","be","became", "because","become","becomes", "becoming", "been", "before", "beforehand", "behind", "being", "below", "beside", "besides", "between", "beyond", "bill", "both", "bottom","but", "by", "call", "can", "cannot", "cant", "co", "con", "could", "couldnt", "cry", "de", "describe", "detail", "do", "done", "down", "due", "during", "each", "eg", "eight", "either", "eleven","else", "elsewhere", "empty", "enough", "etc", "even", "ever", "every", "everyone", "everything", "everywhere", "except", "few", "fifteen", "fify", "fill", "find", "fire", "first", "five", "for", "former", "formerly", "forty", "found", "four", "from", "front", "full", "further", "get", "give", "go", "had", "has", "hasnt", "have", "he", "hence", "her", "here", "hereafter", "hereby", "herein", "hereupon", "hers", "herself", "him", "himself", "his", "how", "however", "hundred", "ie", "if", "in", "inc", "indeed", "interest", "into", "is", "it", "its", "itself", "keep", "last", "latter", "latterly", "least", "less", "ltd", "made", "many", "may", "me", "meanwhile", "might", "mill", "mine", "more", "moreover", "most", "mostly", "move", "much", "must", "my", "myself", "name", "namely", "neither", "never", "nevertheless", "next", "nine", "no", "nobody", "none", "noone", "nor", "not", "nothing", "now", "nowhere", "of", "off", "often", "on", "once", "one", "only", "onto", "or", "other", "others", "otherwise", "our", "ours", "ourselves", "out", "over", "own","part", "per", "perhaps", "please", "put", "rather", "re", "same", "see", "seem", "seemed", "seeming", "seems", "serious", "several", "she", "should", "show", "side", "since", "sincere", "six", "sixty", "so", "some", "somehow", "someone", "something", "sometime", "sometimes", "somewhere", "still", "such", "system", "take", "ten", "than", "that", "the", "their", "them", "themselves", "then", "thence", "there", "thereafter", "thereby", "therefore", "therein", "thereupon", "these", "they", "thickv", "thin", "third", "this", "those", "though", "three", "through", "throughout", "thru", "thus", "to", "together", "too", "top", "toward", "towards", "twelve", "twenty", "two", "un", "under", "until", "up", "upon", "us", "very", "via", "was", "we", "well", "were", "what", "whatever", "when", "whence", "whenever", "where", "whereafter", "whereas", "whereby", "wherein", "whereupon", "wherever", "whether", "which", "while", "whither", "who", "whoever", "whole", "whom", "whose", "why", "will", "with", "within", "without", "would", "yet", "you", "your", "yours", "yourself", "yourselves", "the"]

class Stopword(AbstractStopword):

    def __init__(self, stopword_from=["default"]):
        """
        All stopwords are in small case.
        types_name are::
        default
        nltk
        spacy
        sklearn
        yoast
        humbolt
        googlehistory
        sql
        longlist
        :param stopword_from: list of names from where stopwords need to fetch.
        :type list:
        """
        self.to_include_stopword = stopword_from
        st = []
        for name in stopword_from:
            ss = get_stopword_list(name)
            #print(name, len(ss))
            st += ss
        self.stopword = list(set(st))

    def getStopword(self):
        """
        :return: stopwords
        :rtype: list
        """
        return self.stopword

# sp = Stopword(stopword_from=["nltk","sql"])
# print(len(get_stopword_list("nltk")))
# print(len(get_stopword_list("sql")))
# print(len(sp.getStopword()))
