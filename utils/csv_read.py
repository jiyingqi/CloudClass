import csv

# Dict for storage
out = {}

# Parse the train.csv file for target values
with open('../../train.csv') as traincsv:
    reader = csv.DictReader(traincsv)
    for row in reader:
        filename = row['Image_Label'].split("_")[0]
        if filename not in out:
                out[filename] = {}
        if "Fish" in row['Image_Label']:
            if row['EncodedPixels']:
                out[filename]['fish'] = 1
            else:
                out[filename]['fish'] = 0

        if "Flower" in row['Image_Label']:
            if row['EncodedPixels']:
                out[filename]['flower'] = 1
            else:
                out[filename]['flower'] = 0

        if "Gravel" in row['Image_Label']:
            if row['EncodedPixels']:
                out[filename]['gravel'] = 1
            else:
                out[filename]['gravel'] = 0

        if "Sugar" in row['Image_Label']:
            if row['EncodedPixels']:
                out[filename]['sugar'] = 1
            else:
                out[filename]['sugar'] = 0

traincsv.close()
                        
                    
# Write to individual files for individual testing
with open('../csvs/fish.csv', 'w') as fishcsv:
    fieldnames = ["image_name", "fish"]
    writer = csv.DictWriter(fishcsv,fieldnames=fieldnames)

    writer.writeheader()
    for row in out:
        tmp = row.split("_")
        writer.writerow({'image_name' : tmp[0], 'fish' : out[tmp[0]]['fish']})
        
with open('../csvs/flower.csv', 'w') as fishcsv:
    fieldnames = ["image_name", "flower"]
    writer = csv.DictWriter(fishcsv,fieldnames=fieldnames)

    writer.writeheader()
    for row in out:
        tmp = row.split("_")
        writer.writerow({'image_name' : tmp[0], 'flower' : out[tmp[0]]['flower']})

with open('../csvs/gravel.csv', 'w') as fishcsv:
    fieldnames = ["image_name", "gravel"]
    writer = csv.DictWriter(fishcsv,fieldnames=fieldnames)

    writer.writeheader()
    for row in out:
        tmp = row.split("_")
        writer.writerow({'image_name' : tmp[0], 'gravel' : out[tmp[0]]['gravel']})

with open('../csvs/sugar.csv', 'w') as fishcsv:
    fieldnames = ["image_name", "sugar"]
    writer = csv.DictWriter(fishcsv,fieldnames=fieldnames)

    writer.writeheader()
    for row in out:
        tmp = row.split("_")
        writer.writerow({'image_name' : tmp[0], 'sugar' : out[tmp[0]]['sugar']})


# For multiclassification training
with open('../csvs/targets.csv', 'w') as fishcsv:
    fieldnames = ["image_name", "fish", "flower", "gravel", "sugar"]
    writer = csv.DictWriter(fishcsv,fieldnames=fieldnames)

    writer.writeheader()
    for row in out:
        tmp = row.split("_")
        writer.writerow({'image_name' : tmp[0],'fish' : out[tmp[0]]['fish'], 'flower' : out[tmp[0]]['flower'], 'gravel' : out[tmp[0]]['gravel'] , 'sugar' : out[tmp[0]]['sugar']})

