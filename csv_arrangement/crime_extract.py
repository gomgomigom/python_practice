from tqdm import tqdm

li_1 = []
li_2 = []
with open(
    "/Users/gom/Documents/Coding/Python/test/csv_arrangement/crime.txt",
    "r",
) as file:
    crime = ""
    for line_num, line in enumerate(tqdm(file.readlines()), start=1):
        if ":" in line:
            text = (
                line.split(":", 1)[0]
                .replace("-", "")
                .strip()
                .replace("(", "\(")
                .replace(")", "\)")
                .replace("∙", "∙?.?")
                .replace("*", "")
            )
            text_1 = rf"{text}|[가-힣]\.\s?{text}"
            text_2 = text

            li_1.append(text_1)
            li_2.append(text_2)

print(li_1)
li_1.sort(key=len, reverse=True)
for i in li_1:
    print(i, len(i))

result_text_1 = "|".join(li_1)
print(result_text_1)

li_2.sort(key=len, reverse=True)
result_text_2 = "|".join(li_2)

with open(
    "/Users/gom/Documents/Coding/Python/test/csv_arrangement/crime_extract.txt",
    "w",
) as f:
    f.write(result_text_1)

with open(
    "/Users/gom/Documents/Coding/Python/test/csv_arrangement/crime_extract_2.txt",
    "w",
) as f:
    f.write(result_text_2)
