#Find the probability Distribution from which the document is being generated.

class AbstractGenerativeModel:
    def generateProbabilityDistribution(self,document_list):
        pass

    def getProbabilityDistribution(self):
        pass

    def probOfDocument(self,document):
        pass
