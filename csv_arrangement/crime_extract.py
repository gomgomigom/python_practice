with open(
    "/Users/gom/Documents/Coding/Python/test/csv_arrangement/crime.txt",
    "r",
) as file:
    crime = ""
    for line in file.readlines():
        if ":" in line:
            text = line.split(":", 1)[0].replace("-", "").strip()
            crime += "|" + text
            print(text)
crime = crime[1:]
print(crime)

with open(
    "/Users/gom/Documents/Coding/Python/test/csv_arrangement/crime_extract.txt",
    "w",
) as f:
    f.write(crime)

with open("./crime_extract.txt", "w") as f:
    f.write(crime)
