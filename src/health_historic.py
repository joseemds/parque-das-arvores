class HealthHistoric:
    def __init__(self, date, temperature, weight, height, collected_blood_sample, health_exam_result_was_ok, observation=""):
        self.date = date
        self.temperature = temperature
        self.weight = weight
        self.height = height
        self.collected_blood_sample = collected_blood_sample
        self.health_exam_result_was_ok = health_exam_result_was_ok
        self.observation = observation

    def __str__(self):
        return f"(data={self.date}, temperatura={self.temperature}ºC, peso={self.weight}Kg, altura={self.height}cm, coleta_amostra_sangue={self.collected_blood_sample}, resultado_exame_saude_foi_ok={self.health_exam_result_was_ok}, observacao={self.observation})"

    def __repr__(self):
        return f"(data={self.date}, temperatura={self.temperature}ºC, peso={self.weight}Kg, altura={self.height}cm, coleta_amostra_sangue={self.collected_blood_sample}, resultado_exame_saude_foi_ok={self.health_exam_result_was_ok}, observacao={self.observation})"