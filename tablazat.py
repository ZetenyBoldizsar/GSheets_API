import gspread


def ekezetmentes(vezeteknev, keresztnev):
    vezeteknev = vezeteknev.lower()
    keresztnev = keresztnev.lower()
    if 'á' in vezeteknev or 'á' in keresztnev:
        vezeteknev = vezeteknev.replace('á', 'a')
        keresztnev = keresztnev.replace('á', 'a')
    if 'é' in vezeteknev or 'é' in keresztnev:
        vezeteknev = vezeteknev.replace('é', 'e')
        keresztnev = keresztnev.replace('é', 'e')
    if 'í' in vezeteknev or 'í' in keresztnev:
        vezeteknev = vezeteknev.replace('í', 'i')
        keresztnev = keresztnev.replace('í', 'i')
    if 'ó' in vezeteknev or 'ó' in keresztnev:
        vezeteknev = vezeteknev.replace('ó', 'o')
        keresztnev = keresztnev.replace('ó', 'o')
    if 'ő' in vezeteknev or 'ő' in keresztnev:
        vezeteknev = vezeteknev.replace('ő', 'ö')
        keresztnev = keresztnev.replace('ő', 'ö')
    if 'ú' in vezeteknev or 'ú' in keresztnev:
        vezeteknev = vezeteknev.replace('ú', 'u')
        keresztnev = keresztnev.replace('ú', 'u')
    if 'ű' in vezeteknev or 'ű' in keresztnev:
        vezeteknev = vezeteknev.replace('ű', 'ü')
        keresztnev = keresztnev.replace('ű', 'ü')
    return vezeteknev, keresztnev


def main():
    gc = gspread.service_account(filename='creds.json')
    sheet1 = gc.open('diakok').worksheet('Munkalap1')
    sheet1.update_acell('C1', 'e-mail cím')
    for x in range(2, 8):
        vezeteknev = sheet1.acell(f'A{x}').value
        keresztnev = sheet1.acell(f'B{x}').value
        vezeteknev, keresztnev = ekezetmentes(vezeteknev, keresztnev)
        sheet1.update_acell(f'C{x}', f'{vezeteknev}.{keresztnev}@x_mail.com')


main()
