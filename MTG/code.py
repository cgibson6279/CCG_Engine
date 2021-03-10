#!/usr/bin/env python
'''

'''

import requests

from mtgsdk import Card
from mtgsdk import Set
from mtgsdk import Type
from mtgsdk import Supertype
from mtgsdk import Subtype
from mtgsdk import Changelog

from typing import List, Dict

def main():
    card = Card.find(386616)
    print(card.name
if __name__=="__main__":
    main()