"""
Написать функцию, которая считает количество левых листьев в бинарном дереве.
Листом считается узел, у которого нет детей. Левый лист - узел, в который пришли по левой ветке из родителя.
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


class Direction(Enum):
    left = 0
    right = 1


def calculate_left_leafs(root: Node) -> int:
    count = 0

    def _calculate_left_leafs(direction: Optional[Direction], node: Optional[Node], count: int) -> int:
        if not node:
            return count
        if not node.left and not node.right and direction == Direction.left:
            count += 1
        count = _calculate_left_leafs(Direction.left, node.left, count)
        count = _calculate_left_leafs(Direction.right, node.right, count)
        return count

    count = _calculate_left_leafs(None, root, count)
    return count
            

def main():
    base_dir = pathlib.Path(__file__).parent
    with open(base_dir.joinpath('yml/left_leafs_data.yml')) as f:
        data = yaml.safe_load(f)
    for test in data:
        root = from_dict(data_class=Node, data=test['root'])
        answer = calculate_left_leafs(root)
        assert answer == test['count']
    print('\nAll tests are passed!\n')


if __name__ == '__main__':
    main()
