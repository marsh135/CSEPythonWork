#pip install plotly
#pip install pandas
import plotly.express as px

gapminder_df = px.data.gapminder()

print(gapminder_df.head())