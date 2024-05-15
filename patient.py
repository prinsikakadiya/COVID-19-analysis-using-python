import streamlit as st
from PIL import Image
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
import pandas as pd
from streamlit_option_menu import option_menu 
import numpy as np
# from local_components import card_container

def app():
        st.title('COVID-19 ANALYSIS')

        img = Image.open('./static/covid.jpg')
        st.image(img,use_column_width=True)

        col1, col2, col3 = st.columns(3)
    
        col1.error('Active - 3552')
        col2.success('Discharged - 44143665')
        col3.warning('Deaths - 530698')

        df= pd.read_csv('weekly_data.csv')
        df2= pd.read_csv('covid.csv')



        # -----------------------1st chart-------------------------------
            
        st.subheader("Weekly COVID-19 Cases Across India by Date")
        # Create the line plot
        end_dates = df['enddate']
        total_cases = df['total']
        fig, ax = plt.subplots(figsize=(18, 9))
        ax.plot(end_dates, total_cases, marker='o', color='blue', linestyle='-')
        ax.set_xlabel('End Date')
        ax.set_ylabel('Total COVID-19 Cases')
        ax.set_title('Distribution of Total COVID-19 Cases by End Date')
        plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
        ax.grid(True)  # Add grid lines

        # Format y-axis labels to display in millions
        formatter = FuncFormatter(lambda x, _: '{:,.0f}'.format(x))
        ax.yaxis.set_major_formatter(formatter)

        # Add annotations
        for date, cases in zip(end_dates, total_cases):
            ax.annotate(f'{cases:,.0f}', (date, cases), textcoords="offset points", xytext=(0,10), ha='center')

        # Adjust layout to prevent clipping of labels
        plt.tight_layout()

        # Display the plot in Streamlit
        st.pyplot(fig)

        # -----------------------2nd chart-------------------------------

        def generate_sales_data():
            state = df2['state']
            confirmed_cases = df2['confirmed']
            return pd.DataFrame({'State': state, 'Confirmed_cases': confirmed_cases})

# Define Vega-Lite specification
        vega_lite_spec = {
    "layer": [
        {
            "mark": {"type": "rect", "stroke": "black", "strokeWidth": 1},  # Add a rectangle mark for border
            "encoding": {
                "x": {"field": "State", "type": "ordinal"},
                "y": {"field": "Confirmed_cases", "type": "quantitative", "axis": {"grid": False}},
            }
        },
        {
            "mark": {"type": "bar", "tooltip": True, "fill": "#00b7c7", "cornerRadiusEnd": 1},
            "encoding": {
                "x": {"field": "State", "type": "ordinal"},
                "y": {"field": "Confirmed_cases", "type": "quantitative", "axis": {"grid": False}},
                "text": {"field": "Confirmed_cases", "type": "quantitative"}
            }
        },
        {
            "mark": {"type": "rule", "color": "black"},
            "encoding": {
                "y": {"field": "Confirmed_cases", "type": "quantitative"},
                "y2": {"value": 0},
                "x": {"field": "State", "type": "ordinal"}
            }
        }
    ]
}


# Display the Vega-Lite chart
        st.subheader("Confirmed COVID-19 Cases by State")
        st.vega_lite_chart(generate_sales_data(), vega_lite_spec, use_container_width=True)

        # -----------------------3rd chart-------------------------------
        def generate_sales_data():
            state = df2['state']
            active_cases = df2['active']

            return pd.DataFrame({'State': state, 'Active_cases': active_cases})

# Define Vega-Lite specification
        vega_lite_spec = {
    "layer": [
        {
            "mark": {"type": "rect", "stroke": "black", "strokeWidth": 1},  # Add a rectangle mark for border
            "encoding": {
                "x": {"field": "State", "type": "ordinal"},
                "y": {"field": "Active_cases", "type": "quantitative", "axis": {"grid": False}},
            }
        },
        {
            "mark": {"type": "bar", "tooltip": True, "fill": "#00b7c7", "cornerRadiusEnd": 1},
            "encoding": {
                "x": {"field": "State", "type": "ordinal"},
                "y": {"field": "Active_cases", "type": "quantitative", "axis": {"grid": False}},
                "text": {"field": "Active_cases", "type": "quantitative"}
            }
        },
        {
            "mark": {"type": "rule", "color": "black"},
            "encoding": {
                "y": {"field": "Active_cases", "type": "quantitative"},
                "y2": {"value": 0},
                "x": {"field": "State", "type": "ordinal"}
            }
        }
    ]
}


