#!/bin/bash

echo "Running plasmid builder..."
python plasmid_builder.py

echo "Checking if Output.fa exists..."
if [ ! -f Output.fa ]; then
    echo "TEST FAILED: Output.fa not created"
    exit 1
fi

echo "Checking EcoRI site removal..."
if grep -q GAATTC Output.fa; then
    echo "TEST FAILED: EcoRI site still present"
    exit 1
else
    echo "EcoRI site successfully removed"
fi

echo "ALL TESTS PASSED"
