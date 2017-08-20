import datetime

"""
  This function assumes the string is in the format
  %Y-%m-%d
  where %Y is the full year,
        %m is the month [01,12]
        %d is the date [01,31] depends on the month.
  And it returns the equivalent datetime.date object.
"""
def makeDate(timeString):
  year, month, date = map(int, timeString.split('-'))
  return datetime.date(year, month, date)

class HotelDeal:
  """
    Represents a hotel deal and evaluates the value for any booking.
    Initializes using a map with these keys:
    'hotel_name',
    'nightly_rate',
    'promo_txt',
    'deal_value',
    'deal_type',
    'start_date',
    'end_date'
  """
  def __init__(self, dealMap):
    self.hotelName = dealMap['hotel_name']
    self.nightlyRate = float(dealMap['nightly_rate'])
    self.promoTXT = dealMap['promo_txt']
    self.dealValue = abs(float(dealMap['deal_value']))
    self.dealType = dealMap['deal_type']
    self.startDate = makeDate(dealMap['start_date'])
    self.endDate = makeDate(dealMap['end_date'])

  """
    Returns the value of the deal if eligible
    else returns 0.
    Assumes that a booking is fully eligible if the start_date is between
    the deal's start date and end date.
  """
  def valueFromBooking(self, hotelName=None, bookTime=None, duration=None):
    # asserts required keyword arguments to describe a booking.
    errorString = 'valueFromBooking() missing required {} keyword argument'
    if hotelName is None:
      raise TypeError(errorString.format('hotelName'))
    if bookTime is None:
      raise TypeError(errorString.format('bookTime'))
    if duration is None:
      raise TypeError(errorString.format('duration'))

    # wrong hotel
    if hotelName != self.hotelName:
      return 0

    # checks eligibility for 3 days or more rebates
    if self.dealType == 'rebate_3plus' and duration < 3:
      return 0

    startBookTime = makeDate(bookTime)
    totalBeforeDeal = self.nightlyRate * duration

    if not (self.startDate <= startBookTime <= self.endDate):
      return 0

    return self.calculateValue(totalBeforeDeal)

  # returns the savings for the total booking cost.
  def calculateValue(self, totalBeforeDeal):
    if self.dealType == 'pct':
      return totalBeforeDeal * self.dealValue / 100
    return self.dealValue


# Parses a string for hotel deal.
def parse(dealString, headers=None):
  if headers == None:
    raise ValueError('Missing headers for the hotel deals.')
  dealMap = {}
  for idx, val in enumerate(dealString.strip().split(',')):
    key = headers[idx]
    dealMap[key] = val
  deal = HotelDeal(dealMap)
  return deal
