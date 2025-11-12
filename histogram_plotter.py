import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

def histogram_with_bin_size(csv_file: str, column_name: str, bin_size: float, output_file: str = None):
    df = pd.read_csv(csv_file)

    if column_name not in df.columns:
        raise ValueError(f"Column '{column_name}' not found")

    data = df[column_name].dropna()

    if not pd.api.types.is_numeric_dtype(data):
        raise ValueError(f"Column '{column_name}'not numeric")

    data_min, data_max = data.min(), data.max()
    bins = np.arange(data_min, data_max + bin_size, bin_size)

    counts, edges, patches = plt.hist(data, bins=bins, color='skyblue', edgecolor='black')

    max_count_index = np.argmax(counts)
    max_bin_center = (edges[max_count_index] + edges[max_count_index + 1]) / 2
    max_count = counts[max_count_index]

    plt.text(
        max_bin_center,
        max_count + (0.02 * max(counts)),
        f"Peak: {int(max_count)} values\n at {max_bin_center:.2f} +/- {bin_size:.2f}",
        ha='center',
        va='bottom',
        fontsize=9,
        color='black',
        fontweight='bold'
    )

    if not output_file:
        base = os.path.splitext(os.path.basename(csv_file))[0]
        output_file = f"{base}_histogram_{column_name}.png"

    plt.title(f"Histogram of charge data")
    plt.xlabel("Charge (Coloumbs)")
    plt.ylabel("Frequency")
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.savefig(output_file, bbox_inches='tight')
    print("done")
    plt.show()

histogram_with_bin_size("test.csv", "56-83.6", 20, None)
