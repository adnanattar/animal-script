class Conditions:
    @staticmethod
    def evaluate_condition(condition):
        try:
            if condition:
                return "Roar Condition is True."
            else:
                return "Roar Condition is False."
            # New functionalities
            if condition.startswith("PolarBears"):
                return "Polar bears roar only in icy conditions."
            elif condition.startswith("Koalas"):
                return "Koalas sleep when it's not sunny."
            elif condition.startswith("Penguins"):
                return "Penguins waddle in cold climates."
            elif condition.startswith("Kangaroos"):
                return "Kangaroos hop during the day."
            elif condition.startswith("Sloths"):
                return "Sloths move slowly in hot weather."
            elif condition.startswith("Gorillas"):
                return "Gorillas beat their chests when it's raining."
            elif condition.startswith("Lions"):
                return "Lions roar when they're hungry."
            elif condition.startswith("Bears"):
                return "Bears hibernate during winter."
            elif condition.startswith("Monkeys"):
                return "Monkeys swing from trees during the day."
            else:
                return "Unknown condition."
        except Exception as e:
            return "Follow the Animal Rules"
