import plotly_express as px
import plotly.graph_objects as go

class CatScatter:
    def __init__(self, data, cat, y, x):
        self.data = data[[cat, y, x]]
        self.cat = cat
        self.x = x
        self.y = y
        print(cat, x, y)

    def create_fig(self):
        self.data[self.cat] = self.data[self.cat].astype('str')
        self.data = self.data[self.data[self.y] != 0]
        self.data = self.data[self.data[self.x] != 0]
        df = self.data.copy()
        df = df.groupby([self.cat]).agg(col1=(self.x, 'mean'), col2=(self.y, 'mean'), data_points=(self.y, 'size')).reset_index()
        df = df.round({'col1': 2, 'col2': 2})
        df = df.rename(columns={'col1': f'average {self.y}', 'col2': f'average {self.x}'})
        corr_score = round(df[f'average {self.y}'].corr(df[f'average {self.x}']), 2)
        fig = px.scatter(df, x=f'average {self.x}', y=f'average {self.y}', color=self.cat, trendline='ols', trendline_scope='overall')
        fig.update_layout(
            title=go.layout.Title(
                text=f"Scatter plot of {self.x} vs {self.y} across {self.cat} <br><sup> Correlation score = {corr_score} <sup>",
                xref="paper",
                x=0
            ))
        return fig, df