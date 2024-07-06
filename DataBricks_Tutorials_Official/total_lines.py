from pathlib import Path

location=Path.cwd().joinpath(
    "DataBricks_Tutorials_Official"
    ).glob("[1-9]*.txt")
lineCount=0
for file in location:
    # print(file)
    with file.open(mode="r", encoding="utf-8") as readFile:
        page=readFile.readlines()
        lineCount+=len(page)
print(lineCount)