def add_years_to_date(years_to_add, original_date):
    result_date = original_date.replace(year=original_date.year + years_to_add)
    return result_date

def add_months_to_date(months_to_add, original_date):
    result_date = original_date.replace(month=original_date.month + months_to_add)
    return result_date