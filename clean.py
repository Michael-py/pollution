# import the necessary libraries
import pandas as pd
import numpy as np

def clean(file):
	# a dictionary of the stations and their ids
	stations = {'188.0': 'AURN Bristol Centre',
	 '203.0': 'Brislington Depot',
	 '206.0': 'Rupert Street',
	 '209.0': 'IKEA M32',
	 '213.0': 'Old Market',
	 '215.0': 'Parson Street School',
	 '228.0': 'Temple Meads Station',
	 '270.0': 'Wells Road',
	 '271.0': 'Trailer Portway P&R',
	 '375.0': 'Newfoundland Road Police Station',
	 '395.0': "Shiner's Garage",
	 '452.0': 'AURN St Pauls',
	 '447.0': 'Bath Road',
	 '459.0': 'Cheltenham Road \\ Station Road',
	 '463.0': 'Fishponds Road',
	 '481.0': 'CREATE Centre Roof',
	 '500.0': 'Temple Way',
	 '501.0': 'Colston Avenue'}

	# read in the cropped data csv file
	df = pd.read_csv(file, dtype={'DateEnd':'str', 'Current':'str'}) 

	# clean up necessary columns
	cols = df.select_dtypes(include='float64').columns # get columns that have data of type float64
	df.fillna(np.nan, inplace=True)
	df[cols] = df[cols].apply(pd.to_numeric, errors='coerce') # convert to type numeric. still float64

	# create a new column to serve as the comparison column
	# to remove rows that have a mismatch of siteID and location
	df['Lookup Loc'] = df['SiteID'].astype('str').map(stations)

	# find the mismatching rows
	mismatch = df[['SiteID', 'Location']][df['Location'] != df['Lookup Loc']]

	# print the number of mismatch found
	print(f"\n>>>> Number of mismatch found: {mismatch.shape[0]}\n")
	print(mismatch)

	# drop the comparison column
	df.drop('Lookup Loc', axis=1, inplace=True)

	# drop the rows that are mismatching
	print(f">>>> Number of observations before deletion: {df.shape}\n")
	df.drop(mismatch.index, axis=0, inplace=True)
	print(f">>>> Number of observations after deletion: {df.shape}\n")

	# convert SiteID to type int for get rid of floating point
	df = df.astype({'SiteID':'int'})

	df.to_csv("clean.csv", index=False)

if __name__ == "__main__":
	clean("crop.csv")