import os
import natsort

location = "./Microsoft_Azure_Fundamentals_Udemy/"
files = natsort.natsorted([f for f in os.listdir(location) if f.endswith("txt")])
size = len(files)
# size=9
lineCount = 0
for f in files[:size]:
    # print(f)
    if f != "acc.txt":
        with open(os.path.join(location, f)) as f:
            page = f.readlines()
            lineCount += len(page)

print(lineCount)
