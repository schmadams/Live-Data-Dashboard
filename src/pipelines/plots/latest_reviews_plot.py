


class LatestReviews:
    def __init__(self, data, rat, gran, gran_filter):
        self.data = self.filter_data(data, rat, gran, gran_filter)


    def filter_data(self, data, rat, gran, gran_filter):
        data = data[[rat, gran]]
        data = data[data[gran] == gran_filter]
        a=1
        a=1