#!/usr/bin/env python3
"""Log stats - generates stats about Nginx logs stored in MongoDB"""
from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    db = client.logs
    nginx = db.nginx
    
    # Get total number of documents
    docs_count = nginx.count_documents({})
    print(f"{docs_count} logs")

    # Count methods
    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count = nginx.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    # Count status check
    status_check = nginx.count_documents({
        "method": "GET",
        "path": "/status"
    })
    print(f"{status_check} status check")
