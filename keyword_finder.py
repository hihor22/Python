## Loading the required libraries

import os
import re
import pandas as pd

## Must have a text file folder 
## Setting the directory which hold our pdf files that were converted to .txt files

leaflets_dir = 'dump_profissional/'

## Setting the keywords we want to check on the drug leaflets we scraped from the brazilian drug agency ANVISA,
## Our maing goal is to find drug related information that could help us creating clinical decision support API's.

keywords = [
            'insuficiência hepática',
            'Insuficiência hepática', 
            'disfunção', 
            'disfunções', 
            'hepática', 
            'reajuste de dose', 
            'ajuste de dose', 
            'ajuste posológico',  
            'doença hepática', 
            'Insuficiência renal', 
            'insuficiência renal', 
            'renal', 
            'doença renal' 
            
]
# Creating a 'for loop' to iterate through the text files
rows = []
for root, dirs, files in os.walk(leaflets_dir):
    for f in files:
        keywords_in_leaflet = []
        keywords_not_in_leaflet = []

        leaflet_num = f.rpartition('_bula')[0].partition('bula')[-1]
        leaflet_filename = os.path.join(root, f)

        with open(leaflet_filename,'r',encoding='utf-8',errors='ignore') as l:
            leaflet = l.read()
            for k in keywords:
                if k in leaflet:
                    keywords_in_leaflet.append(k)
                else:
                    keywords_not_in_leaflet.append(k)

            rows.append([
                        leaflet_num, 
                        ', '.join(sorted(keywords_in_leaflet)), 
                        ', '.join(sorted(keywords_not_in_leaflet))
            ])
            
# Wrangling the data into a pandas dataframe

df = pd.DataFrame(
    data = rows,
    columns = [
               'leaflet_id',
               'keywords_in_leaflet',
               'keywords_not_in_leaflet'
    ]
)

# Testing unique values for keywords in leaflet
# df['keywords_in_leaflet'].unique()

# Writing the dataframe into an excel file.
df.to_excel('leaflets_keywords_hep_ren.xlsx', index = False)
