import pandas as pd
import json
import pymongo
from flask import Flask, render_template, redirect
import requests


app = Flask(__name__)



conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)

client.drop_database('park_species')
client.drop_database('status')


api_token = "d7406257128f8a08b87f6924919480f7f68fbcbb51f8dd0822867f55a5a6fd86"

url="http://apiv3.iucnredlist.org/api/v3/country/getspecies/US?token="

iucn_api = url + api_token

api_response = requests.get(iucn_api).json()

iucn_results  = api_response["result"]
iucn_df = pd.DataFrame(iucn_results)

iucn_df = iucn_df.replace("LC", "Least Concern")
iucn_df = iucn_df.replace("DD", "Data Deficient")
iucn_df = iucn_df.replace("NT", "Near Threatened")
iucn_df = iucn_df.replace("VU", "Vunerable")
iucn_df = iucn_df.replace("EN", "Endangered")
iucn_df = iucn_df.replace("CR", "Critically Endangered")
iucn_df = iucn_df.replace("EW", "Extinct in the Wild")
iucn_df = iucn_df.replace("EX", "Extinct")

# iucn_df = iucn_df.reset_index('scientific_name')
#glacier_dataframe = glacier_dataframe.reset_index('scientific_name')

glacier_dataframe = pd.read_csv("cleaned_glacier_data_MOSHER.csv")

# glacier_df = glacier_dataframe.to_json(orient='records')


glacier_df = pd.read_csv("cleaned_glacier_data_MOSHER.csv")

glacier_df = glacier_df.rename(columns={"Park Name": "park_name", "Taxon Group": "taxon_group", "Scientific Name": "scientific_name", "Common Name": "common_name"})

glacier_with_status = glacier_df.merge(iucn_df, left_on='scientific_name', right_on='scientific_name', how='left')

db = client.park_species

collection = db.glacier

# glacier_dataframe = pd.read_csv("cleaned_glacier_data_MOSHER.csv")

# glacier_df = glacier_dataframe.to_json(orient='records')
glacier_with_status = glacier_with_status.to_json(orient='records')

#glacier_with_status = list(glacier_with_status)

g_df = json.loads(glacier_with_status)

# db.glacier.insert_many(g_df)

# collection = db.status


# db.status.insert_many(api_response)

collection = db.joined_frames

db.joined_frames.insert_many(g_df)

final_doc = db.joined_frames.find()



@app.route("/")
def index():

	# doc = db.glacier.find()
	# api_response = requests.get(iucn_api).json()
	doc = final_doc
	return render_template('index.html',list = doc)

# ~~~~~

@app.route("/least_concern")
def lc():
	lc = db.joined_frames.find({"category":"Least Concern"},{"_id":0, "common_name":1, "scientific_name":1, "category":1})
	return render_template("results.html", list=lc)



# ~~~~ BELOW: routes for buttons and data dumps ~~~

@app.route("/status")
def status():
	stat = final_doc
	return render_template('index.html',list = stat)

@app.route("/api_response")
def api_resp():
	doc = final_doc
	return render_template("api_response.html", list=doc)

@app.route("/plants")
def plants():
	# glacier_plants = db.joined_frames.find({"taxon_group":"Mammal"},{"_id":0, "commonname":1, "scientificname":1,})
	glacier_plants = db.joined_frames.find({"taxongroup":"Vascular Plant"},{"_id":0, "common_name":1, "scientific_name":1,"category":1})
	return render_template("results.html", list=glacier_plants)

 
@app.route("/mammals")
def mammals():
	# glacier = db.glacier.find({"taxongroup":"Mammal"},{"_id":0, "commonname":1, "scientificname":1,})
	glacier_mammals = db.joined_frames.find({"taxon_group":"Mammal"},{"_id":0, "common_name":1, "scientific_name":1,"category":1})
	return render_template("results.html", list=glacier_mammals)


@app.route("/birds")
def birds():
	glacier_birds = db.joined_frames.find({"taxongroup":"Bird"},{"_id":0, "common_name":1, "scientific_name":1,"category":1})
	return render_template("results.html", list=glacier_birds)

@app.route("/fish")
def fish():
	glacier_fish = db.joined_frames.find({"taxongroup":"Fish"},{"_id":0, "common_name":1, "scientific_name":1, "category":1})
	return render_template("results.html", list=glacier_fish)


@app.route("/amphibians")
def amphibians():
	glacier_amphibians = db.joined_frames.find({"taxongroup":"Amphibian"},{"_id":0, "common_name":1, "scientific_name":1,"category":1})
	return render_template("results.html", list=glacier_amphibians)

@app.route("/reptiles")
def reptiles():
	glacier_reptiles = db.joined_frames.find({"taxongroup":"Reptile"},{"_id":0, "common_name":1, "scientific_name":1,"category":1})
	return render_template("results.html", list=glacier_reptiles)

if __name__ == '__main__':
    app.run(debug=True)


