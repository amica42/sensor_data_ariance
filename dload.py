# Load data into database

import streamlit as st
import magic
import pandas as pd
import justpy as jp
import pandas as pd
from st_aggrid import GridOptionsBuilder, AgGrid, GridUpdateMode, DataReturnMode
from st_aggrid.shared import JsCode
import sqlite3
from dview import pull_selected_cache

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

def write_buffer():

    uploaded_file = st.sidebar.file_uploader("Choose a file")

#Load the existing data if noting new is added

    if uploaded_file is None:
        print('Loaded Data')
        pull_selected_cache('gc')

#load new file if uploaded
    if uploaded_file is not None:
         st.write('updating buffer',uploaded_file)
         df1 = pd.read_csv(uploaded_file)
         df1.to_csv(uploaded_file, index = None)
         conn = sqlite3.connect('/Users/marenomahony/Downloads/paradise_lost/tmp.sqlite')
         df1.to_sql('file_table_name', conn, if_exists='replace', index=True)
          #df=pd.read_sql('select * from new_table_name', conn)
         conn.close()
         st.write(df1)
         #pull_selected_cache('gc')
         gb = GridOptionsBuilder.from_dataframe(df1)
         gb.configure_selection(selection_mode="multiple", use_checkbox=True)
         gb.configure_pagination()
         gb.configure_side_bar()
         gb.configure_default_column(groupable=True, value=True, enableRowGroup=True, aggFunc="sum", editable=True)
         gridOptions = gb.build()

         data = AgGrid(
            df1,
            gridOptions=gridOptions,
            enable_enterprise_modules=True,
            allow_unsafe_jscode=True,
            update_mode=GridUpdateMode.SELECTION_CHANGED
            )


         selected_rows = data["selected_rows"]
         selected_rows = pd.DataFrame(selected_rows)
         conn = sqlite3.connect('/Users/marenomahony/Downloads/paradise_lost/tmp.sqlite')
         df1.to_sql('file_table_name', conn, if_exists='replace', index=True)
          #df=pd.read_sql('select * from new_table_name', conn)
         conn.close()

         if len(selected_rows)!=0:
             st.write(selected_rows)

             conn = sqlite3.connect('/Users/marenomahony/Downloads/paradise_lost/tmp.sqlite')
             selected_rows.to_sql('new_table_name', conn, if_exists='replace', index=True)
             df1.to_sql('file_table_name', conn, if_exists='replace', index=True)
             #df=pd.read_sql('select * from new_table_name', conn)
             conn.close()


def load_cache():

    uploaded_file = st.sidebar.file_uploader("Choose a file")

    if uploaded_file is None:
        st.write('Loaded Data')
        pull_selected_cache('gc')
        st.write('Selected Working Data')
        pull_selected_cache('wc')



    if uploaded_file is not None:
         #st.write(uploaded_file)
         df1 = pd.read_csv(uploaded_file)
         df1.to_csv(uploaded_file, index = None)
         #st.write(df1)
         #AgGrid(df1)
         gb = GridOptionsBuilder.from_dataframe(df1)
         gb.configure_selection(selection_mode="multiple", use_checkbox=True)
         gb.configure_pagination()
         gb.configure_side_bar()
         gb.configure_default_column(groupable=True, value=True, enableRowGroup=True, aggFunc="sum", editable=True)
         gridOptions = gb.build()

         data = AgGrid(
            df1,
            gridOptions=gridOptions,
            enable_enterprise_modules=True,
            allow_unsafe_jscode=True,
            update_mode=GridUpdateMode.SELECTION_CHANGED
            )


         selected_rows = data["selected_rows"]
         selected_rows = pd.DataFrame(selected_rows)
         conn = sqlite3.connect('/Users/marenomahony/Downloads/paradise_lost/tmp.sqlite')
         df1.to_sql('file_table_name', conn, if_exists='replace', index=True)
          #df=pd.read_sql('select * from new_table_name', conn)
         conn.close()

         if len(selected_rows)!=0:
             st.write(selected_rows)

             conn = sqlite3.connect('/Users/marenomahony/Downloads/paradise_lost/tmp.sqlite')
             selected_rows.to_sql('new_table_name', conn, if_exists='replace', index=True)
             df1.to_sql('file_table_name', conn, if_exists='replace', index=True)
             #df=pd.read_sql('select * from new_table_name', conn)
             conn.close()

             if st.sidebar.checkbox('Graph'):
                 st.write('pass data to graph objects')
                 df=pull_selected_cache('wc')
                 st.write(df)
