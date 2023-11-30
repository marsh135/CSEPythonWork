#pip install plotly
#pip install pandas
import plotly.express as px

gapminder_df = px.data.gapminder()
gapminder2002 = gapminder_df.query('year==2002')
gapminderUSA = gapminder_df.query('country==United States')
#print(gapminder2002.head())
print(gapminderUSA.head())