import csv

# newline='' -> yen bir kayıt oluşturulduğunda yeni bir satır oluşturulmasını engeller

# Dosyaya yazar, eğer dosya varsa üzerine yazar
with open("data.csv","w", newline='') as csvfile:
	writer = csv.writer(csvfile)
	writer.writerow(["Title","Description"])
	writer.writerow(["Row 1","Some desc"])

# Dosyaya yazar, kaydın kaldığı yerden devam eder
with open("data.csv","a", newline='') as csvfile:
	writer = csv.writer(csvfile)
	writer.writerow(["Row 2","Another desc"])

# Kaydın kaldığı yerden k,v formatında yazar
with open("data.csv","a", newline='') as csvfile:
	fieldnames = ["Title", "Description"]
	writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
	writer.writerow({"Title":"Row 3", "Description":"New desc"})

# Dosyadan okur
with open("data.csv", "r") as csvfile:
	reader = csv.reader(csvfile)
	for row in reader:
		print(row)

# k,v formatında okur
with open("data.csv","r") as csvfile:
	reader = csv.DictReader(csvfile)
	for row in reader:
		print(row)