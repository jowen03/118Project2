-- In order to force only one output file, so we need to force the number of reducers
set mapred.reduce.tasks = 1;

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

-- Select a ranked list the articles contains word "potter" determined by number of page views in descending order
INSERT OVERWRITE DIRECTORY '${OUTPUT}'
SELECT *
FROM pageviews
WHERE LOWER(pagename) LIKE '%potter%'
SORT BY total DESC;