from datetime import datetime
from tda.client import Client
from pprint import pprint
import pandas as pd


def Debug(*args):
    for x in args:
        try:
            pprint(vars(x))
        except:
            pprint(x)


class Resolution:
    Minute = {"FrequencyType": Client.PriceHistory.FrequencyType.MINUTE,
              "Frequency": Client.PriceHistory.Frequency.EVERY_MINUTE,
              "PeriodType": Client.PriceHistory.PeriodType.DAY}

    Day = {"FrequencyType": Client.PriceHistory.FrequencyType.DAILY,
           "Frequency": Client.PriceHistory.Frequency.DAILY,
           "PeriodType": Client.PriceHistory.PeriodType.MONTH}

    HalfHour = {"FrequencyType": Client.PriceHistory.FrequencyType.MINUTE,
                "Frequency": Client.PriceHistory.Frequency.EVERY_THIRTY_MINUTES,
                "PeriodType": Client.PriceHistory.PeriodType.DAY}


class BacktestSettings:

    def __init__(self, Portfolio):
        self.CashAmount = 10000
        self.status = 0
        self.EquityList = []
        self.startDate = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
        self.endDate = None
        self.Portfolio = Portfolio
        self.Securities = {}

    def SetStartDate(self, month, day, year):
        self.startDate = datetime(year=year, month=month, day=day)

    def SetEndDate(self, month, day, year):
        self.endDate = datetime(year=year, month=month, day=day)

    def AddEquity(self, symbol, resolution):
        self.EquityList.append({"Symbol": symbol, "Resolution": resolution})
        tempdf = pd.DataFrame(columns=["Symbol", "Current Price", "Volume"])
        tempdf = tempdf.append({"Symbol": symbol,
                                "Current Price": 0,
                                "Volume": 0}, ignore_index=True)
        tempdf.set_index("Symbol", inplace=True)
        # print(tempdf)
        self.Portfolio.EquityInvested = self.Portfolio.EquityInvested.append(tempdf)

    def SetCashAmount(self, amount):
        self.CashAmount = amount
        self.Portfolio.CashAmount = amount
        self.Portfolio.PortfolioValue = amount
