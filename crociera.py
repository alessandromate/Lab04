class Cabina:
    def __init__(self, codice_cabina, num_letti, num_ponte, prezzo):
        self.codice_cabina = codice_cabina
        self.num_letti = num_letti
        self.num_ponte = num_ponte
        self.prezzo = prezzo
        self.assegnata = False
    def __str__(self):
        return f'{self.codice_cabina} {self.assegnata}'
class Cabina_animale(Cabina):
    def __init__(self, codice_cabina, num_letti, num_ponte, prezzo, max_animali): #estensione classe cabina (primo branch)
        super().__init__(codice_cabina, num_letti, num_ponte, prezzo)               #cabine con animali ammessi
        self.max_animali = max_animali
    def __str__(self):
        return f'{self.codice_cabina}{self.assegnata}'
class Cabina_deluxe(Cabina):
    def __init__(self, codice_cabina, num_letti, num_ponte, prezzo, tipologia):
        super().__init__(codice_cabina, num_letti, num_ponte, prezzo)  # cabine con animali ammessi
        self.tipologia = tipologia
    def __str__(self):
        return f'{self.codice_cabina}{self.assegnata}'
class Passeggero:
    def __init__(self, codice_passeggero, nome, cognome):
        self.codice_passeggero = codice_passeggero
        self.nome = nome
        self.cognome = cognome
        self.assegnato = False
        self.cab_assegnata = ''
    def __str__(self):
        return f'Il passeggero: {self.codice_passeggero} {self.nome} {self.cognome} sta/non sta nella cabina: {self.cab_assegnata}'
class Crociera:
    def __init__(self, nome):
        self.nome = nome
        self.passeggeri = []
        self.cabine= []             #appendo ogni tipologia di cabina                       |
    def __str__(self):           #printo con metodo str per ogni elemento di ciascuna lista V
        return f'{self.nome} {[str(p) for p in self.passeggeri ]}'

    def carica_file_dati(self, file_path):
        try:
            with open(file_path, 'r') as file:  # apertura file
                for row in file:
                    line = row.strip().split(',')
                    if line[1].isnumeric(): #se il primo campo è intero allora: CABINA
                        codice_cabina = line[0]
                        num_letti = int(line[1])
                        num_ponte = line[2]
                        prezzo = line[3]
                        if len(line)<=4:
                            cabina = Cabina(codice_cabina, num_letti, num_ponte, prezzo)
                            self.cabine.append(cabina)
                        elif line[4].isnumeric():              #se ultimo parametro è intero allora chiamo classe cab animale
                            max_animali = int(line[4])
                            cabina = Cabina_animale(codice_cabina, num_letti, num_ponte, prezzo,max_animali)
                            self.cabine.append(cabina)
                        elif line[4].isalpha():              #se ultimo parametro è stringa allora chiamo classe cab deluxe
                            tipologia = str(line[4])
                            cabina = Cabina_deluxe(codice_cabina, num_letti, num_ponte, prezzo, tipologia)
                            self.cabine.append(cabina)
                    else:           #se il primo campo è stringa allora:PASSEGGERO
                        codice_passeggero = line[0]
                        nome = line[1]
                        cognome = line[2]
                        passeggero = Passeggero(codice_passeggero, nome, cognome)
                        self.passeggeri.append(passeggero)
        except FileNotFoundError:
            print("File non esistente.")
#cab e pass esistono, cab disp, pass no altre cab
    def assegna_passeggero_a_cabina(self, codice_cabina, codice_passeggero):
        for c in self.cabine:
            if c.codice_cabina == codice_cabina:            #esiste nel file (cabina)
                if c.assegnata == False:                    #non ha assegnazioni (cabina)
                    for p in self.passeggeri:
                        if p.codice_passeggero == codice_passeggero:   #esiste nel file (pass)
                            if p.assegnato ==False:  #non ha assegnazioni (pass), allora inizio l assegnazione
                                c.assegnata = True
                                p.assegnato = True
                                p.cab_assegnata = c.codice_cabina

    def elenca_passeggeri(self):
        passeg = sorted(self.passeggeri, key=lambda x: x.codice_passeggero)
        return passeg

    def cabine_ordinate_per_prezzo(self):
        cabine_ordinate = sorted(self.cabine, key=lambda x: x.prezzo)
        return cabine_ordinate

