# SetenceGenerator

SetenceGenerator is a Python class that generates unique sentences based on a context-free grammar.


### Example

```python
from SetenceGenerator import SetenceGenerator

# Create an instance of SetenceGenerator
sentence_generator = SetenceGenerator()

# Generate 100,000 unique sentences
unique_sentences = sentence_generator.generate_unique_sentences(100000)s
```


#### Note on Algorithm Drawback

While the SetenceGenerator class provides a mechanism to generate unique sentences based on context-free grammar, it's essential to be cautious about potential drawbacks. The algorithm heavily relies on the grammar rules provided, and depending on the complexity of the grammar or the specific rules, it may lead to an infinite loop in the generation process. It is recommended to carefully design and test the grammar to avoid unintended behaviors