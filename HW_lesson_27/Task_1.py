#Task 2
"""
Розширити структуру, яку побудували на уроці, можливістю вставки дерева в наявне дерево та видалення піддерева з дерева, що існує.
"""

from typing import (
    Optional,
    Any,
)


class Category:
    def __init__(self, name: str, parent: Optional["Category"] = None):
        self.name = name
        self._children = []
        self._parent = parent
        if self.parent is not None:
            self._parent._children.append(self)

    def __str__(self):
        return self.name

    @property
    def parent(self):
        return self._parent

    @property
    def children(self):
        return self._children

    def add_child(self, child):
        if child.parent is not None:
            print("The provided child category already has a parent.")
        else:
            self._children.append(child)
            child._parent = self

    def remove_child(self, child_name):
        for i, child in enumerate(self._children):
            if child.name == child_name:
                self._children.pop(i)
                child._parent = None
                return
        print("Child category not found.")
        


def print_tree(category: Category, ident: int = 0):
    print('--' * ident, category)
    for child in category.children:
        # print(f"  {child}")
        print_tree(child, ident + 1)


def find(category: Category, name: str) -> Optional[Category]:
    print(f"... {category}")
    if category.name == name:
        return category

    for child in category.children:
        value = find(child, name)
        if value is not None:
            return value

    return None


if __name__ == '__main__':
    strings = Category("strings", parent=None)
    beats = Category("beats", parent=None)
    guitars = Category("guitars", parent=strings)
    violins = Category("violins", parent=strings)
    drums = Category("drums", parent=beats)
    acoustics = Category("acoustics", parent=guitars)
    electrics = Category("electrics", parent=guitars)
    alt = Category("alt", parent=violins)
    fenders = Category("fenders", parent=electrics)
    gibsons = Category("gibsons", parent=electrics)

    print(electrics)
    print(electrics.parent)
    print(electrics.parent.parent)
    print(electrics.parent.parent.parent)

    print()
    print_tree(strings, 1)
    beats = Category("beats", parent=strings)
    drums = Category("drums", parent=beats)
    print_tree(strings, 1)

    print("===")
    cat = find(strings, "123456")
    print(cat)

    new_category = Category("keyboards")
    beats.add_child(new_category)
    print_tree(strings, 1)
    strings.remove_child("violins")  
    print_tree(strings, 1)
