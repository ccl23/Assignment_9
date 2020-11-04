#! /usr/bin/env python
"""a module file to import and parse document sentences
Classes: 
    Sentence
Functions:
    main
Requirements:
    os
    yaml
"""

import os
import yaml

class Sentence:
    """A class to create a sentence object
    ...
    
    Attributes
    ----------
    sentence_string : str
        text of the sentence string
    document : str
        name of the document the sentence same from
    line_number : int
        the line number in the document the sentence came from
    character_length : int
        number of characters including white space and punctuation
    word_length : int
        number of words in sentence, defined as white-space delimited string characters
    
    Methods
    -------
    count_charaters():
        Counts number of characters including white space and punctuation;stores as character_length
    count_words():
        Counts number of words in sentence and stores as instance attribute word_length
    read():
        Prints sentence object attributes
    write(file):
        Writes the sentence object attributes to yaml doc
"""
    def __init__(self, sentence_string, document, line_number):
        self.sentence_string = sentence_string
        self.document = document
        self.line_number = line_number
        self.character_length = None
        self.word_length = None
    
    def __repr__(self):
        return f"Sentence({self.sentence_string}, document = {self.document}, line_number = {self.line_number})"
    
    def count_characters(self):
        """count characters in sentence including white space and punctuation"""
        self.character_length = len(self.sentence_string)
    
    def count_words(self):
        """count words (defined as white-space-delimited string characters)"""
        self.word_length = len(self.sentence_string.split())

    def read(self):
        """print sentence object attributes"""
        read = {'Sentence String' : self.sentence_string,
                    'Document' : self.document,
                    'Line Number' : self.line_number,
                    'Character Length' : self.character_length,
                    'Word Length' : self.word_length}
        return read
    
    def write(self, file):
        """write the sentence object attributes to yaml doc"""
        with open(file, "a") as f:
            f.write("---")
            yaml.dump(self,f)

def main():
    """module to make yaml outpout with sentence attributes"""
    if os.path.exists("output.yaml"):
        os.remove("output.yaml")
        print("output.yaml exists - file remove")
    else:
        print("output.yaml does not exist")

    directory = r'cleaned_input'
    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)
    with open(filepath, "r") as f:
        count = 0
        for line in f:
            count +=1
            line_in = f.readline()
            sent_in = Sentence(sentence_string = line_in, document = filename, line_number = count)
            sent_in.count_words()
            sent_in.count_characters()
            sent_in.write("output.yaml")


if __name__ == "__main__":
    main()
