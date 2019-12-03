## ETL Final Report from Sam Cooper and Cherie Mosher


**EXTRACT**


    ~ We planned on using the International Union for Conservation of Nature and Natural Resources (IUCN) API to get the 'status' of species based on the geographic region containing Glacier National Park.  Unfortunately, we were not able to get a token from IUCN in time.


    1. We used the National Park Service to get a list of species in Glacier national park (excel file).


        https://irma.nps.gov/NPSpecies/Search/SpeciesList/GLAC


    2. We got a list of endangered and threatened animals by scraping the Animal Welfare Institute's webpage on endangered/threatened animals using pandas (web scrape to dataframe).  This list is likely across the globe and may not be complete.


        https://awionline.org/content/list-endangered-species

    
    3. We got a list of endangered and threatened plants from the United States Department of Agriculture (csv file).  This list is for the United States of America.


        https://plants.usda.gov/java/threat?fedlist=fed

    * 4. We got a token for the IUCN API.  We pulled species and status for the United States into the app.py file.  The 'load' work was mainly done with the Glacier National Park data and the data from IUCN.  The IUCN data was downloaded using the app.py file and was saved as is into a mongo collection.

        http://apiv3.iucnredlist.org/api/v3/country/getspecies/US?token={IUCN_token}


**TRANSFORM**


    The threatened/endangered animal data was fairly clean, though it was in multiple tables based on broad taxonomic groups.  We scraped the Animal Welfare Institute's website using pandas and created 11 dataframes, based on the broad taxonomic group.  We added a column for the broad group (i.e. mammal, bird, etc.).  We then concatenated the 11 dataframes into one.  Finally, we saved the data in a csv file.


    The threatened/endangered plant data was downloaded from the USDA in a csv file.  We imported the csv into a jupyter notebook using pandas.  There were several columns with data that were not useful to us.  We removed those columns.  We changed the threatened/endangered status codes (T and E) to the same coding used in the animal data (Threatened and Endangered).  We created a broad taxonomic group column similar to the animal data.  We concatenated the plant data to the animal data.  This was our final endangered/threatened dataframe.


    We saved the excel spreadsheet of species in Glacier National Park as a csv file.  We cleaned up the data by importing the csv file into a jupyter notebook using pandas.  We removed columns with data that was unimportant to us and we changed the name of a few columns so they were similar to the threatened/endangered dataframe.  We saved the final dataframe to a csv file.

    * We merged the data from the IUCN API with the data for Glacier National Park using pandas.  We made sure to retain any species from the Glacier data that did not have a status from IUCN.


**LOAD**

    The goal was to store (a) the species in Glacier National Park and (b) the status (threatened or endangered) of the species in that park.


    We transformed the final dataframe to json, making sure to orient as records.


    We set up a mongo database for the data.  We loaded the Glacier National Park data (with IUCN status) inta a collection.  
    

    The goal is to use flask to render a web application that allows users to filter species in Glacier National Park by taxonomic group and status/category.

