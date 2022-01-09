import os
import csv

#Store Variables
count = 0
total = 0
months = []
change = []

#Set path to read csv and write txt
csvpath = os.path.join("Resources", "budget_data.csv")
file_to_output= os.path.join("Analysis", "Budget_Analysis.txt")


with open(csvpath) as csvfile:
    csvreader=csv.reader(csvfile, delimiter=",")

#store header   
    header=next(csvreader)

#for data rows in csv file
    for row in csvreader:
        #count total months/rows
        count +=1
        #Total P/L values in column
        total = total + int(row[1])
        #append months for print out 
        months.append(row[0])
        #establish P/L change by subtracting current month minus previous for each month and append
        if count != 1:
            current_change=int(row[1])- previous
            change.append(current_change)
        else: 
            change.append(0)
        previous = int(row[1])


#set index to ID change in PL and align months        
greatest_profit_index=change.index(max(change))
greatest_decrease_profit_index=change.index(min(change))
        
#print results to terminal
print("Financial Analysis")
print("----------------------------------------------")
print ("Total Months:",count)        
print ("Total: $",total)
print ("Average change: $", sum(change)/(count-1))
print("Greatest Increase in Profits: $ ",max(change),months[greatest_profit_index])
print("Greatest Decrease in Profits: $",min(change),months[greatest_decrease_profit_index])

#print results to Budget Analysis.txt
with open(file_to_output, "w") as txt_file:
    txt_file.write("Financial Analysis\n")
    txt_file.write("------------------------------------\n")
    txt_file.write(f"Total Months: {count}\n")
    txt_file.write(f"Total: ${total}\n")
    txt_file.write(f"Average change: ${sum(change)/(count-1)}\n")
    txt_file.write(f"Greatest Increase in Profits: ${max(change),months[greatest_profit_index]}\n")
    txt_file.write(f"Greatest Decrease in Profits: ${min(change),months[greatest_decrease_profit_index]}\n")
