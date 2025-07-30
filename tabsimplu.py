from dash import dash_table
from flask import Flask, render_template
import pandas as pd
from sqlalchemy import create_engine
import dash
from dash import dcc, Dash
from dash import html
from dash.dependencies import Input, Output
import plotly.express as px
import os
import dash_bootstrap_components as dbc
from sqlalchemy.dialects.mssql.information_schema import columns

POSTGRES_ADDRESS=os.environ["POSTGRES_ADDRESS"]
POSTGRES_PORT=os.environ["POSTGRES_PORT"]
POSTGRES_USERNAME=os.environ["POSTGRES_USERNAME"]
POSTGRES_PASSWORD=os.environ["POSTGRES_PASSWORD"]
POSTGRES_DBNAME=os.environ["POSTGRES_DBNAME"]


postgres_str =('postgresql://{username}:{password}@{ipaddress}:{port}/{dbname}'.format (username=POSTGRES_USERNAME,password=POSTGRES_PASSWORD,ipaddress=POSTGRES_ADDRESS,port=POSTGRES_PORT,dbname=POSTGRES_DBNAME))

cnx=create_engine(postgres_str)

server = Flask(__name__)
@server.route('/')
def home():
    return render_template('index.html')


app = dash.Dash(
    __name__,
    server=server,
    url_base_pathname='/dash/'
)

# Încarcă datele

data_grouped= pd.read_sql_query('''Select jira_status AS "Status",priority
From jira_snapshot
Where issue_type='Problem Report'
Group by priority,jira_status ''' ,con=cnx)


pivot_table = pd.pivot_table(
    data_grouped,
    index='Status',
    columns='priority',
    aggfunc='size',
    fill_value=0
)

# Add row totals
pivot_table['Total'] = pivot_table.sum(axis=1)

total_row = pivot_table.sum(numeric_only=True)
total_row.name = 'Total'

# Append the total row using pd.concat (not append)
pivot_table = pd.concat([pivot_table, pd.DataFrame([total_row])])

# Reset index for Dash DataTable
pivot_table = pivot_table.reset_index()

columns = [{'name': col, 'id': col} for col in pivot_table.columns.astype(str)]

app.layout = dbc.Container([
    html.H1("Open PRs by Priority and Status", style={'textAlign': 'center'}),
    dash_table.DataTable(
        columns=columns,
        data=pivot_table.to_dict('records'),
        page_size=10,
        style_table={'overflowX': 'auto'},
        style_cell={'textAlign': 'center', 'minWidth': '100px', 'maxWidth': '180px', 'whiteSpace': 'normal'},
        style_data_conditional=[
            {
                'if': {'filter_query': '{Status} = "Total"'},
                'backgroundColor': 'rgb(240, 255, 255)',
                'fontWeight': 'bold'
            }
        ],
        sort_action='native',
        page_action='native'
    )
])

if __name__ == '__main__':
    app.run(debug=True)
