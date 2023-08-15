#!/usr/bin/env python3
""" A script that returns lists of documents"""


def list_all(mongo_collection):
    """ A function that lists all documents in a collection
    """

    lists = []

    for doc in mongo_collection.find():
        lists.append(doc)
    return lists
