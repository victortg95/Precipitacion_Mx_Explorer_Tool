import pandas as pd
import altair as alt
from vega import VegaLite


df = pd.read_csv("../results/Clean_Data/precipitacion_mensual.csv", header=0)

def fetch_year(date):
    return date.split("-")[0]  #extrae el año

def fetch_month(date):
    return date.split("-")[1]  #extrae el mes

# BASE DE DATOS. Limpiamos la información para poder imprimirla más fácilmente
aux = pd.DataFrame(df.set_index("ENTIDAD").stack()).reset_index().rename(columns={"level_1":"FECHA", 0:"PRECIPITACION"})
aux["AÑO"] = aux["FECHA"].apply(fetch_year)
aux["MES"] = aux["FECHA"].apply(fetch_month)
aux = aux[(aux["ENTIDAD"]=="NACIONAL") | (aux["ENTIDAD"]=="NUEVO LEÓN") | (aux["ENTIDAD"]=="JALISCO")]

# Gráfica
alt.data_transformers.disable_max_rows()

chart = alt.Chart(aux).mark_rect().encode(
    alt.X("MES"),
    alt.Y("AÑO", sort="-y"),
    alt.Color("PRECIPITACION:Q"),
    alt.Column("ENTIDAD"),
    tooltip=["AÑO", "MES", "PRECIPITACION"]
).properties(
    title="Precipitación por mes y año en Nuevo León vs Nacional",
    width=200,
    height=500
)

#chart.save('templates/chart.html')

chart.save('templates/chart.html')