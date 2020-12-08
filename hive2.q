-- Create table using sample data in S3.
CREATE EXTERNAL TABLE IF NOT EXISTS pageviews (
pagename STRING,
dates STRING,
views STRING,
curTotal INT,
curTrend INT
)
ROW FORMAT DELIMITED FIELDS TERMINATED BY '\t' LINES TERMINATED BY '\n'
LOCATION '${INPUT}';

-- Select a ranked list of the 100 most popular articles determined by number of popularity trend in descending order
INSERT OVERWRITE DIRECTORY '${OUTPUT}'
SELECT pagename, ' ', SUM(curTrend) AS trend
FROM pageviews
GROUP BY pagename
SORT BY trend DESC
Limit 100;