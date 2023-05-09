#!/usr/bin/env python3
"""Python function that lists all documents in
a collection"""
import pymongo


def list_all(mongo_collection):
    """Returns a list of documents in a
    collection else return an empty list"""
    if mongo_collection is None:
        return []
    docs = mongo_collection.find()
    return [doc for doc in docs]
    # return list(mongo_collection.find())
