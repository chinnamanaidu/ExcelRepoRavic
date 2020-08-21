# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

import textwrap

csvpath = os.path.join('PyPoll', 'Resources', 'election_data.csv')

# # Method 1: Plain Reading of CSV files
# with open(csvpath, 'r') as file_handler:
#     lines = file_handler.read()
#     print(lines)
#     print(type(lines))


# Method 2: Improved Reading using CSV module

total_val = 0
total_net = 0
total_pr_val =0
total_pr_cnt =0
total_ls_cnt =0
total_ls_val =0
total_chg =  ""
avg_chg =0
gr_inc_pr =0
gr_dec_pr =0
avg_gr_chg=0
avg_de_chg=0
name_list = []
val_found = True
dist_name = []
dist_vote_cnt = []
dist_vote_per_cnt = []
str_namein = ""
len_val = 0
each_vote = 0
winner_index=0

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
   

    print(csvreader)

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
    


    # Read each row of data after the header
    for row in csvreader:
        #print(str(row[2]))          
        name_list.append(str(row[2]))            
        total_val = total_val +1



for strval in name_list:
    if len(dist_name) >0:
        for st in dist_name:            
            if st == strval:
                val_found = False
                break  
    if val_found == True:
        dist_name.append(strval)
    val_found = True



#    print(f" the val of strval is {str(strval)}")

for stval in dist_name:
    each_vote = 0
    with open(csvpath) as csvfile:

        # CSV reader specifies delimiter and variable that holds contents
        csvreader = csv.reader(csvfile, delimiter=',')
        for row in csvreader:       
            if stval == str(row[2]):           
                each_vote = each_vote +1
    dist_vote_cnt.append(str(each_vote))
    

print(dist_name)
for strvalForName in dist_name:
    print(f" The value of strvalForName is {strvalForName}")

vot_cnt =0
vot_ind =0
print(dist_vote_cnt)
for strvalForName in dist_vote_cnt:
    if (int(strvalForName)>vot_cnt):
        vot_ind = vot_ind+1
        vot_cnt = int(strvalForName)
    print(f" The value of strvalForName is {strvalForName}") 
    dist_vote_per_cnt.append(float((int(strvalForName)/int(total_val)) *100))
print(dist_vote_per_cnt)
print(vot_ind)
print(f" The value of total_val is {total_val}")
print(f" The value of count is {total_net}")

print(f"Financial Analysis")
print(f"----------------------------")
print(f" The total number of votes cast: {total_val}")
print(f"  Total: ${total_val}")
print(f" Average  Change: ${avg_chg}")
print(f"  Greatest Increase in Profits: Feb-2012 {gr_inc_pr}")
print(f"  Greatest Decrease in Profits: Sep-2013 {gr_dec_pr}")

print(f"Election Results")
print(f"-------------------------")
print(f"Total Votes: {total_val}")
print(f"-------------------------")
for  i in range(4):
    print(f"{dist_name[i]} {dist_vote_per_cnt[i]}% ({dist_vote_cnt[i]})")

print(f" -------------------------")
print(f"Winner: {dist_name[vot_ind-1]}")
print(f"-------------------------")

output_path = os.path.join(".",  "election.txt")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w') as filewrite:
    filewrite.write(f"Election Results\n")
    filewrite.write(f"-------------------------\n")
    filewrite.write(f"Total Votes: {total_val}\n")
    for  i in range(4):
        filewrite.write(f"{dist_name[i]} {dist_vote_per_cnt[i]}% ({dist_vote_cnt[i]})\n")
    filewrite.write(f"-------------------------\n")
    filewrite.write(f"Winner: {dist_name[vot_ind-1]}\n")
    filewrite.write(f"-------------------------\n")
    