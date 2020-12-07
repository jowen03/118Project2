#!/usr/bin/env python3
import sys
from collections import defaultdict

web_dict = defaultdict(int)

if __name__ == "__main__":
    # Aggregate from mapper result
    for line in sys.stdin:
        try:
            key, value = line.split()
            web_dict[key] += int(value)

        except:
            continue

    for key, value in web_dict.items():
        print("{} {}".format(key, value))
