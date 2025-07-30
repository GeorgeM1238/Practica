import pandas as pd
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px

df = pd.read_csv("sales_data.csv")

app = dash.Dash(__name__,suppress_callback_exceptions=True)

category_options = df['Category'].unique()
region_options = df['Region'].unique()

app.layout = html.Div([
    html.Label('Select columns for bar chart'),
    dcc.Dropdown(
        id='category-dropdown',
        options=[

    {'label': cat, 'value': cat} for cat in category_options
        ],
        value=list(category_options),
        multi=True,
        clearable=False,
        style={'width': '50%'}
    ),
    dcc.Dropdown(
        id='column-dropdown',
        options=[
            {'label': reg, 'value': reg} for reg in region_options

        ],
        value=region_options[0],
        multi=False,
        clearable=False,
        style={'width': '50%'}
    ),

    dcc.Graph(id='bar-chart')
])

@app.callback(
    Output('bar-chart', 'figure'),
    Input('category-dropdown', 'value'),
    Input('column-dropdown', 'value')
)
def update_figure(category_value, column_value):
    if isinstance(category_value, str):
        category_value= [category_value]
    filtered_df = df[(df['Region'] == column_value)]
    filtered_df=filtered_df[filtered_df['Category'].isin(category_value)]

    if filtered_df.empty:

        return px.bar(title="No data available for the selected filters.")

    bar_data = filtered_df.groupby('Category')['Sales'].sum().reset_index(name='number of sales')

    fig = px.bar(bar_data, x='Category', y='number of sales', title=f"Sales by category in {column_value}")
  #  fig.update_layout(barmode='group', xaxis_title='Category', yaxis_title='Total Sales')
    return fig
if __name__ == '__main__':
    app.run(debug=True)
