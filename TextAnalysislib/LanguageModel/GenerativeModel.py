from TextAnalysislib.LanguageModel.AbstractLanguageModel import AbstractGenerativeModel
from nltk.probability import FreqDist

"""
This is the result for Maximum Likelihood estimation. 
It can also be generated using Maximum Aprior Estimation.
"""
class termBased(AbstractGenerativeModel):

    #It requires to pass analyser that will break document into tokens.
    #It can also remove stopwords and make normalization for words.
    def __init__(self, analyser):
        self.analyser = analyser
        print("Term Based ")

    def generateProbabilityDistribution(self, document_list):
        tokens = []
        for doc in document_list:
            tokens += self.analyser(doc)
        self.freqDist = FreqDist(tokens)

    def getProbabilityDistribution(self):
        return self.freqDist

    def probOfDocument(self,document):
        tokens = self.analyser(document)
        prob = 1.0
        for token in tokens:
            if self.freqDist.has_key(token):
                prob *= self.freqDist.freq(token)
        if prob==1.0:
            return 0.0
        return prob


"""
It will cosider background model as given and the document is generated from mixture of
Background{As Consider english language Frequency Distro} and other required info's distro.
P(word|foreground Model) = 1/(1-prob_word_form_backgound)[count_of_word_in_doc/total_word_count - prob_word_from_backgound * prob(word|background) ] 
"""
class termBasedConsiderBackgroundModel(AbstractGenerativeModel):

    def __init__(self,analyser, backgroundDistribution, probOfBackgroundModel):
        self.backGroundDistro = backgroundDistribution
        self.analyser = analyser
        self.ProbBackground = probOfBackgroundModel

    def generateProbabilityDistribution(self, document_list):
        tokens = []
        for doc in document_list:
            tokens += self.analyser(doc)
        self.freqDist = FreqDist(tokens)

        foreground_prob = 1 - self.ProbBackground
        prob_distro = {}

        backDistro = FreqDist()
        for word in self.freqDist.keys():
            backDistro[word] = self.backGroundDistro[word]

        for word in self.freqDist.keys():
            if word not in self.backGroundDistro.keys():
                prob_distro[word] = (1.0/foreground_prob)*(self.freqDist.freq(word))
            else:
                prob_distro[word] = (1.0/foreground_prob)*(self.freqDist.freq(word) - (self.ProbBackground *backDistro.freq(word)))
        self.prob_distro = prob_distro
        flag = True
        for key in prob_distro:
            if prob_distro[key]<0 or prob_distro[key] >1:
                flag=False
                break
        return flag


    def getProbabilityDistribution(self):
        return self.prob_distro

    def probOfDocument(self, document):
        tokens = self.analyser(document)
        prob = 1.0
        for token in tokens:
            if token in self.prob_distro:
                prob *= self.prob_distro[token]
        if prob == 1.0:
            return 0.0
        return prob