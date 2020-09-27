import json
import re
from datetime import datetime

import requests

from typing import List


from .interface import ResultInterface
from app.main import cache


class ResultService(object):
    """test"""
    @staticmethod
    def results() -> List[ResultInterface]:
        '''test'''
        results = cache.get('results')
        if not results:
            results = ResultService.get_all()
            cache.set('results', results)
        return results

    @staticmethod
    def today() -> ResultInterface or None:
        today_result = cache.get('today_result')
        results = ResultService.results()

        if not today_result:
            today_str = datetime.strptime(str(datetime.today().date()), '%Y-%m-%d').isoformat()
            for result in results:
                if 'tarih' in result and result['tarih'] == today_str:
                    cache.set('today_result', result)
                    return result
            return None

        return today_result

    @staticmethod
    def last() -> ResultInterface or None:
        last_result = cache.get('last_result')
        results = ResultService.results()
        if not last_result:
            sorted_results = sorted(results, key=lambda r: r['tarih'], reverse=True)
            if sorted_results:
                cache.set('last_result', sorted_results[0])
                return sorted_results[0]
            return None
        return last_result

    @staticmethod
    def get_all() -> List[ResultInterface]:
        URL = 'https://covid19.saglik.gov.tr/TR-66122/genel-koronavirus-tablosu.html'
        response = requests.get(URL)
        matches = re.findall(r"var geneldurumjson = ([^']*);", response.text)
        results = []
        if matches:
            matched = matches[0]
            results_raw = json.loads(matched)
            results = [ResultService.__model_binding(result) for result in results_raw]
        return [ResultInterface(**result) for result in results] if len(results) > 0 else list()


    @staticmethod
    def __model_binding(result_dict: dict):
        for key in result_dict.keys():
            if key == 'tarih':
                result_dict[key] = datetime.strptime(result_dict[key], '%d.%m.%Y').isoformat()
            elif key == 'hastalarda_zaturre_oran':
                value = result_dict[key].replace(',', '.')
                try:
                    result_dict[key] = float(value)
                except ValueError as _:
                    result_dict[key] = -1
            else:
                value = result_dict[key].replace('.', '')
                try:
                    result_dict[key] = int(value)
                except ValueError as _:
                    result_dict[key] = -1
        return result_dict

