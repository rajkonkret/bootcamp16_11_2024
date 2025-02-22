from dash import Dash, dcc, html
import plotly.express as px
import pandas as pd

df = pd.DataFrame({
    "Miasto" : ["Warszawa", 'Kraków', "Gliwice", "Łódź"],
    "Populacja": [1790658, 779115, 169750, 655345]
})

fig = px.bar(df, x="Miasto", y="Populacja", title="Populacja polskich miast")

app = Dash(__name__)

app.layout = html.Div([
    html.H1("Dashboard z Dash i Plotly"),
    dcc.Graph(id='bar-chart', figure=fig)
])

if __name__ == "__main__":
    app.run_server(debug=True)