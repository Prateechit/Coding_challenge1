#!/usr/bin/env python3

def read_fasta(filename):
    with open(filename, "r") as f:
        lines = f.readlines()
    header = lines[0].strip()
    sequence = "".join(line.strip() for line in lines[1:])
    return header, sequence


def read_design(filename):
    enzymes = []
    markers = []

    with open(filename, "r") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue

            parts = [p.strip() for p in line.split(",")]

            # If second column exists, treat it as enzyme/marker name
            if len(parts) >= 2:
                name = parts[1]
            else:
                name = parts[0]

            # crude but safe classification
            if name.endswith("I") or name.endswith("II"):
                enzymes.append(name)
            else:
                markers.append(name)

    return enzymes, markers



def read_markers(filename):
    marker_dict = {}
    with open(filename, "r") as f:
        for line in f:
            line = line.strip()

            # skip empty lines or comments
            if not line or line.startswith("#"):
                continue

            # skip malformed lines
            if "," not in line:
                continue

            name, seq = line.split(",", 1)
            marker_dict[name.strip()] = seq.strip()

    return marker_dict



def remove_restriction_sites(sequence, enzymes, marker_dict):
    for enzyme in enzymes:
        site_key = enzyme + "_site"
        if site_key in marker_dict:
            sequence = sequence.replace(marker_dict[site_key], "")
    return sequence


def add_required_markers(sequence, markers, marker_dict):
    for marker in markers:
        gene_key = marker + "_gene"
        if gene_key in marker_dict:
            gene_seq = marker_dict[gene_key]
            if gene_seq not in sequence:
                sequence += gene_seq
    return sequence


def write_fasta(header, sequence, filename):
    with open(filename, "w") as f:
        f.write(header + "\n")
        for i in range(0, len(sequence), 60):
            f.write(sequence[i:i+60] + "\n")


def main():
    fasta_file = "Input.fa"
    design_file = "Design.txt"
    marker_file = "markers.tab"
    output_file = "Output.fa"

    header, sequence = read_fasta(fasta_file)
    enzymes, required_markers = read_design(design_file)
    marker_dict = read_markers(marker_file)

    sequence = remove_restriction_sites(sequence, enzymes, marker_dict)
    sequence = add_required_markers(sequence, required_markers, marker_dict)

    write_fasta(header, sequence, output_file)

    print("Plasmid design completed.")
    print("Output written to Output.fa")


if __name__ == "__main__":
    main()
