-- Create table using sample data in S3.
CREATE EXTERNAL TABLE IF NOT EXISTS pageviews (
pagename STRING,
dates STRING,
views STRING,
total INT,
trend INT
)
ROW FORMAT DELIMITED FIELDS TERMINATED BY '\t' LINES TERMINATED BY '\n'
LOCATION '${INPUT}';

-- Select a ranked list of the 100 most popular articles determined by number of total page views in descending order
INSERT OVERWRITE DIRECTORY '${OUTPUT}'
SELECT pagename, total
FROM pageviews
SORT BY total DESC
Limit 100;