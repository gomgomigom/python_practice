from tqdm import tqdm

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
            )
            if line_num == 1:
                crime += text
            crime += "|" + text
            print(text)
print(crime)

with open(
    "/Users/gom/Documents/Coding/Python/test/csv_arrangement/crime_extract.txt",
    "w",
) as f:
    f.write(crime)

with open("./crime_extract.txt", "w") as f:
    f.write(crime)
