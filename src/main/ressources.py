from typing import Any


def isList(obj : str | list) -> Any:
    if isinstance(obj, list):
        return obj
    else:
        return list(obj)

def oddHandler(nb : int) -> int:
    if nb % 2 == 0:
        return nb
    else:
        return nb+1

