import pandas as pd
import plotly.express as px

df_campamentos = pd.read_excel("Campamentos_2019.xlsx")

df_filtrado = df_campamentos[df_campamentos["region"] == "Biobío"]
df_arauco = df_filtrado[df_filtrado['provincia'] == "Arauco"]


val_p4 = df_arauco['p4'].value_counts().index
cant_p4 = list(df_arauco['p4'].value_counts())
fig = px.bar(df_arauco, x=val_p4, y=cant_p4) 
fig.show()
