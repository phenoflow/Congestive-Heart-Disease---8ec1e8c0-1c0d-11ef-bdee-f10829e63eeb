# Victor W Zhong, Juhaeri Juhaeri, Stephen R Cole, Christian M Shay, Carolyn A Chew-Graham, Penny Gordon-Larsen, Evangelos Kontopantelis, Elizabeth J Mayer-Davis, 2024.

import sys, csv, re

codes = [{"code":"G58z.00","system":"readv2"},{"code":"8CMK.00","system":"readv2"},{"code":"G58..00","system":"readv2"},{"code":"G580.00","system":"readv2"},{"code":"14A6.00","system":"readv2"},{"code":"G234.00","system":"readv2"},{"code":"8CeC.00","system":"readv2"},{"code":"1O1..00","system":"readv2"},{"code":"G580100","system":"readv2"},{"code":"G232.00","system":"readv2"},{"code":"8CMW800","system":"readv2"},{"code":"8CL3.00","system":"readv2"},{"code":"G580400","system":"readv2"},{"code":"8H2S.00","system":"readv2"},{"code":"14AM.00","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('congestive-heart-disease-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["congestive-heart-disease-failure---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["congestive-heart-disease-failure---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["congestive-heart-disease-failure---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
