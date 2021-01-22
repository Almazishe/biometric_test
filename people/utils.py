from django.utils.timezone import now


def get_year(year2):
    """
    Выводит из 2 циферного года 
    Если честно до сих пор не понимаю почему так в КЗ иин делают, по 2 последним цифрам
    """
    if int(f'{now().year}'[-2:]) > year2:
        return int(f'{now().year}'[:2] + year2)
    return int(f'{now().year - 1}'[:2] + year2)