import os
import csv
from us_state_abbrev import us_state_abbrev

with open("employee_data2.csv") as pfile:
    csv_reader = csv.reader(pfile, delimiter=',')
# adding path to new file
newBoss_data_csv = os.path.join("employee_data2.csv")

#requied lists for new csv file format
EmpID = []
FirstName= []
LastName = []
DOB =[]
SSN = []
State =[]

#opening and appending lists to new csv file in required formats
with open(newBoss_data_csv, newline='') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')
    next(csv_reader)
    for row in csv_reader:
        EmpID.append(row[0])
        firstLastNames = row[1].split(' ')


        FirstName.append(firstLastNames[0])
        LastName.append(firstLastNames[1])
        DOB.append(row[2])


        newSSN_format = "***-**-" + row[3].split("-")[2]

        SSN.append(newSSN_format)


        stateName = us_state_abbrev[row[4]]
        State.append(stateName)
#zipping all the newlyformatted files
cleanBoss_data_csv = zip(EmpID, FirstName, LastName, DOB, SSN, State)

print(cleanBoss_data_csv)

output_file = os.path.join("boss_final2.csv")
#writing to the new csvfile
with open(output_file, "w",newline="") as datafile:
    writer = csv.writer(datafile)

    writer.writerow(['EmpID','FirstName','LastName','DOB','SSN','State'])
    writer.writerows(cleanBoss_data_csv)

with open('boss_final2.csv') as csfile:
    csv_reader = csv.reader(csfile, delimiter = ',')
    for lines in csv_reader:
        print(lines)
