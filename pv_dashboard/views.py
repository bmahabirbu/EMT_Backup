# import viewsets
from rest_pandas import PandasSimpleView
from .models import TimeSeries
import pandas as pd

class TimeSeriesView(PandasSimpleView):
    def get_data(self, request, *args, **kwargs):
        # Do functions here and return back the frame as an output
        df = TimeSeries.objects.to_dataframe()
        df.set_index('panel', inplace=True)
        print(df.head())
        eds1 = df.loc[['EDS-PV1']]
        eds1.set_index('Date', inplace=True)
        eds1 = eds1[['SI_Before','SI_After']].ffill()
        return eds1
