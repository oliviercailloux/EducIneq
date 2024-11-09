from pyzotero import zotero
import bibtexparser
from pathlib import Path
from collections import Counter
import pandas as pd

# root = Path("../")
root = Path("Économie du développement/") / "Litt/"
article = root / "Article/"

def main():
    my_userID = 97818
    with open(root / "LitZot/" / "Zotero API key.txt", "r") as f:
        my_api_key = f.read().strip()
    
    zot = zotero.Zotero(my_userID, "user", my_api_key)
    collection_key = "9CMUGFZR"
    items = zot.collection_items(collection_key)
    items_bibtex = zot.collection_items(collection_key, sort="dateAdded", format="bibtex")
    # items_bibtex = zot.items(sort="dateAdded", limit=100, format="bibtex", start=0, tag="Éducation et inégalité en Amérique latine")
    its = items_bibtex.entries
    # print(len(its))
    print(f"First item: {its[0]['title']}, last item: {its[-1]['title']}")

    # dump = "\n\n".join([bibtexparser.dumps(i) for i in all_items_bibtex])
    dump = bibtexparser.dumps(items_bibtex)
    with open(article / "zotero.bib", "w", encoding="utf-8") as f:
        f.write(dump)
