import pandas as pd

df = pd.read_csv("./warehouse/test.csv")
regex = df["file_body"].str.extractall(
    r"\d{4}[ㄱ-ㅎ|ㅏ-ㅣ|가-힣]{1,2}\d{1,4}\,*\s*([0-9ㄱ-ㅎㅏ-ㅣ가-힣\(\)\s\,\.\·]+)(?=피\s*고\s*인)"
)
print(regex)

df["죄명"] = regex[0]
test_df = df
print(df)


col1 = test_df.columns[-2:].to_list()
col2 = test_df.columns[:-2].to_list()
new_col = col1 + col2
print(new_col)
test_df = test_df[
    ["사건번호", "죄명", "file_body", "seqnum", "url", "제목", "법원", "내용", "file_name"]
]
# print(test_df)
test_df.to_csv("./warehouse/test_regex.csv", index=False)

# regex = (
#     df["file_body"]
#     .str.extract(
#         r"\d{4}[ㄱ-ㅎ|ㅏ-ㅣ|가-힣]{1,2}\d{1,4}\s*(\b[ㄱ-ㅎㅏ-ㅣ가-힣][0-9ㄱ-ㅎㅏ-ㅣ가-힣\(\)\s\,\.\·]+)(?=피\s*고\s*인)",
#         expand=False,
#     )
#     .str.strip()
#     .str.replace(r"\s", "")
# )
