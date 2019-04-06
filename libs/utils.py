"""
Small file with different utils used by the project.
No order or sorting needed here
"""

import json


def jsonLoad(path: str):
    with open(path, "r") as workon:
        data = json.loads(workon)
    return data