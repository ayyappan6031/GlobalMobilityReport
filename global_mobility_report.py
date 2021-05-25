from datetime import datetime
import pandas as pd
from availabledata import AvailableData
import matplotlib.pyplot as plt


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

    chartType= 'line'

    LINE = 0
    BAR = 2

    def datetoms(self,x):
        return datetime.strptime(x, "%Y-%m-%d").timestamp()

    def setChartType(self,charttype):
        self.chartType = charttype

    def displayChart(self, country, state, city, data_needed, startdate, enddate, chart_type):
        self.collisst.append(self.COUNTRY_REGION)
        self.collisst.append(self.SUB_REGION_1)
        self.collisst.append(self.SUB_REGION_2)
        self.collisst.append(self.DATE)
        self.collisst.append(data_needed)
        self.fromdate = self.datetoms(startdate)
        self.todate = self.datetoms(enddate)
        df = pd.read_csv(self.SOURCE_FILE_NAME, usecols=self.collisst, dtype='unicode')
        newdf = df.loc[(df[self.COUNTRY_REGION] == country) & (df[self.SUB_REGION_1]== state)& (df[self.SUB_REGION_2]==city)]
        newdf[self.DATE] = newdf[self.DATE].apply(lambda x: datetime.strptime(x,"%Y-%m-%d").timestamp())
        newdf = newdf.loc[(newdf[self.DATE]>self.fromdate) & (newdf[self.DATE]<self.todate)]
        newdf[self.DATE] = newdf[self.DATE].apply(lambda x: datetime.fromtimestamp(x))
        xAxisv = newdf.loc[:,self.DATE]
        yAxisv = newdf.loc[:,data_needed].values
        yAxisv = yAxisv.astype(float)
        self.showChart(xAxisv,yAxisv,chart_type)

    def showChart(self,xaxix,yaxis,chattype):
        plt.title("work place movement data")
        plt.xlabel("Date")
        plt.ylabel("work place movement")
        if(chattype==self.LINE):
            plt.bar(xaxix,yaxis)
        else:
            plt.bar(xaxix,yaxis)
        plt.show()








