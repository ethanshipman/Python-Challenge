import os
import csv

# Used relative paths for accessing the CSV file and saving the output
data_path = os.path.join('PyBank', 'Resources', 'budget_data.csv')
output_path = os.path.join('PyBank', 'analysis', 'financial_analysis.txt')

# Initialize variables
total_months = 0
net_total = 0
previous_profit_loss = None
changes = []
dates = []
greatest_increase = {"Date": None, "Amount": float('-inf')}
greatest_decrease = {"Date": None, "Amount": float('inf')}

# Open the CSV file from the relative path
with open(data_path, mode='r') as file:
    csvreader = csv.reader(file)
    
    
    header = next(csvreader)
    
    # Loop through each row of the CSV
    for row in csvreader:
        date = row[0]
        profit_loss = int(row[1])
        
        # Count the total number of months
        total_months += 1
        
        # Calculate the net total amount of "Profit/Losses"
        net_total += profit_loss
        
        # Tracking changes in "Profit/Losses" between months
        if previous_profit_loss is not None:
            change = profit_loss - previous_profit_loss
            changes.append(change)
            dates.append(date)

            # Checked for the greatest increase in profits
            if change > greatest_increase["Amount"]:
                greatest_increase = {"Date": date, "Amount": change}

            # Checked for the greatest decrease in profits
            if change < greatest_decrease["Amount"]:
                greatest_decrease = {"Date": date, "Amount": change}
        
        
        previous_profit_loss = profit_loss

# Calculates the average change
average_change = sum(changes) / len(changes) if changes else 0

# Prepared the analysis summary
analysis = (
    f"Financial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Net Total: ${net_total}\n"
    f"Average Change: ${average_change:.2f}\n"
    f"Greatest Increase in Profits: {greatest_increase['Date']} (${greatest_increase['Amount']})\n"
    f"Greatest Decrease in Profits: {greatest_decrease['Date']} (${greatest_decrease['Amount']})\n"
)

# Print the analysis to the terminal
print(analysis)

# Exported the analysis to a text file in the "analysis" folder using the relative path
with open(output_path, 'w') as file:
    file.write(analysis)