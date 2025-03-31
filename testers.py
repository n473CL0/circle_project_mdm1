import numpy as np
import pandas as pd
import glob
import matplotlib.pyplot as plt
import seaborn as sns

from models import Sheet, System


def test_specific_arrangement(arrangement, d_1, d_2, sheet_width, precision, write_to_terminal=False):
    '''
    Tests an arrangement function by increasing the size of the sheet by a factor of 10
    until the waste percentage converges to %precision decimal places.
    '''

    last_sample = 0
    sample = 1

    size = 10 ** 3

    if write_to_terminal:
        (f"Test started for d1 = {d_1}, d2 = {d_2}")

    while round(last_sample, precision) != round(sample, precision):
        last_sample = sample

        sheet = Sheet(size, sheet_width)
        disks = arrangement(d_1, d_2, sheet)

        system = System(sheet, disks)

        sample = system.waste()
        if write_to_terminal:
            print(f"Length: {size}, Waste: {round(sample, precision)}")

        size *= 10

    n_1, n_2 = system.count(d_1, d_2)

    if write_to_terminal:
        print(f"Test complete: waste = {round(sample, precision)}, ratio = {round(n_1 / n_2, 2)}")

    return system

def test_general_arrangement(arrangement, resolution, precision=2, sheet_width=100, save_figures=False):
    '''
    Tests an arrangement function for a range of pairs of diameters
    '''
    columns = np.arange(resolution, (sheet_width-sheet_width%resolution)+resolution, resolution)
    rows = np.arange(resolution, (sheet_width-sheet_width%resolution)+resolution, resolution)
    data = np.zeros((100 // resolution, 100 // resolution))

    for i in range(100 // resolution):
        
        d_1 = (i+1) * resolution
        
        for j in range(100 // resolution):
            
            d_2 = (j+1) * resolution

            if d_1 >= d_2:
                test = test_specific_arrangement(arrangement, d_1, d_2, sheet_width, precision)
                fraction_waste = round(test.waste(), precision)
                data[i, j] = fraction_waste
                data[j, i] = fraction_waste

                if save_figures:
                    test.save_fig_section(f"figures/{arrangement('name', None, None)}/{d_1}_{d_2}.png", 300)

        print(f"Row {i+1} complete")

    df = pd.DataFrame(data, columns=columns, index=rows)

    return df

def test_overall(file_pattern, file_to):

    # Path to data files (adjust the pattern as needed)
    file_list = glob.glob(file_pattern)

    # List to store dataframes
    dfs = []

    # Read all files into dataframes
    for file in file_list:
        df = pd.read_csv(file, index_col=0)  # Assuming first column and first row contain indices
        dfs.append(df)

    # Ensure all DataFrames have the same structure
    base_df = dfs[0]
    for df in dfs:
        df = df.reindex(index=base_df.index, columns=base_df.columns)

    # Compute the element-wise minimum across all DataFrames
    min_df = pd.concat(dfs).groupby(level=0).min()

    # Save the resulting DataFrame
    min_df.to_csv(file_to)

    print("Processed", len(file_list), f"files. Minimum values saved to {file_to}")

def plot_data(read_from, save_to):
    # Load the minimum waste values file
    min_df = pd.read_csv(read_from, index_col=0)

    # Set up the figure size
    plt.figure(figsize=(10, 8))

    # Create the heatmap
    sns.heatmap(min_df, annot=False, fmt=".2f", cmap="coolwarm")

    # Add titles and labels
    plt.title("Minimum Waste Percentage Heatmap")
    plt.xlabel("d1 /cm")
    plt.ylabel("d2 /cm")

    # Save the plot
    plt.savefig(save_to)