from datetime import date
import pandas as pd

list_first_names=[]
list_last_names=[]
list_number=[]
list_datetime=[]

choix=input('Insérer un contact? Y/N \n')

while choix=='Y'
    Last_name=input("last name: \n")
    list_last_names.append(Last_name)
    First_name=input("first name: \n")
    list_first_names.append(First_name)
    number=input('number: \n')
    list_number.append(number)
    creation_date=date.today
    list_datetime.append(creation_date)
    choix=input('Insérer un contact? Y/N \n')

dict = {
    "first_name" : list_first_names ,
    "last_name" : list_last_names ,
    "number" : list_number,
    "creation_date" : list_datetime ,
}

data=pd.DataFrame(dict)
data.to_csv('Directory/Data.csv', index = False )
data_csv=pd.read_csv('Data.csv')





