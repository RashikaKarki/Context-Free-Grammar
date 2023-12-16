import time

def timing_decorator(func):
    """
    Decorator to measure the execution time of a function.

    Usage:
    @timing_decorator
    def my_function():
        # ... function implementation ...

    The decorator prints the elapsed time when the decorated function is executed.

    Args:
    - func (callable): The function to be decorated.

    Returns:
    - callable: Decorated function.
    """
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"Function '{func.__name__}' took {elapsed_time:.4f} seconds.")
        return result
    return wrapper

def write_sentences_to_file(file_name: str, sentences: set):
    """
    Write unique sentences to a text file.

    Args:
    - file_name (str): The name of the file to write to.
    - sentences (set): Set of unique sentences.

    Returns:
    - None
    """
    with open(file_name, 'w', encoding='utf-8') as file:
        for sentence in sentences:
            file.write(sentence + '\n')
