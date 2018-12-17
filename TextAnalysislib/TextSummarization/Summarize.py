#Gensim summaraization can provide keywords corresponds to text as well summary.
#summary has the ration to define the shrinkness of the summarry.
#Can get as a list of string instead of a single string.
#example.
from gensim.summarization import keywords
from gensim.summarization import summarize

def get_summary(content):
    return summarize(content)

def get_keyword(content):
    return keywords(content).split("\n")
