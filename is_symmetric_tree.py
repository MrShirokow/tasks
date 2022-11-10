from __future__ import annotations

import yaml

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


def is_symmetric(root: Node) -> bool:
    def _is_symmetric(left: Node, l_dir: str, right: Node, r_dir: str) -> bool:
        if l_dir == r_dir:
            return False
        if left is None and right is None:
            return True
        if (
            left is None and right is not None or 
            left is not None and right is None
        ):
            return False
        if left.value != right.value:
            return False
        else:
            return (
                _is_symmetric(left.left, Direction.left, right.right, Direction.right) and 
                _is_symmetric(left.right, Direction.right, right.left, Direction.left)
            )

    return _is_symmetric(root.left, Direction.left, root.right, Direction.right)


def main():
    with open('data.yml') as f:
        data = yaml.safe_load(f)
    for test in data:
        root = from_dict(data_class=Node, data=test['root'])
        assert is_symmetric(root) == test['verdict']
    print('\nAll tests are passed!\n')


if __name__ == '__main__':
    main()
