import os

from sentence_generator import SentenceGenerator
from parse_grammar import parse_grammar
from helper import write_sentences_to_file

if __name__ == '__main__':
    file_name = 'grammar.gr'
    file_path = os.path.join(os.getcwd(), file_name)
    rule = parse_grammar(file_path)
    sentence_generator = SentenceGenerator(rule)
    unique_sentences = sentence_generator.generate_unique_sentences(10000)
    write_sentences_to_file('output.txt', unique_sentences)

