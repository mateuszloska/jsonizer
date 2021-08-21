JSONizer by Mateusz Loska
------- version 1.0 -------
 JSONizer application converts .csv files into .json files. 
Please give the name of the file you want to convert to json and the path you want to save the json data in.

python jsonizer.py INPUT_FILE.CSV INPUT_FILE.JSON [SEPARATOR]
            
depending on which separator you use in the CSV file you can specify the separator 
the default value is comma, so you can leave the field empty
you can either pass a string or use one of the predefined values:
comma space tab semicolon
example:
python jsonizer.py file1.csv file2.json semicolon
