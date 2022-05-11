#!/bin/bash
rm CalibrationFiles/Depth/*
rm CalibrationFiles/Color/*
echo "Timestamp 0 0 0" > CalibrationFiles/OdemData.txt
for i in {0..9}
do
	sudo python3 PythonFile.py
	python3 Intermediate.py
	rs-save-to-disk
	mv rs-save-to-disk-output-Depth.png rs-save-to-disk-output-Depth-${i}.png
	mv rs-save-to-disk-output-Color.png rs-save-to-disk-output-Color-${i}.png
done
rm *.csv
mv rs-save-to-disk-output-Depth-* CalibrationFiles/Depth/
mv rs-save-to-disk-output-Color-* CalibrationFiles/Color/