# Display the Vega-Lite chart
        st.subheader("active COVID-19 Cases by State")
        st.vega_lite_chart(generate_sales_data(), vega_lite_spec, use_container_width=True)


        # -----------------------4th chart-------------------------------
        def generate_sales_data():
            state = df2['state']
            passive_cases = df2['passive']
            return pd.DataFrame({'State': state, 'Passive_cases': passive_cases})

# Define Vega-Lite specification
        vega_lite_spec = {
    "layer": [
        {
            "mark": {"type": "rect", "stroke": "black", "strokeWidth": 1},  # Add a rectangle mark for border
            "encoding": {
                "x": {"field": "State", "type": "ordinal"},
                "y": {"field": "Passive_cases", "type": "quantitative", "axis": {"grid": False}},
            }
        },
        {
            "mark": {"type": "bar", "tooltip": True, "fill": "#00b7c7", "cornerRadiusEnd": 1},
            "encoding": {
                "x": {"field": "State", "type": "ordinal"},
                "y": {"field": "Passive_cases", "type": "quantitative", "axis": {"grid": False}},
                "text": {"field": "Passive_cases", "type": "quantitative"}
            }
        },
        {
            "mark": {"type": "rule", "color": "black"},
            "encoding": {
                "y": {"field": "Passive_cases", "type": "quantitative"},
                "y2": {"value": 0},
                "x": {"field": "State", "type": "ordinal"}
            }
        }
    ]
}


# Display the Vega-Lite chart
        st.subheader("COVID-19 Recovered Cases by State")
        st.vega_lite_chart(generate_sales_data(), vega_lite_spec, use_container_width=True)

       
        
        # -----------------------5th chart-------------------------------
        def generate_sales_data():
            state = df2['state']
            deaths_cases = df2['deaths']
            return pd.DataFrame({'State': state, 'Deaths_cases': deaths_cases})

# Define Vega-Lite specification
        vega_lite_spec = {
    "layer": [
        {
            "mark": {"type": "rect", "stroke": "black", "strokeWidth": 1},  # Add a rectangle mark for border
            "encoding": {
                "x": {"field": "State", "type": "ordinal"},
                "y": {"field": "Deaths_cases", "type": "quantitative", "axis": {"grid": False}},
            }
        },
        {
            "mark": {"type": "bar", "tooltip": True, "fill": "#00b7c7", "cornerRadiusEnd": 1},
            "encoding": {
                "x": {"field": "State", "type": "ordinal"},
                "y": {"field": "Deaths_cases", "type": "quantitative", "axis": {"grid": False}},
                "text": {"field": "Deaths_cases", "type": "quantitative"}
            }
        },
        {
            "mark": {"type": "rule", "color": "black"},
            "encoding": {
                "y": {"field": "Deaths_cases", "type": "quantitative"},
                "y2": {"value": 0},
                "x": {"field": "State", "type": "ordinal"}
            }
        }
    ]
}


# Display the Vega-Lite chart
        st.subheader("COVID-19 Deaths by State")
        st.vega_lite_chart(generate_sales_data(), vega_lite_spec, use_container_width=True)

        
        #---------------------------------------------------------------

        def generate_sales_data():
            state = df2['state']
            confirmed_cases = df2['population']
            return pd.DataFrame({'State': state, 'Confirmed_cases': confirmed_cases})

# Define Vega-Lite specification
        vega_lite_spec = {
    "layer": [
        {
            "mark": {"type": "rect", "stroke": "black", "strokeWidth": 1},  # Add a rectangle mark for border
            "encoding": {
                "x": {"field": "State", "type": "ordinal"},
                "y": {"field": "Confirmed_cases", "type": "quantitative", "axis": {"grid": False}},
            }
        },
        {
            "mark": {"type": "bar", "tooltip": True, "fill": "#00b7c7", "cornerRadiusEnd": 1},
            "encoding": {
                "x": {"field": "State", "type": "ordinal"},
                "y": {"field": "Confirmed_cases", "type": "quantitative", "axis": {"grid": False}},
                "text": {"field": "Confirmed_cases", "type": "quantitative"}
            }
        },
        {
            "mark": {"type": "rule", "color": "black"},
            "encoding": {
                "y": {"field": "Confirmed_cases", "type": "quantitative"},
                "y2": {"value": 0},
                "x": {"field": "State", "type": "ordinal"}
            }
        }
    ]
}


# Display the Vega-Lite chart
        st.subheader("Population by State")
        st.vega_lite_chart(generate_sales_data(), vega_lite_spec, use_container_width=True)

        