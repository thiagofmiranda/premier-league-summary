# import streamlit, pandas and ipyvizzu
from ipyvizzu import Chart, Data, Config, Style, DisplayTarget


def create_chart(df, selected_round):
    
    running_chart = Chart(display = DisplayTarget.MANUAL, width="700px", height="600px")
    running_chart.scroll_into_view = False

    # create and add data to Chart
    data = Data()
    data.add_data_frame(df) 
    running_chart.animate(data)

    config = Config({
        "channels": {
            "y": { "set": ["team"] },
            "x": { "set": ["points"]},
            "color": { "set": ["team"] },
            "label": { "set": ["points"] }
        },
        "sort": 'byValue',
        "legend": None,
    })

    style= Style({
        "plot": {"marker": {"label": {"maxFractionDigits": "0"}}, #cutting off unnecessary digits when animating the labels
            "paddingLeft":"10em", #add padding on the left side of the plot so that long country names are visible
            "paddingTop":"1em", #add padding on the left side of the plot so that long country names are visible
            "xAxis": { "color" : "#3c1c5c", "title": {"color" : "#00000000"}}}, #hiding the axis title on the x-axis
        "title": { "color" : "#3c1c5c" },
        "paddingTop": "1em",
        "paddingBottom": "0em"
    })

    for round in range(1, selected_round + 1):
        running_chart.animate(Config({"title": f"Round {round }"}))
        running_chart.animate(
            Data.filter(f"parseInt(record.league_round) == {round}"), 
            config,style,
            # Animation options:
            duration = 0.5,
            delay = 0,        
            x = { "easing": "linear", "delay": 0 },
            y = { "delay": 0 },
            show = { "delay": 0 },
            hide = { "delay": 0 },
            title = { "duration": 1, "delay": 0 })

    return running_chart._repr_html_()
