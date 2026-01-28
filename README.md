**Plasmid Design Tool**

Overview:

This repository contains a Python-based tool to design plasmid DNA sequences based on user-defined specifications. The tool modifies an input DNA sequence by removing specified restriction enzyme sites and ensuring required genetic markers, producing a final plasmid sequence compatible with bacterial replication.
This project was developed as part of a coding challenge focused on bioinformatics sequence manipulation, robustness, and reproducibility.
------------------------------------------------------------------------------------------------------------------------------------------------
Features:

1. Reads plasmid DNA sequence from a FASTA file

2. Parses a design specification file to determine:

> Restriction enzyme sites to remove

> Genetic markers to ensure

> Uses a marker dictionary file for enzyme recognition sites and markers

3. Safely handles missing or undefined markers

4. Outputs a valid FASTA file of the final plasmid sequence

5. Includes an automated test script to verify correctness
------------------------------------------------------------------------------------------------------------------------------------------
Input Files
1. Input.fa

FASTA file containing the input plasmid DNA sequence.
For testing, the pUC19 plasmid sequence is used.

2. Design.txt

Design specification file defining the desired plasmid configuration.

3. markers.tab

Dictionary mapping marker names to recognition sequences or roles.

Output
Output.fa

> A FASTA file containing the final plasmid DNA sequence after:

> Removal of specified restriction sites (e.g., EcoRI)

> Retention or addition of required markers
---------------------------------------------------------------------------------------------------------------------------------

How to Run:

1. Run the plasmid builder: python plasmid_builder.py

2. Run automated tests
chmod +x test.sh
./test.sh


The test script verifies:

Output file generation

Successful removal of the EcoRI restriction site
-------------------------------------------------------------------------------------------------------------------------------------------
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
