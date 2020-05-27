from pymorphy2 import MorphAnalyzer
from sys import stdin


def clean(text):
    trash = ',.:;!?-'
    for i in trash:
        text = text.replace(i, ' ')
    return text

def noun_counter():

