from animal import Animal
from health_historic import HealthHistoric
from avl_tree import AVLTree, Node
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
    while sex not in ['M', 'F','m', 'f']:
        print("Input inválido. Por favor, insira M ou F.")
        sex = input("Sexo (M/F): ")
    sex = sex.upper()
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
    while True:
        try:
            id = int(input("Id do animal: "))
            break
        except ValueError:
            print("Input inválido. Insira um número válido.")
    date = input("Data da análise: ")
    while True:
        try:
            temperature = float(input("Temperatura em ºC: "))
            weight = round(float(input("Peso em Kg: ")), 3)
            height = float(input("Altura em cm: "))
            break
        except ValueError:
            print("Input inválido. Por favor, insira um número válido.")
    collected_blood_sample = input("Coletou amostra de sangue? (S/N): ")
    while collected_blood_sample.upper() not in ['S', 'N']:
        print("Input inválido. Por favor, insira S ou N.")
        collected_blood_sample = input("Coletou amostra de sangue? (S/N): ")

    health_exam_result_was_ok = input("Exame de saúde OK? (S/N): ")
    while health_exam_result_was_ok.upper() not in ['S', 'N']:
        print("Input inválido. Por favor, insira S ou N.")
        health_exam_result_was_ok = input("Exame de saúde OK? (S/N): ")
    observation = input("Motivo do exame não ter sido OK: ") if health_exam_result_was_ok.upper() != "S" else ""
    health_historic = HealthHistoric(date, temperature, weight, height, collected_blood_sample, health_exam_result_was_ok, observation)

    animal = database.find(Animal(id))
    if not animal:
        print("Animal não encontrado.")
        return
    
    animal.value.health_historic.append(health_historic)
    print("Animal atualizado: ", animal.value)
    print("Registro atualizado com sucesso.")

def save_to_file(root):
    def serialize(node):
        if not node:
            return None
        return {
            'id': node.value.id,  
            'nickname': node.value.nickname,  
            'start_date': node.value.start_date,  
            'species': node.value.species,  
            'sex': node.value.sex, 
            'birth_date': node.value.birth_date, 
            'health_historic': [{
                'date': record.date,
                'temperature': record.temperature,
                'weight': record.weight,
                'height': record.height,
                'collected_blood_sample': record.collected_blood_sample,
                'health_exam_result_was_ok': record.health_exam_result_was_ok,
                'observation': record.observation
            } for record in node.value.health_historic], 
            'left': serialize(node.left),
            'right': serialize(node.right)
        }

    tree_data = serialize(root)
    with open("data.json", "w") as file:  
        json.dump(tree_data, file, indent=4)

def load_from_file():
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
            print("Arquivo carregado com sucesso.")
        return rebuild_tree(data)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Erro ao carregar o arquivo: {str(e)}")
        return AVLTree() 

def rebuild_tree(data):
    if not data or not isinstance(data, list):
        return AVLTree()  

    tree = AVLTree()
   
    for item in data:
        animal = Animal(
            id=item['id'],
            nickname=item['nickname'],
            start_date=item['start_date'],
            species=item['species'],
            sex=item['sex'],
            birth_date=item['birth_date']
        )

        for historic in item['health_historic']:
            health_history = HealthHistoric(
                date=historic['date'],
                temperature=historic['temperature'],
                weight=historic['weight'],
                height=historic['height'],
                collected_blood_sample=historic['collected_blood_sample'],
                health_exam_result_was_ok=historic['health_exam_result_was_ok'],
                observation=historic['observation']
            )
            animal.health_historic.append(health_history)
        
        tree.insert(animal)
        
    return tree

if __name__ == '__main__':
    database = load_from_file()
    if not isinstance(database, AVLTree):
        database = AVLTree()

    while True:
        choice = display_menu()
        
        if choice == 'a':
            database = input_new_animal(database)
        elif choice == 'b':
            database = remove_animal(database)
        elif choice == 'c':
            consult_animal(database)
        elif choice == 'd':
            add_health_Historic(database)
        elif choice == 'e':
            save_to_file(database.root)
        elif choice == 'f':
            print("Saindo...")
            break


if __name__ == '__main__':
    database = load_from_file()
    if not isinstance(database, AVLTree):
        database = AVLTree()

    while True:
        choice = display_menu()
        
        if choice == 'a':
            database = input_new_animal(database)
        elif choice == 'b':
            database = remove_animal(database)
        elif choice == 'c':
            consult_animal(database)
        elif choice == 'd':
            add_health_Historic(database)
        elif choice == 'e':
            save_to_file(database.root)
        elif choice == 'f':
            print("Saindo...")
            break
