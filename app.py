import dash
from dash import dcc, html
from dash.dependencies import Input, Output, State
import pandas as pd
import joblib

# Load the trained model
pipeline = joblib.load('sales_prediction_model.pkl')

# Initialize the Dash app
app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Adidas Sales Prediction"),
    
    # Add input fields for each feature
    html.Div([
        html.Label("Price per Unit"),
        dcc.Input(id='price_per_unit', type='number', value=''),
    ]),
    html.Div([
        html.Label("Region"),
        dcc.Input(id='region', type='text', value=''),
    ]),
    html.Div([
        html.Label("Product"),
        dcc.Input(id='product', type='text', value=''),
    ]),
    html.Div([
        html.Label("Operating Margin"),
        dcc.Input(id='operating_margin', type='number', value=''),
    ]),
    html.Div([
        html.Label("Operating Profit"),
        dcc.Input(id='operating_profit', type='number', value=''),
    ]),
    html.Div([
        html.Label("State"),
        dcc.Input(id='state', type='text', value=''),
    ]),
    html.Div([
        html.Label("Invoice Date"),
        dcc.Input(id='invoice_date', type='text', value=''),
    ]),
    html.Div([
        html.Label("Retailer"),
        dcc.Input(id='retailer', type='text', value=''),
    ]),
    html.Div([
        html.Label("City"),
        dcc.Input(id='city', type='text', value=''),
    ]),
    html.Div([
        html.Label("Retailer ID"),
        dcc.Input(id='retailer_id', type='text', value=''),
    ]),
    html.Div([
        html.Label("Units Sold"),
        dcc.Input(id='units_sold', type='number', value=''),
    ]),
    html.Div([
        html.Label("Sales Method"),
        dcc.Input(id='sales_method', type='text', value=''),
    ]),
    
    html.Button('Predict', id='predict-button', n_clicks=0),
    
    html.Div(id='prediction-output')
])

@app.callback(
    Output('prediction-output', 'children'),
    [Input('predict-button', 'n_clicks')],
    [State('price_per_unit', 'value'),
     State('region', 'value'),
     State('product', 'value'),
     State('operating_margin', 'value'),
     State('operating_profit', 'value'),
     State('state', 'value'),
     State('invoice_date', 'value'),
     State('retailer', 'value'),
     State('city', 'value'),
     State('retailer_id', 'value'),
     State('units_sold', 'value'),
     State('sales_method', 'value')]
)
def predict_sales(n_clicks, price_per_unit, region, product, operating_margin, operating_profit, state, invoice_date, retailer, city, retailer_id, units_sold, sales_method):
    if n_clicks > 0:
        # Create a DataFrame for the input features
        input_data = pd.DataFrame({
            'Price per Unit': [price_per_unit],
            'Region': [region],
            'Product': [product],
            'Operating Margin': [operating_margin],
            'Operating Profit': [operating_profit],
            'State': [state],
            'Invoice Date': [invoice_date],
            'Retailer': [retailer],
            'City': [city],
            'Retailer ID': [retailer_id],
            'Units Sold': [units_sold],
            'Sales Method': [sales_method]
        })
        
        # Make prediction
        prediction = pipeline.predict(input_data)
        
        return f'Predicted Sales: ${prediction[0]:,.2f}'
    return ''

if __name__ == '__main__':
    app.run_server(debug=True)