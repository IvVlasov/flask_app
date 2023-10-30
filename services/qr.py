import qrcode
from io import BytesIO
import base64


def get_qr_code_data(params):
    ls_fio = params['fio'].split(' ')
    summ = ('%.2f' % float(str(params['summ']).replace(',', '.'))).replace('.', '')
    code = 'ST00011|Name={name}|PersonalAcc={rs}|BankName={bank}|BIC={bic}|CorrespAcc={ks}|PayeeINN={inn}|KPP={kpp}\
|PersAcc={ls}|PayerAddress={address}|LastName={last_name}|FirstName={first_name}|MiddleName={middle_name}|Sum={summ}\
|Purpose={purpose}'
    code = code.format(name=params['name'],
                       rs=params['rs'],
                       bank=params['bank'],
                       bic=params['bic'],
                       ks=params['ks'],
                       inn=params['inn'],
                       kpp=params['kpp'],
                       ls=params['ls'],
                       address=params['addres'],
                       last_name=ls_fio[0],
                       first_name=ls_fio[1],
                       middle_name=ls_fio[2],
                       summ=summ,
                       purpose=params['purpose'])
    return code


def generate_qr(params):
    qr = qrcode.QRCode(
        box_size=20,
        border=1,
    )
    code_data = get_qr_code_data(params).replace('\n', '')
    qr.add_data(code_data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color='white')
    buffered = BytesIO()
    img.save(buffered, format="PNG")
    img_str = base64.b64encode(buffered.getvalue())
    return {'img': img_str.decode("utf-8"), 'code_data': code_data}
