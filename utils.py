from json import dumps
from datetime import datetime
from subject import Subject

__ED_DATETIME_PATTERN = '%Y-%m-%d/%H:%M'
__ED_DATE_PATTERN = '%Y-%m-%d'
__ED_HOUR_PATTERN = '%H:%M'

def json_stringify(data, name=None):
    name = data.__name__ if not name else name
    return str(name) + '=' + dumps(data)

def concatenate_date_and_hour(d, h):
    return d + '/'+ h

def str_to_datetime(s):
    return datetime.strptime(s, __ED_DATETIME_PATTERN)

def str_to_date(s):
    return datetime.strptime(s, __ED_DATE_PATTERN)

def dict_to_subject(s):
    s_id_:str = s['id']
    s_code:str = s['codeMatiere']
    s_name:str = s['discipline']
    s_averages = {
        'general':s.get("moyenne", None),
        'class':s.get("moyenneClasse", None),
        'min':s.get("moyenneMin", None),
        'max':s.get("moyenneMax", None)
    }
    s_coeff:int = int(s['coef'])
    s_teachers = [prof['nom'] for prof in s['professeurs']]
    return Subject(s_id_, s_code, s_name, s_averages, s_coeff, s_teachers)