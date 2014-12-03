import datetime

# TODO: Unit/regression testing

def date_range(start, stop, step):
    current = start
    if step.days < 0:
        while current >= stop:
            yield current
            current += step
    else:
        while current < stop:
            yield current
            current += step

def year_of_season(season_str, first=False):
    try:
        top, bot = season_str.split('-')
    except ValueError:
        return datetime.datetime.strptime(season_str, '%Y')
    else:
        if first:
            return datetime.datetime.strptime(top, '%Y')
        else:
            return datetime.datetime.strptime(bot, '%y')

def season_range(start, stop, step=1):
    year = datetime.timedelta(days=365)
    step_delta = step * year
    
    if isinstance(start, datetime.datetime):
        start_date = start
    else: 
        start_date = year_of_season(start)

    if isinstance(stop, datetime.datetime):
        stop_date = stop
    else: 
        stop_date = year_of_season(stop)
    
    return ('{0}-{1}'.format((current-year).strftime('%Y'), current.strftime('%y')) \
            for current in time_range(start_date, stop_date, step_delta))