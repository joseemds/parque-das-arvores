import sys
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

def get_id(message="Id: "):
    while True:
        try:
            id = int(input(message))
            break
        except ValueError:
            print("Input inválido. Insira um número válido.")
    return id

def input_new_animal(database):
    id = get_id()
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
    id = get_id("Id do animal a ser removido: ")
    animal = Animal(id)
    database.delete(animal)
    print("Animal removido com sucesso")
    return database

def consult_animal(database):
    id = get_id("Id do animal a ser consultado: ")
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
    id = get_id("Id do animal: ")
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

def save_to_file(root, path):
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
    # os.makedirs(os.path.dirname("./data"), exist_ok=True)
    with open(path, "w") as file:  
        json.dump(tree_data, file, indent=4)

def load_from_file(path):
    try:
        with open(path, "r") as file:
            data = json.load(file)
            print("Arquivo carregado com sucesso.")
        return rebuild_tree(data)
    except (FileNotFoundError) as e:
        print(f"ATENCAO: O arquivo passado não existe, deseja continuar? [S/N] (Se sim, será criado um arquivo vazio)")
        y_or_n = input()
        while y_or_n not in ["S", "N", "s", "n"]:
          y_or_n = input("Favor inserir S para sim e N para não [S/N]")

        if y_or_n in ["S", "s"]:
         with open(path, "w") as file:
            json.dump({}, file)
        else:
            exit(-1)




def rebuild_node(data):
    def _rec_build_node(data, height):
        if not data:
            return None

        animal = Animal(
            id=int(data['id']),
            nickname=data['nickname'],
            start_date=data['start_date'],
            species=data['species'],
            sex=data['sex'],
            birth_date=data['birth_date']
        )

        for historic in data['health_historic']:
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

        node = Node(animal)
        node.height = height
        node.left = _rec_build_node(data['left'], height+1)
        node.right = _rec_build_node(data['right'], height+1)

        return node

    return _rec_build_node(data, 1)


def construct_tree(data, tree):
    for item in data:
        animal = Animal(
            id=int(item['id']),
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




def rebuild_tree(data):
    if not data:
        return AVLTree()
    elif isinstance(data, list):
        return construct_tree(data, AVLTree())

    root = rebuild_node(data)
    tree = AVLTree(root)
    return tree

def main():
    try:
        path = sys.argv[1]
        database = load_from_file(path)
        if not isinstance(database, AVLTree):
            database = AVLTree()
    except IndexError:
        print("Error: Passar como parametro arquivo para popular banco de dados e para escrita.: ./main arquivo.json")
        exit(-1)
    
    while True:
        try:
            choice = display_menu()
            
            try:
                if choice == 'a':
                    database = input_new_animal(database)
                elif choice == 'b':
                    database = remove_animal(database)
                elif choice == 'c':
                    consult_animal(database)
                elif choice == 'd':
                    add_health_Historic(database)
                elif choice == 'e':
                    save_to_file(database.root, path)
                elif choice == 'f':
                    print("Saindo...")
                    break
            except KeyboardInterrupt:
                print("Cancelando operação")
        except KeyboardInterrupt:
            print("Saindo...")
            break

if __name__ == '__main__':
    main()

