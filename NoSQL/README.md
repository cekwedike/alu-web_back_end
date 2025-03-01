# NoSQL with MongoDB

This project demonstrates various NoSQL operations using MongoDB and Python's PyMongo driver. It covers fundamental to advanced MongoDB operations, including CRUD operations, querying, and aggregation pipelines.

## Project Structure

### MongoDB Basic Operations
* `0-list_databases`: Lists all MongoDB databases
* `1-use_or_create_database`: Creates or uses a database
* `2-insert`: Demonstrates document insertion
* `3-all`: Retrieves all documents
* `4-match`: Performs matching queries
* `5-count`: Counts documents
* `6-update`: Updates documents
* `7-delete`: Deletes documents

### Python with MongoDB
* `8-all.py`: Lists all documents using PyMongo
* `9-insert_school.py`: Inserts documents into school collection
* `10-update_topics.py`: Updates document topics
* `11-schools_by_topic.py`: Finds schools by specific topic

### Advanced Operations
* `100-find`: Advanced find operations
* `101-students.py`: Computes average scores for students
* `102-log_stats.py`: Provides statistics about Nginx logs
* `12-log_stats.py`: Extended log statistics

### Utility
* `mongodb_check.py`: Helper script for MongoDB connection testing

## Requirements
* MongoDB 4.2 or higher
* Python 3.7 or higher
* PyMongo module
* Running MongoDB instance (default: localhost:27017)

## Setup
1. Install MongoDB on your system
2. Install PyMongo:
```bash
pip3 install pymongo
```

## Usage
### For MongoDB Shell Scripts
```bash
mongo < script_name
```

### For Python Scripts
```bash
./script_name.py
# or
python3 script_name.py
```

## Note
Ensure MongoDB service is running before executing the scripts. Default connection settings use localhost:27017.
