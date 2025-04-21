import streamlit as st
from utils.data_loader import load_data
from utils.plot_loader import create_chart
from streamlit.components.v1 import html

def general_results():
    
    st.header("League Summary")

    # Load data
    df_stats, df_cumstats = load_data()

    # Filters for General Results
    league_rounds = df_stats['league_round'].unique()
    
    selected_round = st.slider( 
        "Pick a League Round:",
        min_value=min(league_rounds),
        max_value=max(league_rounds),
        value=max(league_rounds),  # valor inicial
        step=1,
    )

    # Filter data based on selected league_round
    filtered_stats = df_stats[df_stats['league_round'] == selected_round].reset_index(drop=True)
    filtered_cumstats = df_cumstats[df_cumstats['league_round'] == selected_round].reset_index(drop=True)
    # sort values by points
    filtered_cumstats = filtered_cumstats.sort_values(by='points', ascending=False).reset_index(drop=True)
    filtered_cumstats["position"] = filtered_cumstats.index + 1 

    # remove columns match_id, match_date, match_type, team_against, result, ball_possession
    filtered_cumstats = filtered_cumstats.drop(columns=['match_id', 'match_date', 'match_type', 'team_against', 'result', 'ball_possession']) 
    # format columns names
    filtered_cumstats.columns = filtered_cumstats.columns.str.replace('_', ' ').str.title()
    # rename 'Score': 'Goals', 'Score Against': 'Goals Against', 'Score Difference': 'Goals Difference'
    filtered_cumstats = filtered_cumstats.rename(columns={'Score': 'Goals', 'Score Against': 'Goals Against', 'Score Difference': 'Goals Difference'})


    default_columns = ['Position', 'Team', 'Points', 'Goals', 'Goals Against', 'Goals Difference']
    # Select columns to display
    selected_columns = st.multiselect(
        "Pick columns to display:",
        options=filtered_cumstats.columns.tolist(),
        default=default_columns  # por padrão, mostra as 3 primeiras
    )
    filtered_cumstats = filtered_cumstats[selected_columns]

    filtered_cumstats_style = (
        filtered_cumstats
        .style
        .set_properties(**{'background-color': '#FFFFFF','color': 'black'})
    )
    

    # Display data
    st.subheader(f"Standings - Round {selected_round}")
    st.dataframe(filtered_cumstats_style, use_container_width=True, hide_index=True)

    # Visualizations
    df = df_cumstats[["team", "points", "league_round"]]
    CHART = create_chart(df, selected_round)
    
    html(CHART, width=900, height=650)
