#!/usr/bin/env python3
"""Python Script that provides some stats about
NGINX logs stored in MongoDB"""
import pymongo
from pymongo import MongoClient


def nginx_stat_count():
    """Returns counts for Nginx logs for total
    logs then counts per methods in the nginx logs"""
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_collection = client.logs.nginx

    collectn_count = nginx_collection.count_documents({})
    print(f'{collectn_count} logs')
    print('Methods:')
    methods_list = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods_list:
        method_count = nginx_collection.count_documents({"method": method})
        print(f"\tmethod {method}: {method_count}")

    stat_check = nginx_collection.count_documents(
        {"method": "GET", "path": "/status"})
    print(f"{stat_check} status check")


if __name__ == "__main__":
    nginx_stat_count()
