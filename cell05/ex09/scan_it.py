
import sys
import re

if len(sys.argv) != 3:
    print("none")
    sys.exit()

keyword = sys.argv[1]
string_to_search = sys.argv[2]

matches = re.findall(re.escape(keyword), string_to_search)

if len(matches) == 0:
    print("none")
else:
    print(len(matches))
