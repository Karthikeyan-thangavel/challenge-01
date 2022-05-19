import pandas as pd
a=pd.DataFrame(pd.read_excel("C:\\Users\\Karthikeyan\\Documents\\GitHub\\challenge-01\\table_data.xlsx",sheet_name=1))
b=pd.DataFrame(pd.read_excel("C:\\Users\\Karthikeyan\\Documents\\GitHub\\challenge-01\\table_data.xlsx",sheet_name=2))
print(a,b)