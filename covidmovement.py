from global_mobility_report import GlobalMobilityReport
from availabledata import AvailableData
gv = GlobalMobilityReport()
# gv.getCountryCode()
# country = input('Enter country code from above details :')
# gv.getStatesList(country)
# state = input('Enter State name from above list :')
# gv.getCityList(country,state)
# city = input('Enter City name from above list :')

country = 'IN'
state='Tamil Nadu'
city='Kanyakumari'
gv.displayChart(country, state, city, AvailableData.TRANSIT_STATIONS_PERCENT_CHANGE_FROM_BASELINE,
                                    '2021-04-01', '2021-04-30', GlobalMobilityReport.LINE)
