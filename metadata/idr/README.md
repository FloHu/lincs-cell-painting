# IDR submission

This folder contains input files and an .Rmd notebook for generating the library metadata file for submitting the imaging data to IDR. 

The resulting file are stored along with a manually-created study file in a shared google folder linked below:

The input files are as follows:

- In this folder:
  - lincs_plates_final.txt - list of full plate names
  - idr0000-screenA-library.txt - template library file taken from https://github.com/IDR/idr0000-lastname-example/archive/master.zip
- At other locations in this repository: 
  - 2016_04_01_a549_48hr_batch1_metadata_cell_count_summary.tsv - raw screen metadata
  - repurposing_drugs_20200324.txt - repurposing drug annotations
  - repurposing_samples_20200324.txt - repurposing sample annotations

The .Rmd notebook generates an updated version of the file `idr0000-screenA-library.txt.`
