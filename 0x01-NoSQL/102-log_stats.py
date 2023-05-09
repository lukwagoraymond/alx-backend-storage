#!/usr/bin/env python3
"""Python Script that provides some stats about
NGINX logs stored in MongoDB"""
import pymongo


def nginx_stat_count():
    """Returns counts for Nginx logs for total
    logs then counts per methods in the nginx logs"""
    client = pymongo.MongoClient()
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

    print("IPs:")
    top_IPs = nginx_collection.aggregate([
        {"$group":
            {
                "_id": "$ip",
                "count": {"$sum": 1}
            }
         },
        {"$sort": {"count": -1}},
        {"$limit": 10},
        {"$project": {
            "_id": 0,
            "ip": "$_id",
            "count": 1
        }}

    ])
    for top_ip in top_IPs:
        count = top_ip.get('count')
        ip_address = top_ip.get('ip')
        print(f"\t{ip_address}: {count}")


if __name__ == "__main__":
    nginx_stat_count()
