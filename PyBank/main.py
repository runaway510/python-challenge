import os
import csv

# join path
csv_path = os.path.abspath(os.path.join("Resources", "budget_data.csv"))
csv_output = os.path.abspath(os.path.join('Analysis', 'Analysis.txt'))

# open and read csv
with open(csv_path, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    print(f"Header: {csv_header}")
    
    # find net amount of profit and loss
    Profit_Losses = []
    months = []

    # read each row of data after header
    for rows in csvreader:
        Profit_Losses.append(int(rows[1]))
        months.append(rows[0])

    # find total change
    total_change =[]

    for x in range(1, len(Profit_Losses)):
        total_change.append((int(Profit_Losses[x]) - int(Profit_Losses[x-1])))

    # calculate average  change
    avg_change = sum(total_change) / len(total_change)
    revenue_average = round(avg_change, 2)

    # calculate total length of months
    total_months = len(months)

    # greatest increase 
    greatest_increase = max(total_change)

    #greatest decrease 
    greatest_decrease = min(total_change)


    # print Results
    
    print ("Financial Analysis")

    print("....................................................................................")

    print ("Total Months:" + str(total_months))

    print("Total:" + "$" + str(sum(Profit_Losses)))

    print ("Average Change:" + "$" + str(revenue_average))

    print("Greatest Increase in Profits: " + str(months[total_change.index(max(total_change))+1]) + " " + "($" + str(greatest_increase) + ")")

    print("Greatest Decrease in Profits: " + str(months[total_change.index(min(total_change))+1]) + " " + "($" + str(greatest_decrease) + ")")


    # output to a text file
    file = open(csv_output,"w")

    file.write("Financial Analysis" + "\n")

    file.write("----------------------------" + "\n")

    file.write("Total Months: " + str(total_months) + "\n")

    file.write("Total: " + "$" + str(sum(Profit_Losses)) + "\n")

    file.write("Average change: " + "$" + str(revenue_average) + "\n")

    file.write("Greatest Increase in Profits: " + str(months[total_change.index(max(total_change))+1]) + " " + "($" + str(greatest_increase) + ")\n")

    file.write("Greatest Decrease in Profits: " + str(months[total_change.index(min(total_change))+1]) + " " + "($" + str(greatest_decrease) + ")\n")

    file.close()