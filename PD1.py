class Darbinieks:
    def __init__(self, vards, uzvards, vecums):
        self.vards = vards
        self.uzvards = uzvards
        self.vecums = vecums

    def iegut_vardu(self):
        return self.vards

    def iegut_uzvardu(self):
        return self.uzvards

    def iegut_vecumu(self):
        return int(self.vecums)


class Admin(Darbinieks):
    def __init__(self, vards, uzvards, vecums):
        Darbinieks.__init__(self, vards, uzvards, vecums)

    def __str__(self):
        print('Administrators: ' + self.vards + ' ' + self.uzvards)


class Viesis(Darbinieks):
    def __init__(self, vards, uzvards, vecums):
        Darbinieks.__init__(self, vards, uzvards, vecums)

    def __str__(self):
        print('Viesis: ' + self.vards + ' ' + self.uzvards)


if __name__ == '__main__':

    # 1.
    with open('admin.txt', 'r', encoding="utf-8") as admin, open('viesis.txt', 'r', encoding="utf-8") as viesis:
        lines = admin.read() + '\n' + viesis.read()
        print(lines)

    # 2
    darbinieki = []
    for line in lines.splitlines():
        param = line.split()
        if param[2] == 'admin':
            darbinieki.append(Admin(param[0], param[1], param[3]))
        if param[2] == 'viesis':
            darbinieki.append(Viesis(param[0], param[1], param[3]))

    admin_kop_skaits = 0
    admin_kop_vecums = 0
    admin_jaunakais = 1_000_000
    admin_vecakais = 0
    for darbinieks in darbinieki:
        if isinstance(darbinieks, Admin):
            a_vecums = darbinieks.iegut_vecumu()
            admin_kop_skaits += 1
            admin_kop_vecums += a_vecums
            if admin_jaunakais > a_vecums:
                admin_jaunakais = a_vecums
            if admin_vecakais < a_vecums:
                admin_vecakais = a_vecums
    if admin_kop_skaits != 0:
        print('Vidējajs administratora vecums = ', admin_kop_vecums / admin_kop_skaits)
    if admin_vecakais != 0:
        print('Visvecākā administratora vecums = ', admin_vecakais)
    if admin_jaunakais != 1_000_000:
        print('Visjaunākā administratora vecums = ', admin_jaunakais)

    # 3.
    admin_skaits = 0
    viesu_skaits = 0
    for darbinieks in darbinieki:
        if isinstance(darbinieks, Admin):
            admin_skaits += 1
        if isinstance(darbinieks, Viesis):
            viesu_skaits += 1
    print('Administratoru skaits = ', admin_skaits)
    print('Viesu skaits = ', viesu_skaits)
