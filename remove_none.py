import pandas as pd


def remove_none(input_file, output_file):
    df = pd.read_csv(input_file)
    df_drop_row = df.dropna(axis=0)
    df_drop_row.to_csv(output_file, index=False)


if __name__ == "__main__":
    input_file = "./error_list/error_list_merge.csv"
    output_file = "./error_list/error_list_merge_remove_none.csv"
    remove_none(input_file, output_file)
