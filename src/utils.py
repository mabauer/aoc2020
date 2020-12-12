from typing import List

import os

def read_inputfile(filename: str) -> List[str]:
    with open("input" + os.path.sep + filename) as f:
        input = [line.strip() for line in f]
    return input