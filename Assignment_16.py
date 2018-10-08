import pymongo
client = pymongo.MongoClient()
db = client['Students']
collection = db['students']
lst = []
for i in range(1,11):
        data = {}
        print('Student',i)
        data['Name'] = input("\tEnter Student's Name: ")
        while(1):
            data['Marks'] = int(input("\tEnter Student's marks (0-100): "))

            if data['Marks'] >= 0 and data['Marks'] <= 100:
                break
            else:
                print("ERROR!! INVALID INPUT")                
        lst.append(data)   
collection.insert_many(lst)
data1 = collection.find({'Marks': {'$gt': 80}})
print('Students with Marks greater than 80:-')
for d1 in data1:
    print('\t',d1['Name'])
