def is_terminal(symbols):
    return not all(symbol[0].isupper() for symbol in symbols.split())

def parse_grammar(file_path):
    grammar = {}
    with open(file_path, 'r') as file:
        for line in file:
            lineSegments = line.strip().split("\t")
            if len(lineSegments) == 3:
                _, key_data, *value_data = lineSegments

                if key_data != 'ROOT':
                    value_data = value_data[0] if is_terminal(value_data[0]) else value_data[0].split(" ")
                    value_data = [value_data]

                    # To prevent infinite loop
                    if key_data in grammar:
                        if isinstance(value_data, list) and key_data in value_data[0]: 
                            grammar[key_data].extend(value_data)
                        else:
                            temp = grammar[key_data]
                            value_data.extend(temp)
                            grammar[key_data] = value_data
                    else:
                        if value_data:
                            grammar[key_data] = value_data
    return grammar
