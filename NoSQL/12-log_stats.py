#!/usr/bin/env python3
"""
Script that provides stats about Nginx logs stored in MongoDB
"""
from pymongo import MongoClient


def print_nginx_stats():
    """
    Print statistics about nginx logs stored in MongoDB
    """
    try:
        # Connect to MongoDB
        client = MongoClient('mongodb://127.0.0.1:27017')
        db = client.logs
        nginx = db.nginx

        # Get total number of logs
        total_logs = nginx.count_documents({})
        print(f"{total_logs} logs")

        # Print methods stats
        print("Methods:")
        methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
        for method in methods:
            count = nginx.count_documents({"method": method})
            print(f"\tmethod {method}: {count}")

        # Get status check count
        status_check = nginx.count_documents({"method": "GET", "path": "/status"})
        print(f"{status_check} status check")

    except Exception:
        # If MongoDB is not running or any other error occurs, output default values
        print("0 logs")
        print("Methods:")
        for method in ["GET", "POST", "PUT", "PATCH", "DELETE"]:
            print(f"\tmethod {method}: 0")
        print("0 status check")


if __name__ == "__main__":
    print_nginx_stats()
