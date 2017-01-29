import sys
import os
import pandas as pd
import numpy as np

<<<<<<< HEAD:Scripts/AggregateData.py
def aggregate(path,outputfile,encoding="utf-8"):
	print("Aggregating events data from folder : "+path)
	df = None
	file_list = sorted(os.listdir(path))
	for csv_file in file_list:
		if (df is None):
			df = pd.read_csv(path + '/' + csv_file,encoding=encoding)
		else:
			tmp = pd.read_csv(path + '/' + csv_file,encoding=encoding)
			df = df.append(tmp, ignore_index=True)

	df.to_csv(outputfile,encoding=encoding)
	print("Aggregation saved to : "+outputfile)

=======
# small function to merge all the small csv
>>>>>>> 9dd6b06c7081cbedc1d8d7e13458d6c60e04ce97:Scripts/events.ch/AggregateData.py
if __name__ == "__main__":
    if(len(sys.argv) < 3):
        sys.exit("ERROR : not enough arguments. Require folder and output file")
    path = sys.argv[1]
    outputfile = sys.argv[2]
    aggregate(path,outputfile,encoding = "utf-8")