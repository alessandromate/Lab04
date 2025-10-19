from crociera import Crociera
import csv

def menu():
    print(f'\n--- MENU CROCIERA ---')
    print("1. Modifica nome della crociera")
    print("2. Carica dati da file")
    print("3. Assegna cabina a passeggero")
    print("4. Visualizza cabine ordinate per prezzo")
    print("5. Visualizza elenco passeggeri")
    print("6. Esci")

    return input("Scegli un'opzione >> ")

def main():
    crociera = Crociera("MSC Futura")

    while True:
        scelta = menu()

        if scelta == "1":
            nuovo_nome = input("Inserisci il nuovo nome della crociera: ")
            nuova_croc = Crociera(nuovo_nome)
            print(f"La crociera {nuova_croc.nome} è operativa.")

        elif scelta == "2":
            file_path = "dati_crociera.csv"
            try:
                crociera.carica_file_dati(file_path)
                print("Dati caricati correttamente.")
                #print(f"{crociera}")
            except FileNotFoundError:
                print("File non trovato.")

        elif scelta == "3":
            codice_cabina = input("Codice cabina: ")
            codice_passeggero = input("Codice passeggero: ")
            try:
                crociera.assegna_passeggero_a_cabina(codice_cabina, codice_passeggero)
                print("Cabina assegnata con successo.")
                #print(f"{crociera}")
            except Exception as e:
                print(f"Errore: {e}")

        elif scelta == "4":
            cabine_ordinate = crociera.cabine_ordinate_per_prezzo()
            print("\n--- Cabine ordinate per prezzo ---")
            for c in cabine_ordinate:
                print(f'{c.codice_cabina}')

        elif scelta == "5":
            print("\n--- Elenco passeggeri ---")
            passeg = crociera.elenca_passeggeri()
            for p in passeg:
                print(f'{p.codice_passeggero} {p.nome} {p.cognome} {p.cab_assegnata}')

        elif scelta == "6":
            print("Uscita dal programma.")
            break

        else:
            print("Scelta non valida.")

if __name__ == "__main__":
    main()