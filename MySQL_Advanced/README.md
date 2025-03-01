# MySQL Advanced

This project contains a collection of advanced MySQL scripts demonstrating various database concepts and operations. Each script focuses on specific database functionality, from table creation to complex stored procedures.

## Scripts Overview

### Basic Operations
* `0-uniq_users.sql`: Creates a users table with unique email constraints
* `1-country_users.sql`: Implements country enumeration and table creation
* `2-fans.sql`: Ranks country origins by their number of fans
* `3-glam_rock.sql`: Analyzes Glam rock bands by their longevity
* `4-store.sql`: Implements a trigger for item quantity updates
* `5-valid_email.sql`: Creates a trigger for email validation

### Advanced Operations
* `6-bonus.sql`: Stored procedure for adding bonus corrections
* `7-average_score.sql`: Computes and stores average student scores
* `8-index_my_names.sql`: Creates an index on the first letter of name
* `9-index_name_score.sql`: Creates an index on the first letter of name and score
* `10-div.sql`: Creates a function for safe division
* `11-need_meeting.sql`: Creates a view for students needing meetings

### Complex Procedures
* `100-average_weighted_score.sql`: Computes weighted average scores
* `101-average_weighted_score.sql`: Advanced weighted score calculations

## Requirements
* MySQL 5.7 or higher
* Proper database privileges to create tables, triggers, procedures, and functions

## Usage
Each script can be executed in MySQL using the source command:
```sql
source script_name.sql;
```

## Note
Ensure you have the appropriate permissions and database selected before running these scripts.
