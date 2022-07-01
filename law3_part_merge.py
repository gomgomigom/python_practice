import pandas as pd
import glob
import os
from tqdm import tqdm


def part_merge(input_file, output_file, ext):
    allFile_list = glob.glob(os.path.join(input_file, f"*.{ext}"))

    allData = []
    for file in tqdm(allFile_list):
        df = pd.read_csv(file)
        allData.append(df)

    dataCombine = pd.concat(allData, axis=0, ignore_index=True)
    dataCombine.to_csv(output_file, index=False)


if __name__ == "__main__":
    input_file = "./pdf_hwp/"
    output_file = "./csv_merge/court.csv"
    ext = "csv"
    part_merge(input_file, output_file, ext)
