class HeathRecord:
    def __init__(self, date, temperature, weight, height, collected_blood_sample, health_exam_result_was_ok, observation=""):
        self.date = date
        self.temperature = temperature
        self.weight = weight
        self.height = height
        self.collected_blood_sample = collected_blood_sample
        self.health_exam_result_was_ok = health_exam_result_was_ok
        self.observation = observation