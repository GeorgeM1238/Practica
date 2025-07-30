import pandas as pd
import plotly
import plotly.express as px
import plotly.io as pio

data = {'Language': ['English', 'Mandarin', 'Hindi', 'Spanish', 'French', 'Arabic', 'Bengali', 'Russian', 'Portuguese',
                     'Others'], 'Speakers (millions)': [1500, 1117, 615, 534, 280, 274, 273, 258, 234, 1000],
        'Region/Countries': ['Worldwide', 'China, Taiwan, Singapore', 'India, Nepal, Fiji', 'Spain, Latin America',
                             'France, Canada, Africa', 'Middle East, North Africa', 'Bangladesh, India',
                             'Russia, Eastern Europe', 'Brazil, Portugal, Africa', 'Various'],
        'Dialects': [160, 10, 50, 20, 30, 25, 12, 15, 21, 100]}

df = pd.DataFrame(data)

df=df.sort_values("Speakers (millions)", ascending=False)
df=df.head(5)


pie_chart = px.pie(
    data_frame=df,
    values="Speakers (millions)",
    names="Language",
    color="Language",
    color_discrete_sequence=['#ADD8E6', '#87CEEB', '#6495ED', '#4682B4'],
    title="Limbi vorbite in lume",
    template="presentation",
    width=800,
    height=600,

    custom_data=["Region/Countries", "Dialects"]
)

pie_chart.update_traces(
    hovertemplate=(
            "<b>%{label}</b><br>" 
            "Regions: %{customdata[0][0]}<br>" +
            "Dialects: %{customdata[0][1]}<extra></extra>"
    ),
    textinfo="label+percent",
pull=[0,0,0.5,0,0,0.2,0,0,0,0])



pie_chart.show()
