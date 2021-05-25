import pandas as pd
import urllib.request
import matplotlib.pyplot as plt
from datetime import datetime
from global_mobility_report import GlobalMobilityReport
from availabledata import AvailableData
# dt = datetime.strptime("25-04-1990","%d-%m-%Y")
#
# def datetoms(x):
#     return datetime.strptime(x,"%Y-%m-%d").timestamp()
#
# print(dt.timestamp())
# pd.set_option("display.max.columns", None)
#
# collisst =  ['country_region_code','sub_region_1','sub_region_2','date','workplaces_percent_change_from_baseline']
# fromdate = datetoms('2021-04-01')
# todate = datetoms('2021-05-15')
# df = pd.read_csv('Global_Mobility_Report.csv',usecols = collisst,dtype='unicode')
# newdf = df.loc[(df['country_region_code'] == 'IN') & (df['sub_region_1']=='Tamil Nadu')& (df['sub_region_2']=='Chennai')]
# # newdf.to_csv("parsed.csv")
# newdf['date'] = newdf['date'].apply(lambda x: datetime.strptime(x,"%Y-%m-%d").timestamp())
# newdf = newdf.loc[(newdf['date']>fromdate) & (newdf['date']<todate)]
# newdf['date'] = newdf['date'].apply(lambda x: datetime.fromtimestamp(x))
# newdf.to_csv('final.csv')
# xAxisv = newdf.loc[:,'date']
# yAxisv = newdf.loc[:,'workplaces_percent_change_from_baseline'].values
# yAxisv = yAxisv.astype(float)
# plt.title("work place movement data")
# plt.xlabel("Date")
# plt.ylabel("work place movement")
# plt.bar(xAxisv,yAxisv)
# plt.show()
GlobalMobilityReport().displayChart("IN","Tamil Nadu",'Chennai',AvailableData.RETAIL_AND_RECREATION_PERCENT_CHANGE_FROM_BASELINE,'2021-04-01','2021-04-30',GlobalMobilityReport.LINE)
