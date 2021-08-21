import io
import sys
import re

class JSONizer:
    def __init__(self, separator):
        self.data = ""
        self.jsonized_data = ""
        self.separator=separator
        
    def read_csv_data(self, filepath):
        with open(filepath, 'r') as file:
            self.data = file.read()
            
    def save_json_data(self, filepath):
        with open(filepath, 'w+') as file:
            file.write(self.jsonized_data)
            
    def jsonize(self, filepath, savepath):
        try:
            self.read_csv_data(filepath)
        except:
            print("Error while reading the input file - please check if the file exists and the data is correct")
        buffer = io.StringIO(self.data)
        data_classifier = buffer.readline()
        data_classifier = data_classifier.replace("\n","")
        data_classifier = data_classifier.split(self.separator)
        
        self.jsonized_data+="[\n"
        
        data_read = buffer.read()
        data_read=data_read.split('\n')
        data_read=data_read[:-1]
        
        for line in data_read:
            line = line.replace("\n","")
            line = line.split(self.separator)
            data = dict(zip(data_classifier, line))
            self.jsonized_data+="\t{\n"
            dat=""
            for k,v in data.items():
                dat+="\t\t\"" + k + "\":\"" + v + "\",\n"
            dat=dat[:-2] #delete the last empty line and comma
            self.jsonized_data+=dat
            self.jsonized_data+="\n\t},\n"
        
        self.jsonized_data = self.jsonized_data[:-2] #delete the last empty line and comma
        self.jsonized_data+="\n]"
        
        try:
            self.save_json_data(savepath)
        except:
            print("Error while saving the file - please check if the data is correct")

def validate_data(args):
    if len(args) < 2:
        if len(args)==1 and args[0].lower() in ("h","-h","--h","--help","-help","help","man"):
            print(""" 
            JSONizer by Mateusz Loska \n
            ------- version 1.0 -------
            JSONizer application converts .csv files into .json files.  \n
            \tPlease give the name of the file you want to convert to json and the path 
            you want to save the json data in. \n

            python jsonizer.py INPUT_FILE.CSV INPUT_FILE.JSON [SEPARATOR]
            
            depending on which separator you use in the CSV file you can specify the separator \n
            the default value is comma, so you can leave the field empty \n
            you can either pass a string or use one of the predefined values:
            comma space tab semicolon
          
            python jsonizer.py file1.csv file2.json semicolon

            """)
            return False
        else:
            print("Please specify the input and output file, example: \"python jsonizer.py input_data.csv output_data.json \" ")
            return False
    else:
        if not re.search(".*\.csv",args[0]):
            print("The input file must be a .csv file")
            return False
        if not re.search(".*\.json",args[1]):
            print("The output file has to be .json file")
            return False
    return True
        


if __name__ == "__main__":
    args = sys.argv[1:]
    separator = ","
    if validate_data(args):
        if len(args)==3:
            if args[2]=="tab":
                separator = "\t"
            if args[2]=="semicolon":
                separator = ";"
            if args[2]=="space":
                separator = " "
            if args[2]=="comma":
                separator = ","
            else:
                separator = args[2]
        jsonizer = JSONizer(separator)
        jsonizer.jsonize(args[0],args[1])


   