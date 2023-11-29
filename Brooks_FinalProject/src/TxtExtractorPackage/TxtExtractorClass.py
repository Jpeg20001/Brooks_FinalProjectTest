#TxtExtractor

class TextFileExtractor:
    def __init__(self, txt_file_path):
        self.txt_file_path = txt_file_path
        self.lines = None

    def read_lines(self):
        try:
            with open(self.txt_file_path, 'r', encoding='utf-8') as txt_file:
                self.lines = txt_file.readlines()
        except FileNotFoundError:
            print(f"Error: File not found - {self.txt_file_path}")

    def extract_info_by_indexes(self, indexes):
        extracted_info = []
        for index in indexes:
            try:
                # Append the line at the specified index to the list
                extracted_info.append(self.lines[index].strip())
            except IndexError:
                # Handle the case where the index is out of range
                print(f"Error: Index {index} is out of range.")

        # Print the result as a sentence
        if extracted_info:
            sentence = " ".join(extracted_info)
            return sentence
        else:
            print("No information extracted.")