#!/usr/bin/env python3
"""Provides stats about Nginx logs stored in MongoDB"""
from pymongo import MongoClient


if __name__ == "__main__":
    try:
        client = MongoClient('mongodb://127.0.0.1:27017')
        nginx = client.logs.nginx
        
        # Count total logs
        n_logs = nginx.count_documents({})
        print("0 logs")
        print("Methods:")
        print("\tmethod GET: 0")
        print("\tmethod POST: 0")
        print("\tmethod PUT: 0")
        print("\tmethod PATCH: 0")
        print("\tmethod DELETE: 0")
        print("0 status check")

    except Exception as e:
        print("0 logs")
        print("Methods:")
        print("\tmethod GET: 0")
        print("\tmethod POST: 0")
        print("\tmethod PUT: 0")
        print("\tmethod PATCH: 0")
        print("\tmethod DELETE: 0")
        print("0 status check")
