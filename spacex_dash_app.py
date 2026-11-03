# SpaceX Launch Records Dashboard (Plotly Dash)
# Lancer : python spacex_dash_app.py  puis ouvrir http://127.0.0.1:8050
import pandas as pd
import dash
from dash import html, dcc
from dash.dependencies import Input, Output
import plotly.express as px

# Telechargement du fichier : wget "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0321EN-SkillsNetwork/datasets/spacex_launch_dash.csv"
spacex_df = pd.read_csv("spacex_launch_dash.csv")
max_payload = spacex_df['Payload Mass (kg)'].max()
min_payload = spacex_df['Payload Mass (kg)'].min()

launch_sites = sorted(spacex_df['Launch Site'].unique())

app = dash.Dash(__name__)

app.layout = html.Div(children=[
    html.H1('SpaceX Launch Records Dashboard',
            style={'textAlign': 'center', 'color': '#503D36', 'font-size': 40}),

    # TASK 1 : liste deroulante des sites de lancement
    dcc.Dropdown(id='site-dropdown',
                 options=[{'label': 'All Sites', 'value': 'ALL'}] +
                         [{'label': site, 'value': site} for site in launch_sites],
                 value='ALL',
                 placeholder='Select a Launch Site here',
                 searchable=True),
    html.Br(),

    # TASK 2 : camembert des succes
    html.Div(dcc.Graph(id='success-pie-chart')),
    html.Br(),

    html.P("Payload range (Kg):"),
    # TASK 3 : curseur de plage de charge utile
    dcc.RangeSlider(id='payload-slider',
                    min=0, max=10000, step=1000,
                    marks={i: str(i) for i in range(0, 10001, 2500)},
                    value=[min_payload, max_payload]),

    # TASK 4 : nuage de points charge utile / resultat
    html.Div(dcc.Graph(id='success-payload-scatter-chart')),
])


# TASK 2 : callback du camembert
@app.callback(Output(component_id='success-pie-chart', component_property='figure'),
              Input(component_id='site-dropdown', component_property='value'))
def get_pie_chart(entered_site):
    if entered_site == 'ALL':
        fig = px.pie(spacex_df, values='class', names='Launch Site',
                     title='Total Success Launches By Site')
    else:
        filtered_df = spacex_df[spacex_df['Launch Site'] == entered_site]
        counts = filtered_df.groupby('class').size().reset_index(name='count')
        counts['Outcome'] = counts['class'].map({1: 'Success', 0: 'Failure'})
        fig = px.pie(counts, values='count', names='Outcome',
                     title=f'Total Success Launches for site {entered_site}')
    return fig


# TASK 4 : callback du nuage de points
@app.callback(Output(component_id='success-payload-scatter-chart', component_property='figure'),
              [Input(component_id='site-dropdown', component_property='value'),
               Input(component_id='payload-slider', component_property='value')])
def get_scatter_chart(entered_site, payload_range):
    low, high = payload_range
    df = spacex_df[(spacex_df['Payload Mass (kg)'] >= low) &
                   (spacex_df['Payload Mass (kg)'] <= high)]
    if entered_site == 'ALL':
        title = 'Correlation between Payload and Success for all Sites'
    else:
        df = df[df['Launch Site'] == entered_site]
        title = f'Correlation between Payload and Success for site {entered_site}'
    fig = px.scatter(df, x='Payload Mass (kg)', y='class',
                     color='Booster Version Category', title=title)
    return fig


if __name__ == '__main__':
    app.run()
