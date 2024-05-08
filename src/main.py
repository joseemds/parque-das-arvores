from animal import Animal
from health_historic import HeathRecord
from avl_tree import AVLTree
import json

def display_menu():
    print("""
          Selecione uma opção:
          a) Adicionar novo animal
          b) Remover animal por id
          c) Consultar animal por id
          d) Incluir registro de animal
          e) Salvar dados em arquivo
          f) Sair.
          """)
    choice = input()
    return choice

def input_new_animal(database):
    id = input("ID: ")
    nickname = input("Apelido: ")
    start_date = input("Data de início do monitoramento: ")
    species = input("Espécie: ")
    sex = input("Sexo (M/F): ")
    birth_date = input("Data de nascimento (opcional): ")
    animal = Animal(id, nickname, start_date, species, sex, birth_date)
    database.insert(animal)
    print("Animal adicionado com sucesso")
    return database

def remove_animal(database):
    id = input("Id do animal a ser removido: ")
    animal = Animal(id)
    database.delete(animal)
    print("Animal removido com sucesso")
    return database

def consult_animal(database):
    id = input("Id do animal a ser consultado: ")
    print("")
    search_animal = Animal(id)
    animal = database.find(search_animal)
    if animal:
        print("Animal encontrado:", end=" ")
        print(animal.value)
    else:
        print("Animal não encontrado")

    return database

def add_health_Historic(database):
    id = input("Id do animal: ")
    date = input("Data da análise: ")
    temperature = float(input("Temperatura: "))
    weight = float(input("Peso: "))
    height = float(input("Altura: "))
    collected_blood_sample = input("Coletou amostra de sangue? (S/N): ")
    health_exam_result_was_ok = input("Exame de saúde OK? (S/N): ")
    observation = input("Motivo do exame não ter sido OK: ") if health_exam_result_was_ok.upper() != "S" else ""
    health_historic = HealthHistoric(date, temperature, weight, height, collected_blood_sample, health_exam_result_was_ok, observation)

    #insert dudu tree here O.o
    print("Registro atualizado com sucesso.")

def save_to_file(root):
    def serialize(node):
        if not node:
            # :J
            return None
        return {
            'id': node.animal.id,
            'nickname': node.animal.nickname,
            'start_date': node.animal.start_date,
            'species': node.animal.species,
            'sex': node.animal.sex,
            'birth_date': node.animal.birth_date,
            'health_historic': [{
                'date': record.date,
                'temperature': record.temperature,
                'weight': record.weight,
                'height': record.height,
                'collected_blood_sample': record.collected_blood_sample,
                'health_exam_result_was_ok': record.health_exam_result_was_ok,
                'observation': record.observation
            } for record in node.animal.health_historic],
            'left': serialize(node.left),
            'right': serialize(node.right)
        }

    tree_data = serialize(root)
    with open("data.json", w) as file:
        json.dump(tree_data, file, indent=4)

if __name__ == '__main__':
    database = AVLTree()
    while True:
        tree = AVLTree
        choice = display_menu()

        if choice == 'a':
            database = input_new_animal(database)
        elif choice == 'b':
            database = remove_animal(database)
        elif choice == 'c':
            database = consult_animal(database)
        elif choice == 'd':
            add_health_Historic(database)
        elif choice == 'e':
            save_to_file('insert dudu tree root here')
        elif choice == 'f':
            print("Saindo...")
            break
