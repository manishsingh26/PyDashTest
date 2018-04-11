
import plotly.offline as py
import plotly.graph_objs as go


def level_data(df, filter_name):
    df_level1 = df[df["level"] == "Level1"]
    df_level2 = df[df["level"] == "Level2"]
    df_level3 = df[df["level"] == "Level3"]

    # level1_annotations = [dict(x=df_level1["count"].tolist(),
    #                            y=df_level1["endyear"].tolist(),
    #                            text=df_level1[filter_name].tolist(),
    #                            xanchor='auto',
    #                            yanchor='bottom',
    #                            showarrow=False,) for x, y in zip(df_level1["count"].tolist(), df_level1["endyear"].tolist())]
    #
    # level2_annotations = [dict(x=df_level2["count"].tolist(),
    #                            y=df_level2["endyear"].tolist(),
    #                            text=df_level2[filter_name].tolist(),
    #                            xanchor='auto',
    #                            yanchor='bottom',
    #                            showarrow=False,) for x, y in zip(df_level2["count"].tolist(), df_level2["endyear"].tolist())]
    #
    # level3_annotations = [dict(x=df_level3["count"].tolist(),
    #                            y=df_level3["endyear"].tolist(),
    #                            text=df_level3[filter_name].tolist(),
    #                            xanchor='auto',
    #                            yanchor='bottom',
    #                            showarrow=False,) for x, y in zip(df_level3["count"].tolist(), df_level3["endyear"].tolist())]
    # annotations = level1_annotations + level2_annotations + level3_annotations

    level1_trace = go.Bar(
        x=df_level1["count"].tolist(),
        y=df_level1["endyear"].tolist(),
        name=df_level1[filter_name].tolist(),
        orientation='h',
        marker=dict(
            color='rgb(252,141,89)',
            line=dict(
                color='rgb(252,141,89)',
                width=3)
        )
    )

    level2_trace = go.Bar(
        x=df_level2["count"].tolist(),
        y=df_level2["endyear"].tolist(),
        name=df_level2[filter_name].tolist(),
        orientation='h',
        marker=dict(
            color='rgb(255,255,191)',
            line=dict(
                color='rgb(255,255,191)',
                width=3)
        )
    )

    level3_trace = go.Bar(
        x=df_level3["count"].tolist(),
        y=df_level3["endyear"].tolist(),
        name=df_level3[filter_name].tolist(),
        orientation='h',
        marker=dict(
            color='rgb(145,191,219)',
            line=dict(
                color='rgb(145,191,219)',
                width=3)
        )
    )

    data = [level1_trace, level2_trace, level3_trace]
    layout = go.Layout(barmode='stack')

    return {"data": data,
            "layout": layout}
