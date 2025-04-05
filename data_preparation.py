import pandas as pd
import glob
import os

def consolidate_nifty_data():
    # Get all NIFTY 50 CSV files
    nifty_files = glob.glob('NIFTY 50-*.csv')
    
    # Create an empty list to store DataFrames
    dfs = []
    
    # Read each CSV file and append to the list
    for file in nifty_files:
        df = pd.read_csv(file)
        dfs.append(df)
    
    # Concatenate all DataFrames
    consolidated_df = pd.concat(dfs, ignore_index=True)
    
    # Convert 'Date' column to datetime if it exists
    if 'Date' in consolidated_df.columns:
        consolidated_df['Date'] = pd.to_datetime(consolidated_df['Date'])
        # Sort by date
        consolidated_df = consolidated_df.sort_values('Date')
    
    # Save to new CSV file
    consolidated_df.to_csv('nifty_data.csv', index=False)
    print(f"Data consolidated and saved to nifty_data.csv")
    print(f"Total number of records: {len(consolidated_df)}")

if __name__ == "__main__":
    consolidate_nifty_data()
