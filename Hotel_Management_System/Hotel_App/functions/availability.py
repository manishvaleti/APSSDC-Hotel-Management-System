import datetime
from datetime import date
import arrow
from Hotel_App.models import Bookings

def check_availability(rid,sdate,edate):
    avail_list=[]
    booking_list = Bookings.objects.filter(rid_id=rid)
    for i in booking_list:
        if i.sdate > edate or i.edate < sdate:
            avail_list.append(True)
        else:
            avail_list.append(False)
    return all(avail_list)


def no_of_days(ci_date,co_date):
    b=arrow.get(co_date)
    a=arrow.get(ci_date)
    x=(b-a)
    return(x.days)