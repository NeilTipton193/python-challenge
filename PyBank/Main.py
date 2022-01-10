import os
import csv

total_months = 0
net_profit = 0
profit_change = []
num_months = []
greatest_inc = 0
greatest_inc_month = 0
greatest_dec = 0
greatest_dec_month = 0

# create path

csv_path = os.path.join('Resources','budget_data.csv')

with open(csv_path, 'r') as csvfile:
    # read in csv
    file_reader = csv.reader(csvfile, delimiter = ',')
    header = next(file_reader)
    print(f"CSV Header is: {header}")
    row = next(file_reader)
    print(str(row))
    
    #Update Variables with values for first row
    total_months += 1
    net_profit += int(row[1])
    previous_row = int(row[1])
    greatest_inc = int(row[1])
    greatest_inc_month = row[0]

#For Loop to iterate through rows and update metrics
    for row in file_reader:

        total_months +=1
        net_profit += int(row[1])
        change_by_month = int(row[1])-previous_row
        profit_change.append(change_by_month)

        #Calculate greatest decrease:
        if int(row[1]) < greatest_dec:
            greatest_dec = int(row[1])
            greatest_dec_month = row[0]

        #Calculate greatest increase
        if int(row[1]) > greatest_inc:
            greatest_inc = int(row[1])
            greatest_inc_month = row[0]

#adding final required metrics
avg_profit_change = sum(profit_change)/len(profit_change)
max_profit_change = max(profit_change)
min_profit_change = min(profit_change)

#print results
print("Results of Financial Analysis")
print("------------------------------")
print("Total Months: " + str(total_months))
print("Total Profit/Loss: " + str(net_profit))
print("Average Change: " + str(avg_profit_change))
print("Greatest Increase in Profits: " + str(max_profit_change))
print("Greatest Decrease in Profits: " + str(min_profit_change))

text_path = os.path.join('Resources', 'PybankResults.txt')

#Write to new text file
with open(text_path,'w') as text:
    text.write("Results of Financial Analysis")
    text.write('\n')
    text.write("------------------------------")
    text.write('\n')
    text.write("Total Months: " + str(total_months))
    text.write('\n')
    text.write("Total Profit/Loss: " + str(net_profit))
    text.write('\n')
    text.write("Average Change: " + str(avg_profit_change))
    text.write('\n')
    text.write("Greatest Increase in Profits: " + str(max_profit_change))
    text.write('\n')
    text.write("Greatest Decrease in Profits: " + str(min_profit_change))
    




    


