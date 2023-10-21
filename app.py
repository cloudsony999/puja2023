from glob import glob
from streamlit_image_viewer import image_viewer as i
import streamlit_toggle as tog
import streamlit as st

st.set_page_config(layout="wide")

image_path_list = glob('./image/*.jpg') + glob('./image/*.png') + glob('./image/*.enc')
st.markdown("<h1 style='text-align: center; color: maroon;'>!!!DURGAPUJO 2023 MOMENTS!!!</h1>", unsafe_allow_html=True)

setting_col, viewer_col, _ = st.columns([2,4,2])
with setting_col:
    st.markdown("## :gear: How you want to see?")
    n_col = st.number_input("n_col", min_value=1, max_value=10, value=3)
    n_raw = st.number_input("n_raw", min_value=1, max_value=10, value=2)
    is_visible_image_name = tog.st_toggle_switch(label="Show Image Names", 
        key="is_visible_image_name", 
        default_value=True, 
        label_after = False, 
        inactive_color = 'red', 
        active_color="yellow", 
        track_color="blue"
        )
    
with viewer_col:
    st.markdown("## :camera: Viewer")
    i(
        image_path_list,
        ncol=n_col,
        nrow=n_raw,
        image_name_visible=is_visible_image_name,
        key="image_viewer")
