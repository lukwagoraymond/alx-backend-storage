#!/usr/bin/env python3
"""Python function inserts a new document in
a collection based on kwargs"""
import pymongo


def insert_school(mongo_collection, **kwargs):
    """Returns a new id of inserted document"""
    doc_insert = mongo_collection.insert_one(kwargs)
    return doc_insert.inserted_id
