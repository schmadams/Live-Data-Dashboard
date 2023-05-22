import plotly_express as px

class CategoricalRatingFigure:
    def __init__(self, data, cat, rat):
        self.data = data
        self.cat = cat
        self.rat = rat
        self.colors = ['#DCEBF9', '#B3C8E8', '#8CA8D9', '#6493CC', '#406EAF']
        self.rating_order = sorted(self.data[self.rat].unique(), key=int)
        self.cat_order = [str(x) for x in sorted(self.data[self.cat].unique())]

    def category_sort_key(self, category):
        try:
            return int(category)
        except ValueError:
            return category

    def create_count_figure(self):
        plotdf = self.data.groupby([self.cat, self.rat]).size().reset_index(name='count')
        plotdf[self.cat] = plotdf[self.cat].astype('str')
        plotdf[self.rat] = plotdf[self.rat].astype('str')

        fig = px.bar(plotdf, x=self.cat, y='count',
                     color_discrete_sequence=self.colors,
                     color=self.rat, barmode='stack', text='count', category_orders={self.rat: self.rating_order,
                                                                                     self.cat: self.cat_order})

        fig.update_layout(
            barmode='stack',
            paper_bgcolor='rgb(248, 248, 255)',
            plot_bgcolor='rgb(248, 248, 255)'
        )

        fig.update_traces(textposition='auto', insidetextanchor='middle', textfont_size=10)
        fig.update_xaxes(categoryorder='category ascending')
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

        # Create the stacked bar chart with percentage labels
        fig = px.bar(
            plotdf,
            x=self.cat,
            y='percentage',
            color_discrete_sequence=self.colors,
            color=self.rat,
            category_orders={self.rat: self.rating_order, self.cat: self.cat_order},  # Set rating order
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
