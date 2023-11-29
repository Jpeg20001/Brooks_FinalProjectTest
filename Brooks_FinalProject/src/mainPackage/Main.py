# David Brown, Michael Gonzales
# brown6dw@mail.uc.edu"
# Final Project"
# 11/29/2023
# IS 4010
# Fall 2023
# The project shows I can use AI to help solve arrays and other fun stuff.

from jsonReaderPackage.jsonReader import *

import json

if __name__ == "__main__":

    
    json_reader = JsonDataReader('EncryptedGroupHints Fall 2023 Section 001.json')

    json_reader.read_data()

    data = json_reader.get_data()

