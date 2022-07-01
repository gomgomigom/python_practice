import pandas as pd


def remove_duplicates(file_path, columns):
    df = pd.read_csv(file_path).drop_duplicates(columns, keep="first")
    df.to_csv(file_path, index=False)


if __name__ == "__main__":
    file_path = "./error_list/error_list_merge_remove_none.csv"
    columns = "seqnum"

    remove_duplicates(file_path, columns)
