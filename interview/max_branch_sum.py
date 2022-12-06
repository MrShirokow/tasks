"""
Написать функцию, которая находит ветку с максимальной суммой, и возвращает эту сумму.
"""


from __future__ import annotations

import yaml
import pathlib

from enum import Enum
from typing import Optional
from dacite import from_dict
from dataclasses import dataclass


@dataclass
class Node:
    left: Optional[Node]
    right: Optional[Node]
    value: int


class Direction(Enum):
    left = 0
    right = 1


def max_branch_sum(node: Optional[Node]) -> int:
    if not node:
        return 0
    return node.value + max(
        max_branch_sum(node.left), 
        max_branch_sum(node.right)
    )


def main():
    base_dir = pathlib.Path(__file__).parent
    with open(base_dir.joinpath('yml/max_branch_sum.yml')) as f:
        data = yaml.safe_load(f)
    for test in data:
        root = from_dict(data_class=Node, data=test['root'])
        assert max_branch_sum(root) == test['verdict']
    print('\nAll tests are passed!\n')


if __name__ == '__main__':
    main()
