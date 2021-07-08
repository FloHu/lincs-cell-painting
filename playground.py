# %%
import gzip
my_path = "./consensus/2016_04_01_a549_48hr_batch1/2016_04_01_a549_48hr_batch1_consensus_median.csv.gz"


# %%

f = gzip.open(my_path, 'rb')


f.readline()
f.readline()
f.close()

# with gzip.open(my_path, 'rb') as f:
# 	file_content = f.read()


# %%
# let's start with level 4b: normalized and feature selected profiles with metadata
import pandas as pd
import gzip
from pprint import pprint

# my_path = "./profiles/cell_count/2016_04_01_a549_48hr_batch1/SQ00014812/SQ00014812_cell_count.csv"
# tab = pd.read_csv(my_path)

# contains plate and well information and lots of features
my_path = "./profiles/2016_04_01_a549_48hr_batch1/SQ00014812/SQ00014812.csv.gz"
tab = pd.read_csv(my_path)

# searching for the metadata
# contains assay plate barcode, batch number, batch data, plate map name
# (to link barcodes to plate maps?)
my_metapath = "./metadata/platemaps/2016_04_01_a549_48hr_batch1/barcode_platemap.csv"
metatab = pd.read_csv(my_metapath)

# this is the one corresponding to plate barcode SQ00014812
# and contains the concentration and broad compound information etc.
my_platemap_path = "./metadata/platemaps/2016_04_01_a549_48hr_batch1/platemap/C-7161-01-LM6-022.txt"
platemap_tab = pd.read_csv(my_platemap_path, delimiter = "\t")

# this maps back from compounds to plates (?)
broad_sample_info = pd.read_csv("./metadata/platemaps/broad_sample_info.tsv", delimiter="\t")

# 'clue manifest' subdirectory:
# this may be quite useful: seems to list all profile files + what is in them
manifest = pd.read_csv("./metadata/clue_manifest/cell_painting_lincs_pilot_1_manifest.txt", delimiter="\t")
manifest

