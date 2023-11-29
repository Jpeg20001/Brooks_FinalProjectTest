import json
class JsonDataReader:

    def __init__(self, json_file_path):

        self.json_file_path = json_file_path

        self.data = None



    def read_data(self):

        with open(self.json_file_path, 'r') as json_file:

            self.data = json.load(json_file)['Brooks']



    def get_data(self):

        return self.data