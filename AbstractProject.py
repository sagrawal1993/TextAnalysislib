
#All of the function will return Json.
class AbstractProject:

    #It will provide meta information such as Id's, other statistics in json form
    #Give all the information about data.
    def get_meta_info(self):
        pass

    #It will calculate the score of the measures for the dataset on particular project.
    def find_measure_value(self):
        pass

    #It will provide the details of the document mentioned by Id.
    #It will contains the value of measure along with one given doc_info.
    def get_doc_info(self,id):
        pass