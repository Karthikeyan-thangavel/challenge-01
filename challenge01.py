import pandas as pd

ur="https://view.officeapps.live.com/op/view.aspx?src=https%3A%2F%2Fraw.githubusercontent.com%2FKarthikeyan-thangavel%2Fchallenge-01%2Fmain%2Ftable_data.xlsx&wdOrigin=BROWSELINK"
a=pd.DataFrame(pd.read_excel("C:\\Users\\Karthikeyan\\Documents\\GitHub\\challenge-01\\table_data.xlsx",sheet_name=1))
b=pd.DataFrame(pd.read_excel("C:\\Users\\Karthikeyan\\Documents\\GitHub\\challenge-01\\table_data.xlsx",sheet_name=2))
c=a.loc[a["id"].isin(b["employee_id"])==False]
print(c["first_name"]+" "+c["last_name"])
