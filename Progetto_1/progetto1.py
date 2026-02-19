# ==========================================
# PARTE 1 - Variabili e tipi di dati
# ==========================================
print("--- PARTE 1: Variabili ---")

titolo_esempio = "Il Signore degli Anelli"  # Stringa (str)
copie_disponibili = 5                       # Intero (int)
prezzo_medio = 19.99                        # Decimale (float)
disponibile = True                          # Booleano (bool)

print(f"Titolo: {titolo_esempio} (Tipo: {type(titolo_esempio).__name__})")
print(f"Copie: {copie_disponibili} (Tipo: {type(copie_disponibili).__name__})")
print(f"Prezzo: €{prezzo_medio} (Tipo: {type(prezzo_medio).__name__})")
print(f"Stato disponibilità: {disponibile} (Tipo: {type(disponibile).__name__})\n")


# ==========================================
# PARTE 2 - Strutture dati
# ==========================================
print("--- PARTE 2: Strutture Dati ---")

# Lista con 5 titoli
lista_libri = [
    "Il Signore degli Anelli", 
    "1984", 
    "Dune", 
    "Orgoglio e Pregiudizio", 
    "Fondazione"
]

# Dizionario (Mappa Titolo -> Copie)
dizionario_copie = {
    "Il Signore degli Anelli": 5,
    "1984": 3,
    "Dune": 1,
    "Orgoglio e Pregiudizio": 4,
    "Fondazione": 0
}

# Insieme (Set) di utenti (non ammette duplicati)
utenti_registrati = {"Mario Rossi", "Giulia Bianchi", "Luca Verdi"}

print("Lista libri:", lista_libri)
print("Dizionario copie:", dizionario_copie)
print("Utenti registrati:", utenti_registrati)
print("\n")


# ==========================================
# PARTE 3 - Classi e OOP
# ==========================================

class Libro:
    def __init__(self, titolo, autore, anno, copie_disponibili):
        self.titolo = titolo
        self.autore = autore
        self.anno = anno
        self.copie_disponibili = copie_disponibili

    def info(self):
        return f"'{self.titolo}' di {self.autore} ({self.anno}) - Copie: {self.copie_disponibili}"

class Utente:
    def __init__(self, nome, eta, id_utente):
        self.nome = nome
        self.eta = eta
        self.id_utente = id_utente

    def scheda(self):
        print(f"Utente [{self.id_utente}]: {self.nome}, {self.eta} anni")

class Prestito:
    def __init__(self, utente, libro, giorni):
        self.utente = utente
        self.libro = libro
        self.giorni = giorni

    def dettagli(self):
        print(f"PRESTITO -> Libro: '{self.libro.titolo}' | A: {self.utente.nome} | Durata: {self.giorni} giorni")


# ==========================================
# PARTE 4 - Funzionalità e Simulazione
# ==========================================

def presta_libro(utente, libro, giorni):
    """
    Gestisce la logica del prestito verificando la disponibilità.
    Restituisce un oggetto Prestito in caso di successo, altrimenti None.
    """
    if libro.copie_disponibili >= 1:
        libro.copie_disponibili -= 1  # Riduciamo le copie
        nuovo_prestito = Prestito(utente, libro, giorni)
        return nuovo_prestito
    else:
        print(f"[ERRORE] Impossibile prestare '{libro.titolo}'. Copie esaurite!")
        return None

print("--- PARTE 4: Simulazione Prestiti ---")

# 1. Creiamo gli oggetti Libro (il nostro database di oggetti)
l1 = Libro("1984", "George Orwell", 1949, 3)
l2 = Libro("Dune", "Frank Herbert", 1965, 1)
l3 = Libro("Fondazione", "Isaac Asimov", 1951, 0) # Zero copie in partenza
catalogo_oggetti = [l1, l2, l3]

# 2. Creiamo gli oggetti Utente
u1 = Utente("Mario Rossi", 30, "U001")
u2 = Utente("Giulia Bianchi", 25, "U002")

# 3. Simuliamo 3+ prestiti
prestiti_effettuati = []

# Tentativo 1: Mario prende "1984" (Successo, copie 3 -> 2)
p1 = presta_libro(u1, l1, 14)
if p1: prestiti_effettuati.append(p1)

# Tentativo 2: Giulia prende "Dune" (Successo, copie 1 -> 0)
p2 = presta_libro(u2, l2, 7)
if p2: prestiti_effettuati.append(p2)

# Tentativo 3: Mario prova a prendere "Fondazione" (Errore, 0 copie iniziali)
p3 = presta_libro(u1, l3, 10)
if p3: prestiti_effettuati.append(p3)

# Tentativo 4: Mario prova a prendere "Dune" (Errore, copie azzerate dal prestito di Giulia)
p4 = presta_libro(u1, l2, 5)
if p4: prestiti_effettuati.append(p4)

print("\n--- RISULTATI FINALI ---")

# Stampa dettagli di ogni prestito effettuato
print("Dettagli Prestiti Approvati:")
for prestito in prestiti_effettuati:
    prestito.dettagli()

print("\nElenco aggiornato delle copie disponibili nel catalogo:")
for libro in catalogo_oggetti:
    print(libro.info())