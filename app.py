#streamlit run OSA.py --server.maxUploadSize 2000 --server.maxMessageSize 2000
import streamlit as st
#import magic
import pandas as pd
import justpy as jp
import pandas as pd
from st_aggrid import GridOptionsBuilder, AgGrid, GridUpdateMode, DataReturnMode
from st_aggrid.shared import JsCode
import sqlite3
from dview import pull_selected_cache
#from dload import load_cache
import dload as dload
import dview as dview




def main():
    print('in hwere')
    dload.write_buffer()
    buf=dview.pull_selected_cache('gc')
    #st.write(buf)
    if st.sidebar.checkbox("Drop N/A"):
        buf=buf.dropna()
    st.write(buf)
    #dview.display_in_agGrid(buf)



if __name__ == "__main__":
  main()
