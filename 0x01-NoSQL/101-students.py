#!/usr/bin/env python3
"""Python Function that returns all students sorted
by average score"""
import pymongo


def top_students(mongo_collection):
    """Returns all students sorted by Average
    Score"""
    return mongo_collection.aggregate([
        {
            "$project":
                {
                    "name": "$name",
                    "averageScore": {"$avg": "$topics.score"}
                }
        },
        {
            "$sort":
                {
                    "averageScore": -1
                }
        }
    ])
