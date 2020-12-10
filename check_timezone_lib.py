import pytz
def check_timezone(country):
    for tzone in pytz.all_timezones:
        try:
            _, countries = tzone.split("/")
            if country in countries:
                country = tzone
                return(country)
        except:
            pass
    return(None)
