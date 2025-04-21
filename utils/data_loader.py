import pandas as pd
import streamlit as st

@st.cache_data 
def load_data():
    """Load all data required for the app."""
    # Load match statistics
    df_stats = pd.read_parquet('data/df_matches_results_stats.parquet')
    
    # Load summarized statistics
    df_sumstats = pd.read_parquet('data/df_matches_results_cumstats.parquet')
    
    return df_stats, df_sumstats