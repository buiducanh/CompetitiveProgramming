import argparse
import HotelDeals

# defines program's arguments.
parser = argparse.ArgumentParser(description='Find the best hotel deal for your trip.')
parser.add_argument('inputDeals', type=argparse.FileType('r'))
parser.add_argument('hotelName')
parser.add_argument('bookDate')
parser.add_argument('duration', type=int)

# parses command line arguments.
args = parser.parse_args()

inputDeals = args.inputDeals

hotelName = args.hotelName

bookTime = args.bookDate

duration = args.duration
if duration <= 0:
    raise ValueError('Duration can\'t be less than or equal to zero.')

promo = 'no deal available'
maxValue = 0

for idx, line in enumerate(inputDeals):
    if idx == 0:
        headers = line.strip().split(',')
        continue
    deal = HotelDeals.parse(line, headers=headers)

    dealValue = deal.valueFromBooking(hotelName=hotelName,
                                      bookTime=bookTime, duration=duration)

    if dealValue and dealValue > maxValue:
        promo = deal.promoTXT
        maxValue = dealValue

print(promo)
