import os
import csv
import statistics
import calendar
#CSV path
main_csv = os.path.join("..","Resources", "budget_data.csv")

#with open as csv file:
with open(main_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    #Skip the header
    header = next(csvreader)
  
    months = []
    profit_losses = []
    net_total = []
    changes = []
    print("Financial Analysis")
    print("------------------------------")
    
    for row in csvreader:
    
        months.append(row[1])
        profit_losses.append(row[1])
    
        
    # total number of months in dataset:
    total_months = len(months)
    print(f"Total Months :", (total_months))
    
    # convert profit/loss into integer:
    profit_losses = [int(profit) for profit in profit_losses]
    net_total = sum(profit_losses)
    print(f"Total :${net_total}")
   
   # change over the entitre period:
    for i in range(1, total_months):
       change = profit_losses[i] - profit_losses[i-1]
       changes.append(change)
   
   #average change
    change = [change]
    average_change = statistics.mean(changes)
    print(f"Average Change:${average_change:.2f}")
    
    # greatest increase in profits date/amount ovet the entire period
    greatest_increase = max(changes)
    greatest_decrease = min(changes)
    print(f"Greatest Increase in Profits :${greatest_increase}")
    print(f"Greatest Decrease in Profits :${greatest_decrease}")
    
    greatest_increase_date = changes.index(greatest_increase)+1
    print(greatest_increase_date)
    
    greatest_decrease_date = changes.index(greatest_decrease)+1
    print(greatest_decrease_date)
    
   # output in in a text file:
    print("Financial Analysis", file= open("main.txt","a"))
    print("------------------------------", file = open("main.txt","a"))
    print(f"Total Months : {total_months}", file= open("main.txt","a"))
    print(f"Total :${net_total}", file =open("main.txt","a"))
    print(f"Average Change:${average_change:.2f}",file = open("main.txt","a"))
    print(f"Greatest Increase in Profits :${greatest_increase}", file= open("main.txt","a"))
    print(f"Greatest Decrease in Profits :${greatest_decrease}", file = open("main.txt","a"))
