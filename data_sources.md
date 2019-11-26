* We planned on using the International Union for Conservation of Nature and Natural Resources (IUCN) API to get the 'status' of species based on the geographic region containing Glacier National Park.  Unfortunately, we were not able to get a token from IUCN in time.


1. We used the National Park Service to get a list of species in Glacier national park (excel file).


    https://irma.nps.gov/NPSpecies/Search/SpeciesList/GLAC


2. We got a list of endangered and threatened animals by scraping the Animal Welfare Institute's webpage on endangered/threatened animals using pandas (web scrape to dataframe).  This list is likely across the globe and may not be complete.


    https://awionline.org/content/list-endangered-species

    
3. We got a list of endangered and threatened plants from the United States Department of Agriculture (csv file).  This list is for the United States of America.


    https://plants.usda.gov/java/threat?fedlist=fed


The threatened/endangered animal data was fairly clean, though it was in multiple tables based on broad taxonomic groups.  We scraped the Animal Welfare Institute's website using pandas and created 11 dataframes, based on the broad taxonomic group.  We added a column for the broad group (i.e. Mammal, bird, etc.).  We then concatenated the 11 dataframes into one.  Finally, we saved the data in a csv file.


The threatened/endangered plant data was downloaded from the USDA in a csv file.  We imported the csv into a jupyter notebook using pandas.  There were several columns with data that was not useful to us.  We removed those columns.  We changed the threatened/endangered status codes (T and E) to the same coding used in the animal data (Threatened and Endangered).  We created a broad taxonomic group column similar to the animal data.  We concatenated the plant data to the animal data.  This was our final endangered/threatened dataframe.


We saved the excel spreadsheet of species in Glacier National Park as a csv file.  We cleaned up the data by importing the csv file into a jupyter notebook using pandas.  We removed columns with data that was unimportant to us and we changed the name of a few columns so they were similar to the threatened/endangered dataframe.