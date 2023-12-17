from helper import timing_decorator, write_sentences_to_file

class SentenceGenerator:
    """
    SentenceGenerator class generates unique sentences based on a context-free grammar.
    """

    def __init__(self) -> None:
        """
        Initialize the SetenceGenerator object.

        Attributes:
        - start_symbol (str): The start symbol of the grammar.
        - rule (dict): Grammar rules defining the language.
        - unprocessed_queue (list): Queue to track unprocessed grammar sequences.
        - unique_sentences (set): Set to store unique generated sentences.
        """

        self.start_symbol = 'S'
        self.rule = {
            'S': [['NP', 'VP']],
            'VP': [['Verb', 'NP']],
            'NP': [['Det', 'Noun'], ['NP', 'PP']],
            'PP': [['Prep', 'NP']],
            'Noun': ['president', 'sandwich', 'pickle', 'chief of staff', 'floor', ['Adj', 'Noun']],
            'Adj': ['fine', 'delicious', 'perplexed', 'pickled'],
            'Prep': ['with', 'on', 'under', 'in'],
            'Verb': ['ate', 'wanted', 'kissed', 'understood', 'pickled'],
            'Det': ['the', 'a', 'every']
        }
        self.unprocessed_queue = [['S']]
        self.unique_sentences = set()

    def __get_unique_sentence(self, grammar: list) -> str:
        """
        Generate a unique sentence based on the given grammar.

        Args:
        - grammar (list): The grammar to process.

        Returns:
        - str: The generated sentence.
        """

        sentence = ''

        while grammar:
            first_grammar_component = grammar.pop(0)
            derived_grammar_component = self.rule.get(first_grammar_component, None)
            if derived_grammar_component:
                for i, possibility in enumerate(derived_grammar_component):
                    if isinstance(possibility, str):
                        possibility = [possibility]
                    if i == 0:
                        prev_grammar = grammar
                        grammar = possibility + grammar
                    else:
                        self.unprocessed_queue.append([sentence] + possibility + prev_grammar)
            else:
                sentence += ' ' + first_grammar_component
            
        return (sentence.strip() + '.').capitalize()
            

    @timing_decorator
    def generate_unique_sentences(self, total_sentence: int = 100) -> set:
        """
        Generate a specified number of unique sentences.

        Args:
        - total_sentence (int): The number of unique sentences to generate.

        Returns:
        - set: Set of unique sentences.
        """
    
        while len(self.unique_sentences) < total_sentence:
            sentence = self.__get_unique_sentence(self.unprocessed_queue.pop(0))
            self.unique_sentences.add(sentence)
            if len(self.unprocessed_queue) <= 0:
                raise Exception(f"Cannot derive {total_sentence} unique sentences. Limit is {len(self.unique_sentences)}.")
        print(f'Successfully generate {total_sentence} unique sentences.')
        return self.unique_sentences

sentence_generator = SentenceGenerator()
unique_sentences = sentence_generator.generate_unique_sentences(10000)
write_sentences_to_file('output.txt', unique_sentences)

