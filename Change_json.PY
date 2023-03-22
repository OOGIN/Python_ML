import csv
import json
import datetime as dt

data_csv = "DATA_01.csv"
data_txt = "DATA_01.txt"

with open(data_csv,'r', encoding='utf-8', newline = "") as file_csv, \
        open(data_txt,'w', encoding='utf-8', newline = "") as file_txt:
    reader = csv.reader(file_csv)

    col_names = next(reader)
    del col_names[0]
    col_names.append('date')
    
    datetime = dt.datetime.now()
    date = datetime.date()
    for cols in reader:
        del cols[0]
        cols.append(str(date))
        #print (cols)
        doc = {col_name: col for col_name, col in zip(col_names, cols)}
        print(json.dumps(doc, ensure_ascii=False), file=file_txt)
