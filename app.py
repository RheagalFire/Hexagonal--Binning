import os
import plots
import dash
import dash_core_components as dcc
import dash_html_components as html


colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

fig,fig2,fig3=plots.get_figs()


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__,external_stylesheets=external_stylesheets)
markdown='''
### Dash App
Hexagonal Binning of Carshare Data.    
'''
html_h3=html.H3(children="Average Peak Hour Graph",style={'textAlign':'center'})
html_h3_2=html.H3(children="Summed Car Hour",style={'textAlign':'center'})
html_h3_3=html.H3(children="Point Count With Point Markers",style={'textAlign':'center'})

app.layout = html.Div(style={'color':colors['text'],'backgroundColor': colors['background']},children=[
    dcc.Markdown(children=markdown),
    html_h3,
    dcc.Graph(figure=fig),
    html_h3_2,
    dcc.Graph(figure=fig2),
    html_h3_3,
    dcc.Graph(figure=fig3),
    
])
if __name__=="__main__":
    app.run_server(debug=True)