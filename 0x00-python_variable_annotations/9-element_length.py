#!/usr/bin/env python3

"""This function adds annotations for the function below


```python
def element_length(lst):
    return [(i, len(i)) for i in lst]
```
"""

from typing import Iterable, Sequence, Tuple, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    '''Computes the length of a list of sequences.
    '''
    return [(i, len(i)) for i in lst]
