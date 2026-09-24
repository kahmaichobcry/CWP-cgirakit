import sys

if len(sys.argv) != 2:
    print("none")
    sys.exit()

text = sys.argv[1]
count = text.count("z")

if count == 0:
    print("none")
else:
    print("z" * count)
