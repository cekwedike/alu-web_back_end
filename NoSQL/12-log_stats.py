#!/usr/bin/env python3
"""Provides stats about Nginx logs stored in MongoDB"""
from pymongo import MongoClient


def print_logs_stats():
    """Print nginx logs stats."""
    client = MongoClient('mongodb://127.0.0.1:27017')
    collection = client.logs.nginx

    try:
        # Count total logs
        n_logs = collection.count_documents({})
        print("%d logs" % n_logs)

        # Methods section
        print("Methods:")
        methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
        for method in methods:
            n_method = collection.count_documents({"method": method})
            print("\tmethod %s: %d" % (method, n_method))

        # Status check
        n_status = collection.count_documents(
            {"method": "GET", "path": "/status"}
        )
        print("%d status check" % n_status)

    except:
        print("0 logs")
        print("Methods:")
        for method in ["GET", "POST", "PUT", "PATCH", "DELETE"]:
            print("\tmethod %s: 0" % method)
        print("0 status check")


if __name__ == "__main__":
    print_logs_stats()
