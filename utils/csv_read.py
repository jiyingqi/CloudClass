import csv


out = {}

with open('../../train.csv') as traincsv:
    reader = csv.DictReader(traincsv)
    for row in reader:
            if "Fish" in row['Image_Label']:
                if row['EncodedPixels']:
                    out[row['Image_Label']] = 1
                else:
                    out[row['Image_Label']] = 0

traincsv.close()
                        
                    
with open('../csvs/fish.csv', 'w') as fishcsv:
    fieldnames = ["image_name", "fish"]
    writer = csv.DictWriter(fishcsv,fieldnames=fieldnames)

    writer.writeheader()
    for row in out:
        tmp = row.split("_")
        writer.writerow({'image_name' : tmp[0], 'fish' : out[row]})