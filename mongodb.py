from pymongo import MongoClient
# mongodb+srv://root:Mb%409371288080@cluster007.cyzcj.mongodb.net/?retryWrites=true&w=majority
client = MongoClient("mongodb+srv://root:Mb%409371288080@cluster007.cyzcj.mongodb.net/?retryWrites=true&w=majority")

database = client['Mindbowser']

collection = database['scraper_pipeline']

# record = {
#     'uid': 59,
#     'scraper_name': "nik",
#     'scraper_date': '2023-05-06T00:00:00.000+00:00',
#     'start_time': "12:10:06",
#     'job_message': "Success",
#     'records_fetched': 13,
#     'job_status': True,
#     'end_time': "12:10:07",
#     'execution_time': "1 second"
# }

# rec = database['scraper_pipeline'].insert_one(record)

# collection.update_one({'scraper_name': 'nik'}, {'$set': {'scraper_name': 'nikhil'}})

# collection.delete_one({'scraper_name': 'nikhil'})

for i in collection.find({'scraper_name': 'nikhil'}):
    print(i)
    print('Present')
else:
    print('Absent')

