import csv
import time
import datetime


class DataPoint():

    def __init__(self, id, datetime, siteid, offerid, category, merchant, countrycode, browserid, devid):
        self.id = id
        self.datetime = datetime
        self.siteid = siteid
        self.offerid = offerid
        self.category = category
        self.merchant = merchant
        self.countrycode = countrycode
        self.browserid = browserid
        self.devid = devid

    def prepro_datetime(self):
        self.datetime = time.mktime(datetime.datetime.strptime(
            self.datetime.strip(), "%Y-%m-%d %H:%M:%S").timetuple())

    def prepro_siteid(self):
        pass

    def prepro_offerid(self):
        pass

    def prepro_category(self):
        pass

    def prepro_merchant(self):
        pass

    def prepro_countrycode(self):
        pass

    def prepro_browserid(self):
        pass

    def prepro_devid(self):
        pass


class DataPointList():

    def __init__(self):
        self.datapointlist = datapointlist


def readdata(filename):
    with open(filename, 'rb') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        next(reader, None)
        for row in reader:
            datapoint = DataPoint(*row)
            datapoint.prepro_datetime()

if __name__ == "__main__":
    readdata("data/test.csv")
