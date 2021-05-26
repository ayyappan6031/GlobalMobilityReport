from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt
from download_source import SourceDownlaod


class GlobalMobilityReport:
    COUNTRY_REGION_CODE = 'country_region_code'
    COUNTRY_REGION = 'country_region'
    SUB_REGION_1 = 'sub_region_1'
    SUB_REGION_2 = 'sub_region_2'
    METRO_AREA = 'metro_area'
    ISO_3166_2_CODE = 'iso_3166_2_code'
    CENSUS_FIPS_CODE = 'census_fips_code'
    PLACE_ID = 'place_id'
    DATE = 'date'

    SOURCE_FILE_NAME = 'Global_Mobility_Report.csv'
    collisst = []

    fromdate = 0.0
    todate = 0.0

    LINE = 0
    BAR = 2

    def __init__(self):
        SourceDownlaod().downloadsourcefile()
        self.df = pd.read_csv(self.SOURCE_FILE_NAME, dtype='unicode')

    def datetoms(self, x):
        return datetime.strptime(x, "%Y-%m-%d").timestamp()

    def setChartType(self, charttype):
        self.chartType = charttype

    def getCountryCode(self):
        rgcode = pd.unique(self.df[self.COUNTRY_REGION_CODE])
        rgname = pd.unique(self.df[self.COUNTRY_REGION])
        for index, w in enumerate(rgcode):
            print(rgname[index], '--', rgcode[index])
    def getStatesList(self,country):
        stdf = self.df.loc[self.df[self.COUNTRY_REGION_CODE]==country]
        print(pd.unique(stdf[self.SUB_REGION_1]))

    def getCityList(self,country,state):
        stdf = self.df.loc[(self.df[self.COUNTRY_REGION_CODE]==country) & (self.df[self.SUB_REGION_1]==state)]
        print(pd.unique(stdf[self.SUB_REGION_2]))


    def displayChart(self, country, state, city, data_needed, startdate, enddate, chart_type):
        self.fromdate = self.datetoms(startdate)
        self.todate = self.datetoms(enddate)
        newdf = self.df.loc[(self.df[self.COUNTRY_REGION_CODE] == country) & (self.df[self.SUB_REGION_1] == state) & (
                self.df[self.SUB_REGION_2] == city)]
        newdf[self.DATE] = newdf[self.DATE].apply(lambda x: datetime.strptime(x, "%Y-%m-%d").timestamp())
        newdf = newdf.loc[(newdf[self.DATE] > self.fromdate) & (newdf[self.DATE] < self.todate)]
        newdf[self.DATE] = newdf[self.DATE].apply(lambda x: datetime.fromtimestamp(x))
        xAxisv = newdf.loc[:, self.DATE]
        yAxisv = newdf.loc[:, data_needed].values
        yAxisv = yAxisv.astype(float)
        self.showChart(xAxisv, yAxisv, data_needed, chart_type)


    def showChart(self, xaxix, yaxis, datas, chattype):
        plt.title(datas)
        plt.xlabel("Date")
        plt.ylabel(datas)
        if chattype == self.LINE:
            plt.bar(xaxix, yaxis)
        else:
            plt.bar(xaxix, yaxis)
        plt.show()
