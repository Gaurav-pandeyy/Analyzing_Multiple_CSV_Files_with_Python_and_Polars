import glob
import polars as pl

# Get all CSV files from the 'invoices' directory
csv_files = glob.glob("./invoices/*.csv")

# Iterate over the CSV files and process each one
for file in csv_files:
    # Load the CSV file into a Polars dataframe
    df = pl.read_csv(file)

    # Calculate total price and number of invoices
    total_price = df["Total Price"].sum()
    total_invoices = df.height

    # Extract the filename without the path
    filename = file.split("/")[-1]

    # Print the output in the desired format
    print(f"File: {file}")
    print(f"Number of invoices: {total_invoices}")
    print(f"Total sum of prices: ${total_price:.2f}")
    print("----------------------------------------")  # Separator line with dashes
