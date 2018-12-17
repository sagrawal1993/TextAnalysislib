#!flask/bin/python
from flask import Flask,jsonify
from Test import ContextualSuggestionTopicExtraction

app = Flask(__name__)
project = None
@app.route('/')
def index():
    return "Hello, World!"

@app.route('/ContextualSuggestionTopic')
def ContextualInfoMeta():
    global project
    if project ==None or project.name != "ContextualTopic":
        project = ContextualSuggestionTopicExtraction.ContexualSuggestionTopicExtraction()
    meta_info = project.get_meta_info()
    #doc_info = project.get_doc_info(0)
    return jsonify(meta_info)

@app.route('/ContextualSuggestionTopic/<string:id>')
def ContextualTopic(id):
    global project
    if project ==None or project.name != "ContextualTopic":
        project = ContextualSuggestionTopicExtraction.ContexualSuggestionTopicExtraction()
        meta_info = project.get_meta_info()
    doc_info = project.get_doc_info(id)
    return jsonify(doc_info)

@app.route('/ContextualSuggestionTopic/HighFreqTopic')
def ContextualTopicList():
    global project
    if project ==None or project.name != "ContextualTopic":
        project = ContextualSuggestionTopicExtraction.ContexualSuggestionTopicExtraction()
        meta_info = project.get_meta_info()
    #topic_list = project.find_high_freq_topic()
    #topic_list = project.find_noun_topics()
    topic_list = project.find_topic_score()
    return jsonify(topic_list)

if __name__ == '__main__':
    app.run(debug=True)