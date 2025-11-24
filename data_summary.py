"""
Author: Lexi Virta
Date: 2025-11-24
Description: Summarizes data from ch_9_lab_data.txt into a summary.txt file
"""

from pathlib import Path

INPUT_FILE = Path.resolve(Path("./ch_9_lab_data.txt"))
OUTPUT_FILE = Path.resolve(Path("./output.txt"))

def main():
    input_handle = open(INPUT_FILE, "r")

    dataset_sum = 0
    dataset_size = 0

    while True:
        line = input_handle.readline()
        if not line: break

        try:
            parsed_number = int(line)

            dataset_sum += parsed_number
            dataset_size += 1
        except ValueError:
            print("Exception: encountered non-integer in dataset: " + line)
            return
        
    input_handle.close()

    if(dataset_size == 0):
        print("No elements found in " + str(INPUT_FILE))
        return

    with open(OUTPUT_FILE, "w") as output_handle:
        output_handle.writelines([
            "======= Dataset Summary =======\n"
            f"{'Size:':<8}{dataset_size:>20,}\n"
            f"{'Sum:':<8}{dataset_sum:>20,}\n"
            f"{'Avg:':<8}{dataset_sum / dataset_size:>23,.2f}\n"
        ])


main()