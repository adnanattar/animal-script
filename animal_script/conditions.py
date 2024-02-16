class Conditions:
    @staticmethod
    def evaluate_condition(condition):
        try:
            if condition:
                return "Roar Condition is True."
            else:
                return "Roar Condition is False."
        except Exception as e:
            return "Follow the Animal Rules"
