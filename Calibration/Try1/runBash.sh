#!/bin/bash
for i in {1..14}
do
    python3 PythonFile.py
    ./Save2Disk
done
mv output-Color-* CalibrationFiles/RGB/
mv output-Depth-* CalibrationFiles/Depth/