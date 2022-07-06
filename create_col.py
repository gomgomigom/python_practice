import pandas as pd

df = pd.read_csv("./warehouse/test.csv")
regex = (
    df["file_body"]
    .str.split(pat=r"피\s*고\s*인", n=1, expand=True)[0]
    .str.split(pat=r"\d{4}[가-힣]{1,2}\d{1,4}", n=1, expand=True)[1]
    .replace(
        to_replace=r"[0-9]|\(병합\)|\,|고단|고정|고합|\(분리\)|[가나다라마바사]\.|\-|○|\:|선고기일|\.",
        value="",
        regex=True,
    )
    .replace(to_replace=r"\s{2,}", value=" ", regex=True)
    .str.strip()
    .str.split(pat=r"\s")
)

print(regex)
print(type(regex))
df["죄명"] = regex
print(df)


# col1 = test_df.columns[-2:].to_list()
# col2 = test_df.columns[:-2].to_list()
# new_col = col1 + col2
# print(new_col)
df = df[
    ["사건번호", "죄명", "file_body", "seqnum", "url", "제목", "법원", "내용", "file_name"]
]
# print(test_df)
print(df.iloc[:, 1][0])
for i in df.iloc[:, 1][0]:
    print(f"iloc:{i}".format(i))
print(df.loc[:, "죄명"][0])
for i in df.loc[:, "죄명"][0]:
    print(f"loc: {i}")
df.to_csv("./warehouse/test_regex.csv", index=False)

# regex = (
#     df["file_body"]
#     .str.extract(
#         r"\d{4}[ㄱ-ㅎ|ㅏ-ㅣ|가-힣]{1,2}\d{1,4}\s*(\b[ㄱ-ㅎㅏ-ㅣ가-힣][0-9ㄱ-ㅎㅏ-ㅣ가-힣\(\)\s\,\.\·]+)(?=피\s*고\s*인)",
#         expand=False,
#     )
#     .str.strip()
#     .str.replace(r"\s", "")
# )

# r"\d{4}[ㄱ-ㅎㅏ-ㅣ가-힣]{1,2}\d{1,4}\,*\s*([0-9ㄱ-ㅎㅏ-ㅣ가-힣\(\)\s\,\.\·]+)(?=피\s*고\s*인)"


#   r"(교통사고처리특례법위반|도로교통법위반|사기|폭행|상해|협박|횡령|배임|명예훼손|모욕|강간|추행|청소년의성보호에관한법률위반|성폭력범죄의처벌등에관한특례법위반|음란물유포|손괴|은닉|파괴|문화재보호법위반|절도|강도|불법사용|점유이탈물횡령|폭력행위등처벌에관한법률위반|특정범죄가중처벌등에관한법률위반|특정경제범죄가중처벌등에관한법률위반)(?=피\s*고\s*인)"
