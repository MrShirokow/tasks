"""
Написать функцию, которая считает сумму значений листьев в бинарном дереве.
Листом считается узел, у которого нет детей.
"""

from __future__ import annotations

import yaml
import pathlib

from typing import Optional
from dacite import from_dict
from dataclasses import dataclass


@dataclass
class Node:
    value: int
    left: Optional[Node]
    right: Optional[Node]


def calculate_leafs_sum(root: Node) -> int:
    summ = 0

    def _calculate_leafs_sum(node: Optional[Node], summ: int) -> int:
        if not node:
            return summ
        if not node.left and not node.right:
            summ += node.value
        summ = _calculate_leafs_sum(node.left, summ)
        summ = _calculate_leafs_sum(node.right, summ)
        return summ

    summ = _calculate_leafs_sum(root, summ)
    return summ
            

def main():
    base_dir = pathlib.Path(__file__).parent
    with open(base_dir.joinpath('yml/max_branch_sum.yml')) as f:
        data = yaml.safe_load(f)
    for test in data:
        root = from_dict(data_class=Node, data=test['root'])
        answer = calculate_leafs_sum(root)
        assert answer == test['summ']
    print('\nAll tests are passed!\n')


if __name__ == '__main__':
    main()
