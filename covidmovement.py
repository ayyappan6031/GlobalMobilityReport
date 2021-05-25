from global_mobility_report import GlobalMobilityReport
from availabledata import AvailableData

GlobalMobilityReport().displayChart("IN", "Tamil Nadu", 'Chennai', AvailableData.PARKS_PERCENT_CHANGE_FROM_BASELINE,
                                    '2021-04-01', '2021-04-30', GlobalMobilityReport.LINE)
