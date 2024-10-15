import time
import streamlit as st
import streamlit.components.v1 as components
from src import config
import src.data_utils as utils
import src.profiling as profiling
from pathlib import Path

# Configure page layout
st.set_page_config(layout="wide", page_title="Profiling Viz", page_icon=":bar_chart:")

# Application title and subtitle
st.title("Profiling Viz")
st.subheader("Automating Exploratory Data Analysis")

# Upload dataset file
dataset_file = st.file_uploader('Upload the dataset', type=['xlsx', 'csv'])

def load_data(file):
    """Load data based on file extension."""
    file_path = Path(file.name)
    if file_path.suffix == '.xlsx':
        return utils.load_excel(file)
    elif file_path.suffix == '.csv':
        return utils.load_csv(file)
    else:
        st.error("The dataset file extension is not recognized.")
        return None

def generate_reports(data):
    """Generate and display reports for the data."""
    if data is not None:
        start_time = time.time()  # Start timer
        
        with st.spinner('Generating reports...'):
            # Here you generate the reports
            profile_report = profiling.generate_profile_report(data)
            profiling.generate_sweetviz_report(data)
            profiling.generate_klib_report(data)

        end_time = time.time()  # End timer
        elapsed_time = end_time - start_time
        
        st.success("Reports generated successfully!")
        st.info(f"Time spent on report generation: {elapsed_time:.2f} seconds")

        # Setup tabs for reports
        tab1, tab2, tab3 = st.tabs(["ydata", "sweetviz", "klib"])

        # Display YData report
        with tab1:
            st.header("Ydata")
            components.html(profile_report, height=800, scrolling=True)

        # Display Sweetviz report
        with tab2:
            st.header("Sweetviz")
            with open(config.sweetviz_report_path, 'r') as f:
                sweetviz_html = f.read()
            components.html(sweetviz_html, height=800, scrolling=True)

        # Display Klib report
        with tab3:
            st.header("Klib")
            images = [config.klib_cat_plot_path, config.klib_dist_plot_path, config.klib_missing_val_plot_path]
            captions = ['Categorical Plot', 'Distribution Plot', 'Missing Values Plot']
            st.image(images, caption=captions, use_column_width=True)

# Handle file upload
if dataset_file is not None:
    data = load_data(dataset_file)
    generate_reports(data)