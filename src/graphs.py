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
    width=200,
    height=500
)

#chart.save('templates/chart.html')

chart.save('templates/chart.html')

################# GEOPANDAS


import geopandas as gpd
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib_scalebar.scalebar import ScaleBar

gdf_mexico = gpd.read_file('../data/mapa_mexico/').set_index('CLAVE').to_crs(epsg=4485)

df = pd.read_csv("../results/Clean_Data/precipitacion_anual.csv", header=0)
new_df = df.iloc[:-1, 1:]
edos = gdf_mexico.dissolve(by='CVE_EDO')

edos = edos.reset_index(drop=True)
new_df = new_df.reset_index(drop=True)

# Convert GeoDataFrames to DataFrames
df1 = edos.drop(columns=['geometry','NOM_MUN','CVE_MUNI'])
# Concatenate the DataFrames along the columns
result_df = pd.concat([df1, new_df], axis=1)

# Convert the concatenated DataFrame back to a GeoDataFrame
result_gdf = gpd.GeoDataFrame(result_df, geometry=edos.geometry)

def plot_precipitation_for_year(year, gdf):
    # Crear un objeto de figura y ejes
    fig, ax = plt.subplots(figsize=(8, 6))

    # Plotear el GeoDataFrame con la columna del año dado
    gdf.plot(column=str(year), legend=True, ax=ax)

    # Eliminar los valores en los ejes
    ax.set_axis_off()

    # Establecer el título del gráfico
    plt.title(f'Precipitación Acumulada [mm] promedio para el año {year}')
    plt.savefig("static/" + str(year) + "precipitacion.png")
    plt.close()


#for i in range(1985,2023):
#    plot_precipitation_for_year(i,result_gdf)
    