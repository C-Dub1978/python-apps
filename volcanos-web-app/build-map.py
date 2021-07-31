import pandas
import folium

volcanosDf = pandas.read_csv("./files/Volcanoes.txt")
latMean = volcanosDf['LAT'].mean()
longMean = volcanosDf['LON'].mean()

worldDf = pandas.read_json(open("./files/world.json"))
print(worldDf)

fMap = folium.Map(location=[latMean, longMean])
fMap.save("./files/index.html")