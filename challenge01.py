import pandas as pd
url="C:\\Users\\Karthikeyan\\Documents\\GitHub\\challenge-01\\table_data.xlsx"
a=pd.DataFrame(pd.read_excel(url,sheet_name=1))
b=pd.DataFrame(pd.read_excel(url,sheet_name=2))
c=a.loc[a["id"].isin(b["employee_id"])==False]
print(c["first_name"]+" "+c["last_name"])