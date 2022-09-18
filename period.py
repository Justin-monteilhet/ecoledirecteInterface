from datetime import datetime
from typing import Dict, Tuple
from subject import Subject

class Period:
    def __init__(self, id_:str, name:str, is_annual:bool, dates:Tuple[datetime], is_finished:bool, averages:dict, council_date:datetime=None, calcul_date:str=None, main_teacher:str=None, career_counselor:str=None, grades:Dict[str,Subject]=None) -> None:
        self.id, self.name, self.is_annual, self.dates, self.is_finished, self.averages, self.council_date, self.calcul_date, self.main_teacher, self.career_counselor, self.grades  = id_, name, is_annual, dates, is_finished, averages, council_date, calcul_date, main_teacher, career_counselor, grades 