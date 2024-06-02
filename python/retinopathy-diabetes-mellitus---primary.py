# Tim Doran, Evangelos Kontopantelis, Jose M Valderas, Stephen Campbell, Martin Roland, Chris Salisbury, David Reeves, 2024.

import sys, csv, re

codes = [{"code":"2BBo.00","system":"readv2"},{"code":"F420.00","system":"readv2"},{"code":"C109611","system":"readv2"},{"code":"F420z00","system":"readv2"},{"code":"C10E700","system":"readv2"},{"code":"C10F600","system":"readv2"},{"code":"C109612","system":"readv2"},{"code":"C108711","system":"readv2"},{"code":"C108712","system":"readv2"},{"code":"C10F611","system":"readv2"},{"code":"250 C","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('diabetes-mellitus-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["retinopathy-diabetes-mellitus---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["retinopathy-diabetes-mellitus---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["retinopathy-diabetes-mellitus---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
