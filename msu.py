import pandas as pd 
import os
import os.path

# The webpage URL whose table we want to extract 
url = [
"https://cpk.msu.ru/rating/dep_01",
"https://cpk.msu.ru/rating/dep_02",
"https://cpk.msu.ru/rating/dep_03",
"https://cpk.msu.ru/rating/dep_04",
"https://cpk.msu.ru/rating/dep_05",
"https://cpk.msu.ru/rating/dep_06",
"https://cpk.msu.ru/rating/dep_07",
"https://cpk.msu.ru/rating/dep_08",
"https://cpk.msu.ru/rating/dep_09",
"https://cpk.msu.ru/rating/dep_10",
"https://cpk.msu.ru/rating/dep_11",
"https://cpk.msu.ru/rating/dep_12",
"https://cpk.msu.ru/rating/dep_13",
"https://cpk.msu.ru/rating/dep_14",
"https://cpk.msu.ru/rating/dep_15",
"https://cpk.msu.ru/rating/dep_16",
"https://cpk.msu.ru/rating/dep_17",
"https://cpk.msu.ru/rating/dep_18",
"https://cpk.msu.ru/rating/dep_19",
"https://cpk.msu.ru/rating/dep_20",
"https://cpk.msu.ru/rating/dep_21",
"https://cpk.msu.ru/rating/dep_22",
"https://cpk.msu.ru/rating/dep_25",
"https://cpk.msu.ru/rating/dep_26",
"https://cpk.msu.ru/rating/dep_27",
"https://cpk.msu.ru/rating/dep_28",
"https://cpk.msu.ru/rating/dep_29",
"https://cpk.msu.ru/rating/dep_30",
"https://cpk.msu.ru/rating/dep_31",
"https://cpk.msu.ru/rating/dep_32",
"https://cpk.msu.ru/rating/dep_33",
"https://cpk.msu.ru/rating/dep_34",
"https://cpk.msu.ru/rating/dep_35",
"https://cpk.msu.ru/rating/dep_36",
"https://cpk.msu.ru/rating/dep_37",
"https://cpk.msu.ru/rating/dep_39",
"https://cpk.msu.ru/rating/dep_88",
"https://cpk.msu.ru/rating/dep_90"
]

# Create separeted directory for every URL
for i in url:
    os.mkdir(i[-6:])
    name = str(i[-6:])
    
    # Print name that we will use as a directory name 
    print(name)

    # Assign the tables data to a Pandas dataframe 
    table = pd.read_html(i)

    # Calculate how many table have we found on this page
    print("found " + str(len(table)) + " elements in directory " + name + "\n")

    # Set tables counter to 0 and use it as part of file names
    seq = 0

    # Generate XLSX files for every table and store it into dir by their positions in HTML
    for i in table:
        seq += 1
        i.to_excel("/Users/alardus/work/" + name +  "/data_" + str(seq) + ".xlsx")
