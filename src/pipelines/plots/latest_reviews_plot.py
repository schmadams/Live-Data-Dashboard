


class LatestReviews:
    def __init__(self, data, rat, gran, gran_filter):
        self.data = self.filter_data(data, rat, gran, gran_filter)
        self.cols = [rat] + gran


    def filter_data(self, data, rat, gran, gran_filter):
        data = data[[self.cols]]
        for filter in gran_filter:
            temp_gran, temp_filter = filter.split('-')[0], filter.split('-')[1]
        data = data[data[gran] == gran_filter]
        a=1
        a=1