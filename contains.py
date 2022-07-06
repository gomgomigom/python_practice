import pandas as pd
from tqdm import tqdm


def find_value_in_column(input_file, output_file, want_column, find_value):
    df = pd.read_csv(input_file)
    df = df[df[want_column].str.contains(find_value, na=False)]
    print(df)
    df.to_csv(output_file, index=False)


if __name__ == "__main__":
    input_file = "./warehouse/court_GO.csv"
    output_file = "./warehouse/OCR.csv"
    want_column = "file_body"
    find_value = "RequiredOCR"
    find_value_in_column(input_file, output_file, want_column, find_value)
