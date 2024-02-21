# Plik models/database.py
import csv

# Ścieżka do pliku z danymi użytkowników
USERS_DATA_FILE = 'data/users.csv'

# Wczytanie danych użytkowników z pliku CSV
def load_users_data():
    users_data = []
    with open(USERS_DATA_FILE, 'r', encoding='utf-8') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            users_data.append(row)
    return users_data

# Porównanie odpowiedzi z innymi użytkownikami
def compare_answers(answers):
    # Wczytanie danych użytkowników
    users_data = load_users_data()
    
    # Porównanie odpowiedzi z każdym użytkownikiem
    matching_users = []
    for user_data in users_data:
        user_id = user_data['id']
        user_answers = {int(key): int(value) for key, value in user_data.items() if key != 'id'}
        match_score = calculate_match_score(answers, user_answers)
        matching_users.append({'id': user_id, 'match_score': match_score})
    
    # Znalezienie użytkownika o najwyższym wyniku dopasowania
    best_match = max(matching_users, key=lambda x: x['match_score'])
    
    # Zwrócenie informacji o użytkowniku z najlepszym dopasowaniem
    best_match_id = best_match['id']
    return f"Your psychological profile closely matches user {best_match_id}."

# Obliczenie wyniku dopasowania między odpowiedziami
def calculate_match_score(answers1, answers2):
    match_score = 0
    for key in answers1.keys():
        if key in answers2:
            if answers1[key] == answers2[key]:
                match_score += 1
    return match_score

