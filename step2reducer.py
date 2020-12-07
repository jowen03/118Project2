#!/usr/bin/env python3
import sys
from collections import defaultdict

web_time_dict = defaultdict(dict)
POSITIVE = {"20160603", "20160604", "20160605"}

if __name__ == "__main__":
    for line in sys.stdin:
        # Retrieve article name, date and page views
        try:
            key, value = line.split()
            name, date = key.split('}')
            cur_dict = web_time_dict[name]
            cur_dict[date] = cur_dict.get(date, 0) + int(value)

        except:
            continue

    # Retrieve lists of sorted dates and corresponding views
    # Compute total page views and popularity trend
    for name, cur_dict in web_time_dict.items():
        temp_tuples = list(zip(*sorted(cur_dict.items())))
        dates, views = map(list, temp_tuples)
        total_views = sum(views)

        # Filter out unpopular item
        if total_views < 10:
            continue

        trend = 0

        for i, date in enumerate(dates):
            if date in POSITIVE:
                trend += views[i]

            else:
                trend -= views[i]

        print("{}\t{}\t{}\t{}\t{}".format(name, dates, views, total_views, trend))
