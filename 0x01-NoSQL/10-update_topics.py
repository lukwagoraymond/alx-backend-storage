#!/usr/bin/env python3
"""Python function that changes all topics of a
school document based on the name"""
import pymongo


def update_topics(mongo_collection, name, topics):
    """Updates a field in a document if filed doesn't
    exist then a field is created"""
    mongo_collection.update_many({"name": name},
                                 {"$set": {"topics": topics}})
