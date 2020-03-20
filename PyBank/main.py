import os
import csv

PyBank_csv = os.path.join("Resources","budget_data.csv")

profit = []
monthly_changes = []
date = []
 
count = 0
total = 0
total_change = 0
initial_profit = 0

with open(PyBank_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    for row in csvreader:    
      count = count + 1 
      date.append(row[0])
      profit.append(row[1])
      total = total + int(row[1])
      final_profit = int(row[1])
      monthly_change_total = final_profit - initial_profit
      monthly_changes.append(monthly_change_total)

      total_change = total + monthly_change_total
      initial_profit = final_profit
      average_change = (total_change/count)
      
      most_increase = max(monthly_changes)
      most_decrease = min(monthly_changes)

      increase_date = date[monthly_changes.index(most_increase)]
      decrease_date = date[monthly_changes.index(most_decrease)]
      
    print("Financial Analysis")
    print("----------------------------------------------------------")
    print("Total Months: " + str(count))
    print("Total: " + "$" + str(total))
    print("Average Change: " + "$" + str(int(average_change)))
    print("Greatest Increase in Profits: " + str(increase_date) + " ($" + str(most_increase) + ")")
    print("Greatest Decrease in Profits: " + str(decrease_date) + " ($" + str(most_decrease)+ ")")

    with open('PyBank_analysis.txt', 'w') as text:
      text.write("Financial Analysis"+ "\n")
      text.write("----------------------------------------------------------\n\n")
      text.write("Total Months: " + str(count) + "\n")
      text.write("Total: " + "$" + str(total) +"\n")
      text.write("Average Change: " + '$' + str(int(average_change)) + "\n")
      text.write("Greatest Increase in Profits: " + str(increase_date) + " ($" + str(most_increase) + ")\n")
      text.write("Greatest Decrease in Profits: " + str(decrease_date) + " ($" + str(most_decrease) + ")\n")
