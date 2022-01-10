import os
import csv

total_votes = 0
candwvotes_list = ['Khan', 'Correy', 'Li', "O'Tooley"]
khan_total = 0
correy_total = 0
li_total = 0
otooley_total = 0

csv_path = os.path.join('Resources', 'election_data.csv')

#Read in CSV
with open(csv_path) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csvheader = next(csvreader)
    
    #For loop to iterate through rows and calculate election metrics
    for row in csvreader:
        total_votes += 1
        
        if row[2]=='Khan':
            khan_total +=1
        elif row[2]=='Correy':
            correy_total +=1
        elif row[2]=='Li':
            li_total +=1
        else:
            otooley_total +=1
    
    #Calculate percentages
    khan_perc = khan_total/total_votes
    correy_perc = correy_total/total_votes
    li_perc = li_total/total_votes
    otooley_perc = otooley_total/total_votes

    perc_list = [khan_perc,correy_perc,li_perc,otooley_perc]
    winner_perc = max(perc_list)

    if winner_perc == khan_perc:
        winner = "Khan"
    elif winner_perc == correy_perc:
        winner = "Correy"
    elif winner_perc == li_perc:
        winner = "Li"
    else:
        winner = "O'Tooley"

print("Election Results")
print("-------------------------")
print("Total Votes: " + str(total_votes))
print("Khan: "+ str(khan_perc) + "with " +str(khan_total) + " votes.")
print("Correy: "+ str(correy_perc) + "with " +str(correy_total) + " votes.")
print("Li: "+ str(li_perc) + "with " +str(li_total) + " votes.")
print("O'Tooley: "+ str(otooley_perc) + "with " +str(otooley_total) + " votes.")
print("-------------------------")
print("The Winner is: "+ str(winner))
print("-------------------------")

text_file_path = os.path.join('Resources', 'Election_Results.txt')

with open(text_file_path, 'w') as newtxt:
    newtxt.write("Election Results")
    newtxt.write('\n')
    newtxt.write("-------------------------")
    newtxt.write('\n')
    newtxt.write("Total Votes: " + str(total_votes))
    newtxt.write('\n')
    newtxt.write("Khan: "+ str(khan_perc) + "with " +str(khan_total) + " votes.")
    newtxt.write('\n')
    newtxt.write("Correy: "+ str(correy_perc) + "with " +str(correy_total) + " votes.")
    newtxt.write('\n')
    newtxt.write("Li: "+ str(li_perc) + "with " +str(li_total) + " votes.")
    newtxt.write('\n')
    newtxt.write("O'Tooley: "+ str(otooley_perc) + "with " +str(otooley_total) + " votes.")
    newtxt.write('\n')
    newtxt.write("-------------------------")
    newtxt.write('\n')
    newtxt.write("The Winner is: "+ str(winner))
    newtxt.write('\n')
    newtxt.write("-------------------------")
   
    




