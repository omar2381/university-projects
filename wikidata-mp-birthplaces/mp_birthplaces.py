#to run the code, enter "python mp_birthplaces.py"

# IMPORTS
import sys
from SPARQLWrapper import SPARQLWrapper, JSON
import pandas as pd
from geopy.geocoders import Nominatim
import time

start = time.time()

# Global Variables
#LoPs is an acronym for "List of Parliments" printing len(LoPs) returns 57 which is the number of parliments from 1-58 
#this list was manually made from the data in wikidata
LoPs = ["Q41582416","Q41582499","Q41582532","Q41582534","Q41582535","Q41582538","Q41582540","Q41582542","Q41582544",
"Q41582545","Q41582546","Q41582548","Q41582550","Q41582553","Q41582555","Q41582556","Q41582557","Q41582558","Q41582559",
"Q41582560","Q41582563","Q41582565","Q41582568","Q41582570","Q41582572","Q41582573","Q41582575","Q41582577","Q41582579",
"Q41582581","Q41582582","Q41582584","Q41582585","Q41582587","Q41582588","Q41582591","Q41582593","Q41582597","Q41582600",
"Q41582603","Q41582604","Q41582606","Q41582608","Q41582609","Q41582612","Q41582615","Q41582617","Q41582619","Q41582621",
"Q41582624","Q41582627","Q36634044","Q35921591","Q35647955","Q35494253","Q30524718","Q30524710","Q77685926"]

#The Url for accessing wikidata
endpoint_url = "https://query.wikidata.org/sparql"

#the query was split into 3 sections querya, queryb and queryc to allow for the automation of data collection
#of each parliment in the loop below
querya = """SELECT ?item ?itemLabel ?born ?bornLabel ?coord WHERE{{ ?item wdt:P39 wd:"""
queryc = """{ ?item wdt:P19 ?born . } { ?born wdt:P625 ?coord . }  SERVICE wikibase:label { bd:serviceParam wikibase:language "en" }}ORDER BY ?itemLabel"""

# Functions

#this function was created automatically on wikidata
def get_results(endpoint_url, query):
    user_agent = "WDQS-example Python/%s.%s" % (sys.version_info[0], sys.version_info[1])
    sparql = SPARQLWrapper(endpoint_url, agent=user_agent)
    sparql.setQuery(query)
    sparql.setReturnFormat(JSON)
    return sparql.query().convert()

#my function to collect the data automatically
def get_data():

    f = open("MPs.txt","w")  #opening text file
    results = {}             #empty dictionary
    coords_seen = {}      #set of coordinates seen to increase the speed of program
    lines_seen = set()       #set of MP's seen to prevent repeating values
    no_of_MPs = 0            #variable to count the number of MPs

    for i in range(0,len(LoPs)): #loop from the first parliment to the last

        #f = open("parliment"+str(i+1)+".csv","w")
        #f.write("------------ PARLIMENT NUMBER " + str(i+1) + " START ------------\n\n")

        queryb = LoPs[i] + ".}"  #the final part of query to be combined 
        query = querya + queryb + queryc
        
        results = get_results(endpoint_url,query) #sending the query to the previous function which returns the wikidata list

        for result in results["results"]["bindings"]: #loop to filter and clean the wikidata data

            name = result["itemLabel"]["value"]   #name of the MP

            coordinates = result["coord"]["value"][6:-1].replace(' ', ',') #coordinates (lat,long)
            coord = coordinates.split(",") #spliting lat and long to reform
            coordinates = coord[1] + "," + coord[0] # making the set (long,lat)

            bornlabel = result["bornLabel"]["value"]

            born = result["born"]["value"][31:]    #code of where the MP was born

            #before this if-else statement was included, the program took 2.3 hrs to run, after it takes 27 miuntes
            #i thought of the if statement myself as the code was taking too long to run
            if coordinates in coords_seen: #if the coordinates have been seen before, then get the correspoding values
                state = coords_seen[coordinates][0]
                country = coords_seen[coordinates][1]
            else: #if these are new coordinates, then find out the corresponding location and add it to the list
                locator = Nominatim(user_agent="myGeocoder") #using reverse geocoding to find the location from the coordinates
                location = locator.reverse(coordinates)
                location = location.raw
                country = location["address"]["country"]
                if country == "United Kingdom": #make sure only MP's born in the UK are considered
                    state = location["address"]["state"]
                    coords_seen.update({coordinates:(state, country)})

            #if statement to make sure that values are unique and making sure that the only MPs considered were born in the UK
            if name not in lines_seen and country == "United Kingdom": 

                #f.write(name + "            ")
                f.write(born + ",")
                f.write(bornlabel + ',')
                f.write(state + ",")
                f.write(coordinates + "\n")
                lines_seen.add(name)  #adding the name of the current MP to the set for uniqness 
                no_of_MPs = no_of_MPs + 1

        #f.write("------------ PARLIMENT NUMBER " + str(i+1) + " END ------------\n\n")

        #df = pd.read_csv("parliment"+str(i+1)+".csv", names=['longitude','latitude'])
        #df.to_csv("parliment"+str(i+1)+".csv", index=None)
    print("\n")
    print("number of MPs of current session = "+str(no_of_MPs))

#Function Calls
#get_data()

end = time.time()
print("runtime = " + str((end-start)/60) + " minutes")
print("\n")

#converting the text file to a csv with the proper headers for QGIS mapping
df = pd.read_csv('MPs.txt', names=["born","bornLabel","state",'latitude','longitude'])
df.to_csv('MPs.csv', index=None)

#print for confirmation
print((df["bornLabel"].value_counts()))