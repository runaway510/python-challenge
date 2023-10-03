import os
import csv


csv_path = os.path.join("...", "Resources","budget_data.csv")
csv_output = os.path.join('..', 'Analysis', 'Analysis.txt')

#variables
month_count = 0
profit_losses = 0
profit_losses_change = []
profit_increase = [] 
profit_decrease = []
current_month = 0
previous_month = 0
net_profit_loss = 0

with open(csv_path) as csvfile:
    csvreader = csv.reader(csvfile,)

    next(csvfile)

    for row in csvreader:
#Total months
        month_count = (month_count + 1)
#The net total amount of 'Profit/Losses' over the entire period 
        profit_losses_net = int(row[1])
        net_profit_loss += profit_losses

#The changes in 'Profit/Losses' over the entire period, and then the average of those changes
    
         
        profit_losses_change.append(current_month-previous_month) 
        
          


               


    print (month_count)
    print (profit_losses_net)