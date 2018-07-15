import csv

with open("data.csv","w+", newline='') as csvfile:	# w+ : Read and write. Overwrite existing file or creates a new file.
	writer = csv.writer(csvfile)
	writer.writerow(["Title","Description"])
	writer.writerow(["Row 1","Some desc"])