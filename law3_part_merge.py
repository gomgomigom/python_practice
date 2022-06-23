import pandas as pd
import glob
import os

input_file = "./csv/"
output_file = "./csv_merge/precedent.csv"

allFile_list = glob.glob(os.path.join(input_file, "*.csv"))

print(allFile_list)

allData = []
for file in allFile_list:
    df = pd.read_csv(file)
    allData.append(df)

dataCombine = pd.concat(allData, axis=0, ignore_index=True)

dataCombine.to_csv(output_file, index=False)
