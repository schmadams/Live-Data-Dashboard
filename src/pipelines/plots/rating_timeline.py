import plotly_express as px


class RatingTimeline:
    def __init__(self, data, fields):
        self.data = data
        if not isinstance(fields, list):
            fields = [fields]
        self.fields = fields

    def create_fig(self):
        all_cols = ['Pass_Date'] + self.fields
        plot_df = self.data[all_cols]
        plot_df = plot_df.groupby(['Pass_Date']).mean().reset_index()
        fig = px.line(plot_df, x='Pass_Date', y=self.fields)
        return fig
