import plotly_express as px

class CategoricalRatingFigure:
    def __init__(self, data, cat, rat):
        self.data = data
        self.cat = cat
        self.rat = rat
        self.colors = ['#DCEBF9', '#B3C8E8', '#8CA8D9', '#6493CC', '#406EAF']


    def create_count_figure(self):
        plotdf = self.data.groupby([self.cat, self.rat]).size().reset_index(name='count')
        plotdf[self.cat] = plotdf[self.cat].astype('str')
        plotdf[self.rat] = plotdf[self.rat].astype('str')

        rating_order = sorted(plotdf[self.rat].unique(), key=int)

        fig = px.bar(plotdf, x=self.cat, y='count',
                     color_discrete_sequence=self.colors,
                     color=self.rat, barmode='stack', text='count', category_orders={self.rat: rating_order},)

        fig.update_layout(
            barmode='stack',
            paper_bgcolor='rgb(248, 248, 255)',
            plot_bgcolor='rgb(248, 248, 255)'
        )

        fig.update_traces(textposition='auto', insidetextanchor='middle', textfont_size=10)
        for trace in fig.data:
            if trace.textangle is not None and any(angle > 45 and angle < 135 for angle in trace.textangle):
                trace.text = [None] * len(trace.text)

        return fig

    def create_percentage_figure(self):
        plotdf = self.data.groupby([self.cat, self.rat]).size().reset_index(name='count')
        plotdf[self.cat] = plotdf[self.cat].astype('str')
        plotdf[self.rat] = plotdf[self.rat].astype('str')

        # Calculate the total count for each category
        plotdf['total_count'] = plotdf.groupby(self.cat)['count'].transform('sum')

        # Calculate the percentage representation for each rating
        plotdf['percentage'] = (plotdf['count'] / plotdf['total_count']) * 100
        plotdf = plotdf.round(1)

        # Sort the unique rating values in ascending order
        rating_order = sorted(plotdf[self.rat].unique(), key=int)

        # Create the stacked bar chart with percentage labels
        fig = px.bar(
            plotdf,
            x=self.cat,
            y='percentage',
            color_discrete_sequence=self.colors,
            color=self.rat,
            category_orders={self.rat: rating_order},  # Set rating order
            barmode='stack',
            text='percentage',
            hover_data={'count': True, 'percentage': ':.2f%'}
        )

        # Update the layout
        fig.update_layout(
            barmode='stack',
            paper_bgcolor='rgb(248, 248, 255)',
            plot_bgcolor='rgb(248, 248, 255)'
        )

        # Conditionally hide text annotations if rotated by 90 degrees
        fig.update_traces(textposition='auto', insidetextanchor='middle',
                          textfont_size=10)

        fig.update_traces(texttemplate='%{text:.0f}%', textfont_color='white')
        for trace in fig.data:
            if trace.textangle is not None and any(angle > 45 and angle < 135 for angle in trace.textangle):
                trace.text = [None] * len(trace.text)

        # Show the figure
        return fig
