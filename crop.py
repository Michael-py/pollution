# import the necessary library
import pandas as pd

def crop_data(file, delimiter, date_limit):

	# read in the csv file
	df = pd.read_csv(file, delimiter=delimiter, dtype={'DateEnd':'str', 'Current':'str'})

	#get the shape of the dataframe before cropping and print
	shape1 = df.shape
	print(f"\n>>>> Shape of the dataframe before cropping is: {shape1}")

	# convert the `Date Time`, DateStart and DateEnd columns
	# to datetime format
	df[["Date Time", "DateStart", "DateEnd"]] = df[["Date Time", "DateStart", "DateEnd"]].apply(pd.to_datetime)

	# delete every record that exist before 00:00 01 Jan 2010
	df.drop(df[df["Date Time"] < date_limit].index, inplace=True)

	# print out the number of items deleted and the current 
	# shape of the datarame
	print(f"\n>>>> Total number of items deleted: {shape1[0] - df.shape[0]}")
	print(f"\n>>>> Shape of dataframe after cropping: {df.shape}\n")

	df.to_csv("crop.csv", index=False)


crop_data("bristol-air-quality-data.csv", ";", "2010-01-01")