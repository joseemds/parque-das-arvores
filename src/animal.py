class Animal:
    def __init__(self, id, nickname, start_date, species, sex, birth_date=None):
        self.id = id
        self.nickname = nickname
        self.start_date = start_date
        self.species = species
        self.sex = sex
        self.birth_date = birth_date
        self.health_records = []