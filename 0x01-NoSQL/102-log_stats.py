#!/usr/bin/env python3
""" A script that displays stats about nginx logs and the top 10 of
    the most present IPs in the collection nginx of the database logs
"""
from pymongo import MongoClient
from typing import List


if __name__ == "__main__":
    # connect to MongoDB database
    client: MongoClient = MongoClient('mongodb://127.0.0.1:27017')
    db = client['logs']
    collection = db['nginx']

    # Get number of document in the collection
    total_logs: int = collection.count_documents({})
    print(f"{total_logs} logs")

    # Get number of documents with the list of methods
    http_methods: List[str] = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    method_stats = {method: collection.count_documents(
        {"method": method}) for method in http_methods}

    print("Methods:")
    for method, count in method_stats.items():
        print(f"\tmethod {method}: {count}")

    # Get the number of documents with method=GET and path=/status
    status_count: int = collection.count_documents(
            {"method": "GET", "path": "/status"}
            )
    print(f"{status_count} status check")

    # Get the top 10 most present IDs
    print("IPs:")
    request_logs = collection.aggregate(
        [
            {
                '$group': {'_id': "$ip", 'totalRequests': {'$sum': 1}}
            },
            {
                '$sort': {'totalRequests': -1}
            },
            {
                '$limit': 10
            },
        ]
    )
    for request_log in request_logs:
        ip = request_log['_id']
        ip_requests_count = request_log['totalRequests']
        print('\t{}: {}'.format(ip, ip_requests_count))
