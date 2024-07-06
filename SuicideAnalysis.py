# %%
#Setup
import pandas as pd
import plotly_express as px
import numpy as np
# %%
#Load the Dataset
df = pd.read_csv("master.csv")
df
# %%
# Group countries by average suicide rate
avg = df.groupby("country")["suicides/100k pop"].mean().reset_index()
# Sort values descending and the first 10
avg = avg.sort_values("suicides/100k pop", ascending=False).head(10)
# Chart
fig = px.histogram(
    avg,
    x="country",
    y="suicides/100k pop",
    color="country",
    title="1985-2016 Suicide Rate Avg"
)
fig.update_layout(
    xaxis_title= "Country",
    yaxis_title= "Suicides for 100k people",
    legend_title= "Country"
)
fig.show()
# %%
# Filter for year only 2000+
df1 = df.query("year >= 2000")
# Group countries by average suicide rate
avg1 = df1.groupby("country")["suicides/100k pop"].mean().reset_index()
# Sort values descending and the first 10
avg1 = avg1.sort_values("suicides/100k pop", ascending=False).head(10)
# Chart
fig1 = px.histogram(
    avg1,
    x="country",
    y="suicides/100k pop",
    color="country",
    title="2000-2016 Suicide Rate Avg"
)
fig1.update_layout(
    xaxis_title= "Country",
    yaxis_title= "Suicides for 100k people",
    legend_title= "Country"
)
fig1.show()
# %%
# Filter to 2015 and to Korea and Lithuania
df2 = df.query("year == 2015 and country == 'Republic of Korea' or country == 'Lithuania'")

# Group by age and country and avg the suicide rate, sort and first 10
avg2 = df2.groupby(["country", "age"])["suicides/100k pop"].mean().reset_index().sort_values("suicides/100k pop", ascending=False)
# Combine country and age into a column
avg2["country_age"] = avg2['country'] + ' ' + avg2['age'].astype(str)
# Chart
fig2 = px.histogram(
    avg2,
    x="country_age",
    y="suicides/100k pop",
    color="country_age",
    title="2015 Korea and Lithuania Suicide Rates Ages"
)
fig2.update_layout(
    xaxis_title = "Country and Age",
    yaxis_title = "Suicides for 100k people",
    legend_title= "Country and Age"
)
fig2.show()
# %%
# Filter to 2015 and to Korea and Male
df3 = df.query("year == 2015 and country == 'Republic of Korea'")
df3 = df3.query("age == '75+ years'")
# Group by sex and avg the suicide rate, sort and first 10
avg3 = df3.groupby("sex")["suicides/100k pop"].mean().reset_index().sort_values("suicides/100k pop", ascending=False)
# Chart
fig3 = px.histogram(
    avg3,
    x="sex",
    y="suicides/100k pop",
    color="sex",
    title="2015 Korea Suicide Rates 75+ Years"
)
fig3.update_layout(
    xaxis_title = "Sex",
    yaxis_title = "Suicides for 100k people",
    legend_title= "Sex"
)
fig3.show()
# %%
# Average HDI for country compared to suicide rate top 30 HDI
# Group by country, average HDI and suicide rate
df4 = df.groupby("country")[["HDI for year", "suicides/100k pop"]].mean().reset_index()
df4 = df4.sort_values("HDI for year", ascending=False).head(30)
print(f"(30 Top HDI)Suicides per 100k pop:{round(df4["suicides/100k pop"].mean(), 2)}")

# Average HDI for country compared to suicide rate last 30 HDI
# Group by country, average HDI and suicide rate
df5 = df.groupby("country")[["HDI for year", "suicides/100k pop"]].mean().reset_index()
df5 = df5.sort_values("HDI for year", ascending=True).head(30)
print(f"(30 Last HDI)Suicides per 100k pop:{round(df5["suicides/100k pop"].mean(), 2)}")
print(f"Top 30 is an increase of {round(df4["suicides/100k pop"].mean() / df5["suicides/100k pop"].mean() * 100 - 100, 2)}%")
# %%
# Average GDP for country compared to suicide rate top 30 GDP
# Group by country, average gdp and suicide rate
df6 = df.groupby("country")[["gdp_per_capita ($)", "suicides/100k pop"]].mean().reset_index()
df6 = df6.sort_values("gdp_per_capita ($)", ascending=False).head(30)
print(f"(30 Top GDP)Suicides per 100k pop:{round(df6["suicides/100k pop"].mean(), 2)}")

# Average GDP for country compared to suicide rate last 30 GDP
# Group by country, average gdp and suicide rate
df7 = df.groupby("country")[["gdp_per_capita ($)", "suicides/100k pop"]].mean().reset_index()
df7 = df7.sort_values("gdp_per_capita ($)", ascending=True).head(30)
print(f"(30 Last GDP)Suicides per 100k pop:{round(df7["suicides/100k pop"].mean(), 2)}")
print(f"Top 30 is an increase of {round(df6["suicides/100k pop"].mean() / df7["suicides/100k pop"].mean() * 100 - 100, 2)}%")
# %%
