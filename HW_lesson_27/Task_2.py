# #Task 2
# """
# Написати алгоритм, що буде парсити html документ та зберігати його Document Object Model (DOM) у дереві.
# Дерево повинно зберігати тег та текст, обрамлений цим тегом (якщо є такий).
# Додати можливість пошуку тексту за тегом.
# Вхідні дані: html документ та тег
# Вихідні дані: текст, якщо є.
# """

import requests
from bs4 import BeautifulSoup


def create_dom_tree(html_doc):
    """Creates a DOM tree from parsed HTML elements."""
    tree = {}
    root = tree

    # Parse the HTML using BeautifulSoup
    soup = BeautifulSoup(html_doc, 'html.parser')

    # Iterate through tags and create the tree structure
    for element in soup.find_all(True):
        tag = element.name
        if tag in tree:
            child = tree[tag]
        else:
            child = {}
            tree[tag] = child

        child['text'] = element.text.strip()  # Extract text and strip whitespace

    return root


def search_text_by_tag(tree, tag):
    """Searches for text within the DOM tree by tag."""
    if tag in tree:
        return tree.get('text', '')

    for child in tree.values():
        found_text = search_text_by_tag(child, tag)
        
        if found_text:
            print(found_text)
            return found_text
    return ''


if __name__ == "__main__":
    url = 'https://ru.wikipedia.org/wiki/%D0%97%D0%B0%D0%B3%D0%BB%D0%B0%D0%B2%D0%BD%D0%B0%D1%8F_%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0'
    response = requests.get(url)


    tree = create_dom_tree(response.text)
    #print(tree)

    


