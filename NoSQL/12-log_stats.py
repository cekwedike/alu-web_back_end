#!/usr/bin/env python3
"""Provides stats about Nginx logs stored in MongoDB"""
from pymongo import MongoClient


def print_nginx_logs_stats():
    """Prints stats about Nginx logs stored in MongoDB"""
    client = MongoClient('mongodb://127.0.0.1:27017')
    logs_collection = client.logs.nginx

    # Count total logs
    total_logs = logs_collection.count_documents({})
    print(f"{total_logs} logs")

    # Print methods stats
    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count = logs_collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    # Count status check
    status_checks = logs_collection.count_documents({
        "method": "GET",
        "path": "/status"
    })
    print(f"{status_checks} status check")


if __name__ == "__main__":
    print_nginx_logs_stats()
