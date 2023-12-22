# Don't change the Libraries
import os
import sys

#Your Code Here
def find_longest_orf(sequence):
    start_codon = "ATG"
    stop_codons = ["TAG", "TGA", "TAA"]
    longest_orf = ""
    current_orf = ""

    for i in range(len(sequence)):
        if sequence[i:i+3] == start_codon:
            current_orf = start_codon

            for j in range(i+3, len(sequence), 3):
                codon = sequence[j:j+3]
                current_orf += codon

                if codon in stop_codons:
                    if len(current_orf) > len(longest_orf):
                        longest_orf = current_orf
                    break 

    return longest_orf

def main():
    if len(sys.argv) < 2:
        print("Please provide the input file path as an argument.")
        return

    file_path = sys.argv[1]

    if not os.path.isfile(file_path):
        print("Invalid file path.")
        return

    with open(file_path, 'r') as file:
        sequences = {}
        current_sequence = ""

        for line in file:
            line = line.strip()

            if line.startswith(">"):
                if current_sequence:
                    sequences[current_sequence_name] = current_sequence
                    current_sequence = ""

                current_sequence_name = line[1:]
            else:
                current_sequence += line

        if current_sequence:
            sequences[current_sequence_name] = current_sequence

    for sequence_name, sequence in sequences.items():
        longest_orf = find_longest_orf(sequence)

        print(f"Longest ORF in sequence '{sequence_name}': {longest_orf}")

        if "--print_length" in sys.argv:
            print(f"Length: {len(longest_orf)}")

if __name__ == "__main__":
    main()