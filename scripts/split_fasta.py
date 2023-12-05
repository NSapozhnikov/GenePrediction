import os
from Bio import SeqIO

def split_fasta(input_file, output_prefix, max_size):
    records = list(SeqIO.parse(input_file, "fasta"))
    
    current_size = 0
    current_records = []
    output_files = []

    for record in records:
        current_records.append(record)
        current_size += len(record.seq)

        if current_size >= max_size:
            output_file = f"{output_prefix}_{len(output_files) + 1}.fasta"
            SeqIO.write(current_records, output_file, "fasta")
            output_files.append(output_file)

            current_records = []
            current_size = 0

    # Write the remaining records to a file
    if current_records:
        output_file = f"{output_prefix}_{len(output_files) + 1}.fasta"
        SeqIO.write(current_records, output_file, "fasta")
        output_files.append(output_file)

    return output_files

input_file = "data/blastp_augustus.whole_filtered_proteins.aa"
output_prefix = "data/blastp_augustus.whole_filtered_proteins"
max_size = 190000  # 190 KB

split_files = split_fasta(input_file, output_prefix, max_size)
print(f"FASTA file split into {len(split_files)} pieces.")