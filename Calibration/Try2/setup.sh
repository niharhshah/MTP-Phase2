#!/bin/bash
rm CalibrationFiles/Depth/*
rm CalibrationFiles/Color/*
echo "0 0 1 0" > CalibrationFiles/OdemData.txt
for i in {0..2}
do
	rs-save-to-disk
	python3 PythonFile.py
	mv rs-save-to-disk-output-Depth.png Depth-${i}.png
	mv rs-save-to-disk-output-Color.png Color-${i}.png
done
rm *.csv
mv Depth-* CalibrationFiles/Depth/
mv Color-* CalibrationFiles/Color/

