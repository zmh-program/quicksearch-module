from importlib import import_module
from typing import List
from time import time


def parse(text: str) -> None:
    benchmark = time()

    try:
        pre, *child = text.split(".")
        value_list = eval(".".join([pre, *child[:-1]]), globals(), {
            pre: globals()[pre] if pre in globals() else import_module(pre),
        })
        target = child[0].lower() if child else ""
        res: List[str] = [element for element in dir(value_list) if element.lower().startswith(target)]
    except ModuleNotFoundError:
        res = []

    duration = time() - benchmark

    text_length = max(tuple(map(len, res))) if res else 0
    for i, r in enumerate(res):
        print(r.ljust(text_length), end="\t" if i % 4 else "\n")
    print(f"\n{len(res)} in set ({round(duration, 2)} sec)")


if __name__ == "__main__":
    while True:
        content = input("Search> ").strip()
        if content.lower() in ("q", "quit", "exit"):
            break
        parse(content)
