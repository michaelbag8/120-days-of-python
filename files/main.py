import zipfile
import csv

to_zip = [
"file1.txt",
"file2.txt",
"file3.txt",
"file4.txt",
"file5.txt",
"file6.txt",
"file7.txt",
"file8.txt",
"file9.txt",
"file10.txt"
]


add_zip = [
"sample1.txt",
"sample2.txt",
"sample3.txt",
"sample4.txt",
"sample5.txt",
"sample6.txt",
"sample7.txt",
"sample8.txt",
"sample9.txt",
"sample10.txt"
]
def create_zip(zipf, files, opt):
    with zipfile.ZipFile(zipf, opt, allowZip64=True) as archive:
        for file in files:
            archive.write(file)

#create_zip("./tests.zip", to_zip, "w")


def add_to_zip(zipf, files, opt):
    with zipfile.ZipFile(zipf, opt) as archive:
        for file in files:
            lst = archive.namelist()
            if not file in lst:
                archive.write(file)
            else:
                print(f"file exists in zip file {file}")
    
#add_to_zip("./tests.zip", add_zip, "a")


def read_zip(zipf):
    with zipfile.ZipFile(zipf, "r") as archive:
        lst = archive.namelist()
        for file in lst:
            zfinf = archive.getinfo(file)
            print(f"{file} => {zfinf.file_size} bytes {zfinf.compress_size} compressed")

#read_zip("./tests.zip")

def extract_file(zipf, filename, path):
    with zipfile.ZipFile(zipf, "r") as archive:
        archive.extract(filename, path=path)


#extract_file("./tests.zip", "sample2.txt", "extract")


def extract_all(zipf, path):
    with zipfile.ZipFile(zipf, "r") as archive:
        archive.extractall(path=path)


#extract_all("./tests.zip", "extract_all")


def read_csv(fn, delimiter):
    with open(fn) as csv_f:
        counter = -1
        rows = csv.reader(csv_f, delimiter=delimiter)
        for row in rows:
            if counter == -1:
                print(f'{" | ".join(row)}')
            else:
                print(f"{row[0]} | {row[1]} | {row[2]} ")
            counter += 1
        print(f"{counter} lines")


#read_csv("names.csv", ",")


def write_csv(fn, header, row):
    with open(fn , mode="w", newline="") as csv_f:
        writer = csv.writer(csv_f, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(header)
        writer.writerow(row)

write_csv("names2.csv", ["name", "campus", "cohort"], ["Tempest", "Otukpo", "February"])