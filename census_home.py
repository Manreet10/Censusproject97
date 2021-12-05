# Show complete dataset and summary in 'census_home.py'
# Import necessary modules.
import streamlit as st

# Define a function 'app()' which accepts 'census_df' as an input.
def app(census_df):  

    st.header("View Data")
    # Display dataset within beta_expander.
    with st.beta_expander("View Full Dataset"):
        st.dataframe(census_df)
    # Show dataset summary on click of a checkbox.
    if st.checkbox("Show summary"):
        st.table(census_df.describe())

