import sys

import arrangers
import testers as test
    

def named_model(name):
    '''
    Returns the arrangement function corresponding to the name
    '''
    if name == 'square_simple':
        return arrangers.square_simple
    if name == 'square_vertical':
        return arrangers.square_vertical
    if name == 'hexagonal':
        return arrangers.hexagonal
    if name == 'hexagonal_rotated':
        return arrangers.hexagonal_rotated
    if name == 'square_spiral':
        return arrangers.square_spiral
    else:
        sys.exit(f"Model {name} not found.")


def test_arrangment(arrangement_name, resolution, save_figures=False):

    df = test.test_general_arrangement(
        named_model(arrangement_name), 
        resolution, 
        save_figures=save_figures
    )

    df.to_csv(f"data/{arrangement_name}_{resolution}.csv")

import pandas as pd

import pandas as pd

def mirror_csv(input_csv, output_csv):
    # Read the CSV file, ensuring no automatic indexing
    df = pd.read_csv(input_csv, header=None, index_col=None)

    # Extract headers (first row = d1 values, first column = d2 values)
    d1_values = df.iloc[0, 1:].values  # First row (excluding top-left cell)
    d2_values = df.iloc[1:, 0].values  # First column (excluding top-left cell)

    # Extract the numeric data part of the table
    data = df.iloc[1:, 1:].copy()

    # Convert to numeric in case there are accidental string values
    data = data.apply(pd.to_numeric, errors='coerce')

    # Mirror the values where d2 > d1
    for i in range(len(d2_values)):
        for j in range(len(d1_values)):
            if d2_values[i] > d1_values[j]:  # Upper triangle swap
                data.iat[i, j] = data.iat[j, i]  # Swap values

    # Write the modified data back into the dataframe
    df.iloc[1:, 1:] = data

    # Save to new CSV without changing the original format
    df.to_csv(output_csv, index=False, header=False)
    print(f"Mirrored data saved to {output_csv}")

import pandas as pd
import numpy as np

def merge_data_with_grid(full_grid_csv, data_csv, output_csv):
    # Load the full 100x100 grid of 1s
    full_df = pd.read_csv(full_grid_csv, header=None, index_col=None)
    
    # Load the CSV with missing data
    data_df = pd.read_csv(data_csv, header=None, index_col=None)

    # Extract headers from the data CSV
    d1_values = data_df.iloc[0, 1:].values  # First row (excluding top-left cell)
    d2_values = data_df.iloc[1:, 0].values  # First column (excluding top-left cell)

    # Extract actual data
    data = data_df.iloc[1:, 1:].copy()

    # Replace values in the full grid where data is available
    for i, d2 in enumerate(d2_values):
        for j, d1 in enumerate(d1_values):
            value = data.iat[i, j]  # Get the available data point
            if not pd.isna(value):  # Only replace if the value exists
                full_df.at[d2, d1] = value  # Set value at (d2, d1)
                full_df.at[d1, d2] = value  # Ensure symmetry at (d1, d2)

    # Reinsert headers
    full_df.insert(0, "d2 \\ d1", full_df.index)  # First column as d2
    full_df.loc[0] = ["d2 \\ d1"] + list(full_df.columns[1:])  # First row as d1
    full_df.sort_index(inplace=True)  # Ensure headers stay at the top

    # Save to CSV
    full_df.to_csv(output_csv, index=False, header=False)
    print(f"Merged data saved to {output_csv}")


if __name__ == '__main__':

    
    methods = [
            'square_simple',
            'square_vertical',
            'hexagonal',
            'hexagonal_rotated'
        ]
    '''
    for m in methods:
        test_arrangment(m, 1)
    '''
    

    test.plot_data(f'data/hexagon_seperate.csv', f'data/heatmaps/hexagon_seperate.png')