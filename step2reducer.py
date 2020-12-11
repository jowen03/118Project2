#!/usr/bin/env python3
import sys
from collections import defaultdict

# The following arguments are necessary for partitioning step2 map intermediate result by page name and
# sorting them by key + date. Add these arguments when custom configuring hadoop streaming program
# -D stream.num.map.output.key.fields=2
# -D map.output.key.field.separator=}
# -D mapreduce.partition.keypartitioner.options=-k1,1
# -partitioner org.apache.hadoop.mapred.lib.KeyFieldBasedPartitioner

# Dates set that have positive value for page trend
POSITIVE = {"20160603", "20160604", "20160605"}


# Determine if we should output from current dictionary items
def printer(cur_dict):
    # Retrieve dates list and corresponding list sorted by date in ascending order
    dates, views = map(list, zip(*sorted(cur_dict.items())))

    total_views = sum(views)
    trend = 0

    # If the page views is less than 10, then it's unpopular, don't output it
    if total_views >= 10:
        for i, cur_date in enumerate(dates):
            if cur_date in POSITIVE:
                trend += views[i]

            else:
                trend -= views[i]

        print("{}\t{}\t{}\t{}\t{}".format(pre_name, dates, views, total_views, trend))


if __name__ == "__main__":
    pre_name = ""
    page_dict = defaultdict(int)

    for line in sys.stdin:
        try:
            # Retrieve article name, date and page views
            key, value = line.split()
            name, date = key.split('}')

            # If current name is different from previous name, then it indicates we have finished counting the data for
            # previous page name and should output it in one line. After that, reset the dictionary and let previous
            # name be current name.
            if name != pre_name:
                if pre_name:
                    printer(page_dict)

                page_dict.clear()
                pre_name = name

            # Keep counting the page views by date
            page_dict[date] += int(value)

        except:
            continue

    # Output the last item out from step2 reducer
    printer(page_dict)
