import os
import csv
import operator
import collections


print("Election Results")
print("__________________________________")

with open("election_data_2.csv") as pfile:
    csv_reader = csv.reader(pfile, delimiter = ',')

total_election_data_csv = os.path.join("election_data_2.csv")

total_votes_cnt = 0
with open(total_election_data_csv, newline ="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader, None)
    for row in csvreader:
       total_votes_cnt == row[0]
       total_votes_cnt = total_votes_cnt +1
    print("Total Votes are : " + str(total_votes_cnt))
print("_________________________________")

with open(total_election_data_csv, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter =",")
    next(csvreader, None)
    list_o_candidates = []
    for rows in csvreader:
        list_o_candidates.append(rows[2])
with open(total_election_data_csv, "r")as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    sort = sorted(list_o_candidates, key = operator.itemgetter(0))
    counter = collections.Counter(list_o_candidates)

    for (k, v) in counter.items():
        percent_votes = round((int(v)/int(total_votes_cnt)*100), 1)
        print(k, ":%s %%\n"% percent_votes,"(",v,")")
    print("___________________________________")

    inverse = [(value,key) for key, value in counter.items()]
    print("Winner is  " + (max(inverse)[1]))
print("___________________________________")
