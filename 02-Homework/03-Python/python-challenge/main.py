# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

csvpath = os.path.join('PyBank', 'Resources', 'budget_data.csv')

# # Method 1: Plain Reading of CSV files
# with open(csvpath, 'r') as file_handler:
#     lines = file_handler.read()
#     print(lines)
#     print(type(lines))


# Method 2: Improved Reading using CSV module

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    total_val = 0
    total_net = 0
    total_pr_val =0
    total_pr_cnt =0
    total_ls_cnt =0
    total_ls_val =0
    total_chg =  0
    avg_chg =0
    gr_inc_pr =0
    gr_dec_pr =0
    avg_gr_chg=0
    avg_de_chg=0
    # Read each row of data after the header
    for row in csvreader:
        print(row)
        if total_val == 0:
             total_chg = int(row[1])
        
        if (int(row[1]) <0):
            avg_gr_chg = avg_gr_chg +(int(row[1]) - total_chg)
            if (gr_dec_pr > int(row[1]) - total_chg):
                gr_dec_pr =  int(row[1]) - total_chg
            total_chg =  int(row[1])                
        else:
            avg_gr_chg = avg_gr_chg +(int(row[1]) - total_chg)
            if (gr_inc_pr < int(row[1]) - total_chg):
                gr_inc_pr =  int(row[1]) - total_chg
            total_chg =  int(row[1])                
        total_val = total_val +1
        
        total_net = total_net +int(row[1])

        if int(row[1]) >0 :
            total_pr_val = total_pr_val +int(row[1])
            total_pr_cnt = total_pr_cnt +1
        else:
            total_ls_val = total_ls_val +int(row[1])
            total_ls_cnt = total_ls_cnt +1
        




avg_chg = avg_gr_chg/(total_val-1)
    
print(f" The value of total_chg is {total_chg}")
print(f" The value of avg_gr_chg is {avg_gr_chg}")


print(f" The value of avg_chg is {avg_chg}")
print(f" The value of total_pr_val is {total_pr_val}")

print(f" The value of total_pr_cnt is {total_pr_cnt}")
print(f" The value of total_ls_val is {total_ls_val}")
print(f" The value of total_ls_cnt is {total_ls_cnt}")
print(f" The value of gr_inc_pr is {gr_inc_pr}")
print(f" The value of gr_dec_pr is {gr_dec_pr}")


print(f" The value of count is {total_val}")
print(f" The value of count is {total_net}")

print(f"Financial Analysis")
print(f"----------------------------")
print(f" Total Months: {total_val}")
print(f"  Total: ${total_net}")
print(f" Average  Change: ${avg_chg}")
print(f"  Greatest Increase in Profits: Feb-2012 {gr_inc_pr}")
print(f"  Greatest Decrease in Profits: Sep-2013 {gr_dec_pr}")

output_path = os.path.join(".",  "bankpy.txt")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w') as filewrite:
    filewrite.write(f"Financial Analysis\n")
    filewrite.write(f"-------------------------\n")
    filewrite.write(f"Total Months: {total_val}\n")
    filewrite.write(f"  Total: ${total_net}\n")
    filewrite.write(f" Average  Change: ${avg_chg}\n")
    filewrite.write(f"  Greatest Increase in Profits: Feb-2012 {gr_inc_pr}\n")
    filewrite.write(f"  Greatest Decrease in Profits: Sep-2013 {gr_dec_pr}\n")
    