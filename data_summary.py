"""
Author: Lexi Virta
Date: 2025-11-24
Description: Summarizes data from ch_9_lab_data.txt into a summary.txt file
"""

from pathlib import Path

# Configurable file paths
INPUT_FILE = Path.resolve(Path("./data/ch_9_lab_data.txt"))
OUTPUT_FILE = Path.resolve(Path("./data/output.txt"))


def main():
    input_handle = None
    try:
        input_handle = open(INPUT_FILE, "r")
    except FileNotFoundError:
        print("Error: Data file " + str(INPUT_FILE) + " not found")
        return

    dataset_sum = 0
    dataset_size = 0

    # Read input dataset
    while True:
        # Read each line as its own number
        line = input_handle.readline()
        if not line: break

        try:
            parsed_number = int(line)

            dataset_sum += parsed_number
            dataset_size += 1
        except ValueError:
            print("Exception: encountered non-integer in dataset: " + line)
            return
        
    input_handle.close() # Stop using the raw data in the input file

    # Prevents a divide-by-zero error if no elements are present in the dataset file
    if(dataset_size == 0):
        print("No elements found in " + str(INPUT_FILE))
        return

    # Write output table
    with open(OUTPUT_FILE, "w") as output_handle:
        output_handle.writelines([
            "======= Dataset Summary =======\n"
            f"{'Size:':<8}{dataset_size:>20,}\n"
            f"{'Sum:':<8}{dataset_sum:>20,}\n"
            f"{'Avg:':<8}{dataset_sum / dataset_size:>23,.2f}\n"
        ])
    
    print("Output written to " + str(OUTPUT_FILE))


main()