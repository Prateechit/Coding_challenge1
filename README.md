**Plasmid Design Tool**

Overview:

This repository contains a Python-based tool to design plasmid DNA sequences based on user-defined specifications. The tool modifies an input DNA sequence by removing specified restriction enzyme sites and ensuring required genetic markers, producing a final plasmid sequence compatible with bacterial replication.
This project was developed as part of a coding challenge focused on bioinformatics sequence manipulation, robustness, and reproducibility.
------------------------------------------------------------------------------------------------------------------------------------------------
Features:

Reads plasmid DNA sequence from a FASTA file

Parses a design specification file to determine:

Restriction enzyme sites to remove

Genetic markers to ensure

Uses a marker dictionary file for enzyme recognition sites and markers

Safely handles missing or undefined markers

Outputs a valid FASTA file of the final plasmid sequence

Includes an automated test script to verify correctness

Input Files
1. Input.fa

FASTA file containing the input plasmid DNA sequence.
For testing, the pUC19 plasmid sequence is used.

2. Design.txt

Design specification file defining the desired plasmid configuration.

Example:

Multiple_Cloning_Site1, EcoRI
Antibiotic_marker1, AmpR
# End of File

3. markers.tab

Dictionary mapping marker names to recognition sequences or roles.

Example:

EcoRI_site, GAATTC
BamHI_site, GGATCC
AmpR_gene, AMPICILLIN_RESISTANCE_GENE

Output
Output.fa

A FASTA file containing the final plasmid DNA sequence after:

Removal of specified restriction sites (e.g., EcoRI)

Retention or addition of required markers

Note: Output.fa is a generated file and is intentionally excluded from version control.
It can be reproduced by running the script.

How to Run
Run the plasmid builder
python plasmid_builder.py

Run automated tests
chmod +x test.sh
./test.sh


The test script verifies:

Output file generation

Successful removal of the EcoRI restriction site

File Structure
.
├── plasmid_builder.py   # Main plasmid design script
├── Design.txt           # Design specification
├── Input.fa             # Input DNA sequence
├── markers.tab          # Marker dictionary
├── test.sh              # Automated test script
├── .gitignore           # Ignored generated files
└── README.md            # Project documentation

Assumptions & Design Choices

The input plasmid (pUC19) already contains a functional origin of replication.

Marker and restriction site definitions are provided via markers.tab.

Missing markers or enzymes are safely ignored without crashing.

Generated output files are not committed to GitHub.

Testing

The repository includes a shell-based test (test.sh) that automatically validates:

Correct execution of the tool

Removal of the EcoRI recognition sequence (GAATTC)

Author

Prateechi Tulsyan
