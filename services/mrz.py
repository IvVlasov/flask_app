from mrz.generator.td1 import TD1CodeGenerator
from datetime import datetime


def _date_format(date):
    _date = datetime.strptime(date, '%Y-%m-%d')
    return _date.strftime('%y%m%d')


def generate_mrz_de_id(params):
    mrz = str(TD1CodeGenerator("ID",
                               "Germany",
                               params['pass_num'],
                               _date_format(params['date_b']),
                               "X",
                               _date_format(params['date_exp']),
                               "Germany",
                               params['surname'],
                               params['name'].split(' ')[0])).split('\n')
    if len(params['name'].split(' ')) > 1:
        mrz_line_3 = (params['surname'].replace(' ', '<').replace('-', '<').upper() + '<<' + params['name'].replace(' ', '<').upper() + ('<' * 30))[:30]
    else:
        mrz_line_3 = mrz[2]
    return mrz[0] + '\n' + mrz[1] + '\n' + mrz_line_3
