# Tim Doran, Evangelos Kontopantelis, Jose M Valderas, Stephen Campbell, Martin Roland, Chris Salisbury, David Reeves, 2024.

import sys, csv, re

codes = [{"code":"C108E12","system":"readv2"},{"code":"66AJ200","system":"readv2"},{"code":"66A7100","system":"readv2"},{"code":"C109D12","system":"readv2"},{"code":"C108E00","system":"readv2"},{"code":"C10EE00","system":"readv2"},{"code":"C10FD00","system":"readv2"},{"code":"66AJ000","system":"readv2"},{"code":"C109D00","system":"readv2"},{"code":"C109D11","system":"readv2"},{"code":"66AJ300","system":"readv2"},{"code":"C108E11","system":"readv2"},{"code":"250 HC","system":"readv2"},{"code":"250 E","system":"readv2"},{"code":"250 ED","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('diabetes-mellitus-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["diabetes-mellitus-hypoglycaemia---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["diabetes-mellitus-hypoglycaemia---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["diabetes-mellitus-hypoglycaemia---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
