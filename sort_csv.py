import pandas as pd


def sort_csv(file_path, column_name):
    df = pd.read_csv(file_path)
    df.sort_values(by=column_name).to_csv(file_path, index=False)


if __name__ == "__main__":
    file_path = "./error_list/error_list_merge_remove_none.csv"
    column_name = "seqnum"
    sort_csv(file_path, column_name)
