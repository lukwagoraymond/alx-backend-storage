#!/usr/bin/env python3
"""Python function that returns the list
of schools having a specific topic"""
import pymongo


def schools_by_topic(mongo_collection, topic):
    """Returns a list of schools having a
    specific topic"""
    return mongo_collection.find({"topics": topic})
