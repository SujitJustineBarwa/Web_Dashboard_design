import pandas as pd
from dash import Dash, dcc, html
from dash.dependencies import Input, Output

# Load the Iris dataset
data = pd.read_csv("iris.csv")

# Unique species and features for dropdowns
species = data["species"].unique()
features = ["SepalLengthCm","SepalWidthCm","PetalLengthCm","PetalWidthCm"]

external_stylesheets = [
    {
        "href": (
            "https://fonts.googleapis.com/css2?"
            "family=Lato:wght@400;700&display=swap"
        ),
        "rel": "stylesheet",
    },
]

# Setup the Dash app
app = Dash(__name__,external_stylesheets=external_stylesheets)
app.title = "Iris Flower Data Exploration"
server = app.server

app.layout = html.Div(
    children=[
        html.Div(
            children=[
                html.H1(children="Iris Flower Data Exploration",className='header-title'),
                html.P("Visualize the Iris flower dataset features by species.",className="header-description"),
            ],
            className="header",
        ),
        html.Div(
            children=[
                html.Div(
                    children=[
                        html.P("Select the flower type :",className="dropdown-description"),
                        dcc.Dropdown(
                            id="species-selector",
                            options=[{"label": specie, "value": specie} for specie in species],
                            value=species[0],  # Default value
                            className="dropdown",
                        )
                    ]
                ),
                html.Div(
                    children=[
                        html.P("Select the feature :",className="dropdown-description"),
                        dcc.Dropdown(
                            id="feature-selector",
                            options=[{"label": feature, "value": feature} for feature in features],
                            value=features[0],  # Default value
                            className="dropdown",
                        )
                    ]
                )
            ],
            className="menu",
        ),
        dcc.Graph(id="feature-graph"),
        html.Footer(
            children=[
                html.P("© 2024 Sujit Justine Barwa. All Rights Reserved. ",className="footer"),
                html.A("View source code of this webpage on GitHub", href="https://github.com/SujitJustineBarwa/Web_Dashboard_design", target="_blank"),
            ],
            className="footer-container"
        ),
    ]
)


@app.callback(
    Output("feature-graph", "figure"),
    [Input("species-selector", "value"), Input("feature-selector", "value")],
)
def update_graph(selected_species, selected_feature):
    filtered_data = data[data["species"] == selected_species]
    figure = {
        "data": [
            {
                "x": filtered_data[selected_feature],
                "y": filtered_data.index,
                "type": "bar",
            },
        ],
        "layout": {
            "title": f"Distribution of {selected_feature} for {selected_species}",
            "xaxis": {"title": selected_feature},
            "yaxis": {"title": "Count"},
        },
    }
    return figure


if __name__ == "__main__":
    app.run_server(debug=True)
