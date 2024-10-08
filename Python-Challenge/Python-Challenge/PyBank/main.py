import os
import csv

# Define the base directory (where your script is located)
base_dir = '/Users/EthanShipman/Desktop/school/Python-Challenge/Python-Challenge/PyBank'
data_path = os.path.join(base_dir, 'Resources', 'budget_data.csv')

# Initialize variables
total_months = 0
net_total = 0
previous_profit_loss = None
changes = []
dates = []
greatest_increase = {"Date": None, "Amount": float('-inf')}
greatest_decrease = {"Date": None, "Amount": float('inf')}

# Open the CSV file from the specified path
with open(data_path, mode='r') as file:
    csvreader = csv.reader(file)
    
    # Skip the header row
    header = next(csvreader)
    
    # Loop through each row of the CSV
    for row in csvreader:
        date = row[0]
        profit_loss = int(row[1])
        
        # Count the total number of months
        total_months += 1
        
        # Calculate the net total amount of "Profit/Losses"
        net_total += profit_loss
        
        # Track changes in "Profit/Losses" between months
        if previous_profit_loss is not None:
            change = profit_loss - previous_profit_loss
            changes.append(change)
            dates.append(date)

            # Check for the greatest increase in profits
            if change > greatest_increase["Amount"]:
                greatest_increase = {"Date": date, "Amount": change}

            # Check for the greatest decrease in profits
            if change < greatest_decrease["Amount"]:
                greatest_decrease = {"Date": date, "Amount": change}
        
        # Set the current profit/loss as previous for the next iteration
        previous_profit_loss = profit_loss

# Calculate the average change
average_change = sum(changes) / len(changes) if changes else 0

# Prepare the analysis summary
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

# Define the path to save the analysis in the "analysis" folder
output_path = os.path.join(base_dir, 'analysis', 'financial_analysis.txt')

# Export the analysis to a text file in the "analysis" folder
with open(output_path, 'w') as file:
    file.write(analysis)