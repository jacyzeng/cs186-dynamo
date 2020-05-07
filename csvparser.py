import csv

with open('sampleipaddress.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    f = open("boto.txt", "w")
    seen={"283383"}
    ips = {"3"}
    # f.write("\t"+"{")
    pr = '"PutRequest": {'
    pi = '"Item": { '
    # tablename = '"rasn": ['
    # f.write(tablename+"\n")
    # f.write("\t"+"{" +"\n")
    # f.write("\t"+"\t"+pr+"\n")
    # f.write("\t"+"\t"+"\t"+ pi+"\n")
    for row in csv_reader:
        if line_count == 0:
            line_count += 1
        else :
            if row[0] not in seen and row[2] not in ips:
                f.write("table.put_item("+"\n")
                f.write("Item={"+"\n")
                date = ', "date":'
                ip = ', "ip":'
                rasn = '"rasn":'
                fval = ', "f":'
                qoute = '"'
                inter = '"N": '
                string = '"S": '
                fc = "{"
                fo="}"

                # f.write("{")
                f.write( rasn+ row[2]+date+ 
                qoute+row[0]+qoute+ip + row[1]+ fval+ row[3]+"\n"+"}"+"\n"+")"+"\n")

                # f.write("\t"+"\t"+"\t"+"\t"+"{"+rasn+ fc+inter +qoute+row[2]+qoute+fo+date+ 
                    # fc+string+qoute+row[0]+qoute+fo+ip+ fc+inter+qoute + row[1] +qoute+fo+fval+fc+inter+qoute+ row[3]+qoute+fo)
    #             f.write("}," +"\n")
                line_count += 1 
    #             print(line_count%26)
    #             seen.add(row[2])
    #             # ips.add(row[2])
    #             line_count=line_count+1
    #             if line_count%25==0:
    #                 f.write("\t"+"\t"+"\t"+"\t"+ "}" +"\n")
    #                 f.write("\t"+"\t"+"}" +"\n")
    #                 f.write("\t"+"}," +"\n")
    #                 f.write("\t"+"{" +"\n")
    #                 f.write("\t"+"\t"+pr+"\n")
    #                 f.write("\t"+"\t"+"\t"+ pi+"\n")
    #             # if line_count/26==0:
    #             #     print(line_count)
    #             #     f.write("\t"+"\t"+"\t"+"\t"+ "}" +"\n")
    #             #     f.write("\t"+"\t"+"}" +"\n")
    # f.write("\t"+"\t"+"\t"+"\t"+ "}" +"\n")
    # f.write("\t"+"\t"+"}" +"\n")
    # f.write("\t"+"}," +"\n")
    # f.write("]" +"\n")

    print(line_count)