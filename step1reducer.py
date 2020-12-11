#!/usr/bin/env python3
import sys


if __name__ == "__main__":
    cur_key = ""
    count = 0

    # Aggregate from mapper result but don't put all (key, value) in only one place, because the intermediate data are
    # sorted by their key
    for line in sys.stdin:
        try:
            key, val = line.split()

            if key != cur_key:
                if cur_key:
                    print("{} {}".format(cur_key, count))

                count = 0
                cur_key = key

            count += int(val)

        except:
            continue

    # Output the last item out from step1 reducer
    if count:
        print("{} {}".format(cur_key, count))
