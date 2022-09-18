from typing import Dict, Tuple, List
import requests as rq
import json
from datetime import datetime

from utils import *
from period import Period
from subject import Subject

class Pupil:
    def __init__(self, username, password) -> None:
        self.session = rq.Session()
        self.session.headers['user-agent'] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36"

        login_url = 'https://api.ecoledirecte.com/v3/login.awp?v=4.17.10'
        login_payload = {
            "identifiant": username,
            "motdepasse": password
        }
        login_data:str = json_stringify(login_payload, name='data')
        login = self.session.post(login_url, login_data)
        json_response:dict = login.json()

        self.json_data = jdata = json_response['data']['accounts'][0]
        self.token:str = json_response['token']
        self.id:str = jdata['id']
        self.uid:str = jdata['uid']
        self.account_type:str = jdata['typeCompte']
        self.name:str = [jdata['prenom'], jdata['particule'], jdata['nom']]
        self.email:str = jdata['email']
        self.current_school_years:str = jdata['anneeScolaireCourante']
        self.school:str = jdata['nomEtablissement']

        jdata = jdata['profile']
        self.sex:str = jdata['sexe']

        self.profile_picture_url:str = 'https:' + jdata['photo']

    def get_periods(self) -> List[Period]:
        grades_url = f"https://api.ecoledirecte.com/v3/eleves/{self.id}/notes.awp?verbe=get&"
        payload:str = json_stringify({'token':self.token}, name='data')
        grades_request = self.session.post(grades_url, data=payload)
        data:dict = grades_request.json()['data']
        final_periodes = []
        for p in data['periodes']:
            p_id_:str = p['idPeriode']
            p_name:str = p['periode']
            p_is_annual:bool = p['annuel']
            p_dates:Tuple[datetime] = [str_to_date(i) for i in (p['dateDebut'], p['dateFin'])]
            p_is_finished:bool = p['cloture']
            if 'dateConseil' in p:
                p_council_date:datetime = str_to_datetime(concatenate_date_and_hour(p['dateConseil'], p['heureConseil']))
            
            m = p['ensembleMatieres']
            p_calcul_date:str = m.get('dateCalcul', None)
            p_averages = {
                'general' : m.get('moyenneGenerale', None),
                'class' : m.get('moyenneClasse', None),
                'min' : m.get('moyenneMin', None),
                'max' : m.get('moyenneMax', None)
            }
            p_main_teacher:str = m.get('nomPP', None)
            p_career_counselor:str = m.get('nomCE', None)

            d = m['disciplines']
            p_grades = {}
            p_subjects = {}
            for subj in d:
                if subj['groupeMatiere']:
                    continue

                subject = dict_to_subject(subj)
                p_subjects[subject.name] = subject
                p_grades[subject.name] = subject
            
            final_periodes.append(Period(p_id_, p_name, p_is_annual, p_dates, p_is_finished, p_averages, p_council_date, p_calcul_date, p_main_teacher, p_career_counselor, p_grades, p_subjects))
        
        return final_periodes
