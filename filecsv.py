import csv

# f = open('main.csv','r')
# content = csv.reader(f)
# for row in content:
#     print(row)
#
# f.close()
#  Read csv file
with open('main.csv','r') as file:
    content = csv.reader(file, delimiter='\t')
    for row in content:
        print(row)

# write csv file with single row
# with open('main.csv','w',newline= '') as file:
#     writer =csv.writer(file)
#     writer.writerow(["SN","Name","FatherName","Address","Contact"])
#     writer.writerow(['1',"Ali","Khan","baghlan","0703030101"])


# # write csv file with multiple rows
# with open('main.csv', 'w') as file:
#     row_list = [["SN", "Name", "FatherName", "Address", "Contact"],
#                 ["1", "Imran", "Khan", "kabul", "0703030303"],
#                 ["2", "Naveed", "Islam", "Laghman", "0702010310"],
#                 ['3',"Khalid","Khan","Nangarhar","070202022"]
#                 ]
#     writer = csv.writer(file, delimiter = '\t')
#     writer.writerows(row_list)
#
