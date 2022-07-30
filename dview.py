import streamlit as st
import magic
import pandas as pd
import justpy as jp
import pandas as pd
from st_aggrid import GridOptionsBuilder, AgGrid, GridUpdateMode, DataReturnMode
from st_aggrid.shared import JsCode
import sqlite3


cellsytle_jscode = JsCode(
    """
function(params) {
    if (params.value.includes('United States')) {
        return {
            'color': 'white',
            'backgroundColor': 'darkred'
        }
    } else {
        return {
            'color': 'black',
            'backgroundColor': 'white'
        }
    }
};
"""
)



def pull_selected_cache(working):


    conn = sqlite3.connect('/Users/marenomahony/Downloads/paradise_lost/tmp.sqlite')
    #selected_rows.to_sql('new_table_name', conn, if_exists='replace', index=True)
    if working=="wc":
        df=pd.read_sql('select * from new_table_name', conn)
    if  working=="gc":
        st.write('pulling global')
        df=pd.read_sql('select * from file_table_name', conn)
    conn.close()

    return(df)
    #df=df.dropna(how='all')


def display_in_agGrid(df):

    gb = GridOptionsBuilder.from_dataframe(df)
    gb.configure_selection(selection_mode="multiple", use_checkbox=True)
    gb.configure_pagination()
    gb.configure_side_bar()
    gb.configure_default_column(groupable=True, value=True, enableRowGroup=True, aggFunc="sum", editable=True)
    gridOptions = gb.build()

    data = AgGrid(
        df,
        gridOptions=gridOptions,
        enable_enterprise_modules=True,
        allow_unsafe_jscode=True,
        update_mode=GridUpdateMode.SELECTION_CHANGED
        )



    selected_rows = data["selected_rows"]
    selected_rows = pd.DataFrame(selected_rows)

    #st.write(selected_rows)
    #st.write(data)
    #if len(selected_rows)!=0:
    #     st.write(selected_rows)
    return(selected_rows)
