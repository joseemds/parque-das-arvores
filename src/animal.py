class Animal:
    def __init__(self, id, nickname=None, start_date=None, species=None, sex=None, birth_date=None):
        self.id = id
        self.nickname = nickname
        self.start_date = start_date
        self.species = species
        self.sex = sex
        self.birth_date = birth_date
        self.health_historic = []

    def add_health_history(self, health_history):
        self.health_historic.append(health_history)

    def __repr__(self):
        return f"(id={self.id}, apelido={self.nickname}, especie={self.species}, sexo={self.sex}, data_nascimento={self.birth_date}, data_inicio={self.start_date}, historico_saude={str(self.health_historic)})"

    def __eq__(self, other):
        return self.id == other.id

    def __lt__(self, other):
        return self.id < other.id

    def __gt__(self, other):
        return self.id > other.id
