#!/usr/bin/env python3
import sys
import urllib
from urllib.parse import urlparse

invalid_titles = ["Media", "Special", "Talk", "User", "User_talk", "Project", "Project_talk", "File", "File_talk",
                  "MediaWiki", "MediaWiki_talk", "Template", "Template_talk", "Help", "Help_talk",
                  "Category", "Category_talk", "Portal", "Wikipedia",
                  "Wikipedia_talk"]
invalid_endings = ["jpg", "gif", ".png", ".JPG", ".GIF", ".PNG", ".ico", ".txt"]
boilerplate_pages = ["404_error", "Main_Page", "Hypertext_Transfer_Protocol", "Favicon.ico", "Search"]


def is_valid(code: str, name: str) -> bool:
    # Filter out non-english project
    if code != "en":
        return False

    # Filter out page with name starting with lower case letter
    if name[0].islower():
        return False

    # Filter out items with invalid page tiles
    for invalid_title in invalid_titles:
        if name.startswith(invalid_title):
            return False

    # Filter out items with invalid format
    for invalid_ending in invalid_endings:
        if name.endswith(invalid_ending):
            return False

    # Filter out boilerplate pages
    for boilerplate_page in boilerplate_pages:
        if name == boilerplate_page:
            return False

    return True


if __name__ == "__main__":
    # Retrieve date from apache hadoop
    filepath = os.environ["map_input_file"]
    filename = os.path.split(filepath)[-1]
    date = filename.split('-')[1]

    for line in sys.stdin:
        try:
            proj_code, pagename, pageviews, totalByte = line.split()

            # Transform pagename
            pagename = urllib.parse.unquote_plus(pagename)

            # Filter out invalid pages
            if is_valid(proj_code, pagename):
                print("{}{}{}\t{}".format(pagename, '}', date, pageviews))

        # Exclude outliers like: some lines in raw data only have three fields
        except:
            continue
