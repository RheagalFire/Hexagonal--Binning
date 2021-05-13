#Import Necessary Libraries
import numpy as np
import plotly.graph_objects as go
fig = go.Figure() 
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.figure_factory as ff
import plotly.express as px
import os

token=os.getenv("TOKEN")

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

def get_figs():
    px.set_mapbox_access_token(token)
    df = px.data.carshare()
    # Create Figures
    fig = ff.create_hexbin_mapbox(  
        data_frame=df, lat="centroid_lat", lon="centroid_lon",
        nx_hexagon=10, opacity=0.9, labels={"color": "Avg_Peak Hour"},color="peak_hour",agg_func=np.mean
    )
    fig.update_mapboxes(style='carto-positron')



    fig2= ff.create_hexbin_mapbox(  
    data_frame=df, lat="centroid_lat", lon="centroid_lon",
    nx_hexagon=10, opacity=0.9, labels={"color": "Summed Car Hours"},color="car_hours",agg_func=np.sum,color_continuous_scale="Icefire"
    )

    fig2.update_mapboxes(style='carto-positron')


    fig3= ff.create_hexbin_mapbox(  
    data_frame=df, lat="centroid_lat", lon="centroid_lon",min_count=1,
    nx_hexagon=10, opacity=0.9, labels={"color": "Point Count"},show_original_data=True,original_data_marker=dict(size=4,opacity=0.6,color="antiquewhite"),color_continuous_scale="Viridis"
    )
    fig3.update_mapboxes(style='carto-positron')


    return fig,fig2,fig3


