# twitterscrapes
A simple script to import basic data from twitter.

## Requirements
* Python 3
* Tweepy and pymysql libraries
* Mysql or MariaDB

## Usage
* Import scrapes.sql in your Mysql or MariaDB database.
* Edit importer.py with your Twitter API credentials (l.10-13) and database connection data (l.20).
* Edit account_list to match the users you want to monitor (l.22)
* Run the script through a cron job once per day.
