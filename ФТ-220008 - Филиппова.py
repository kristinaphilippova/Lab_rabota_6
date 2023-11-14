def calculate_weights(n_criteria):
    criteria = []
    weights = []
    total = 0

    for i in range(n_criteria):
        for j in range(i+1, n_criteria):
            while True:
                try:
                    comparison_value = float(input(f"Введите значение сравнения для критерия {i + 1} и {j + 1}: "))
                    break
                except ValueError:
                    print("Ошибка ввода! Попробуйте снова.")
        criteria.append(comparison_value)
        total += comparison_value

    # Проверка на ноль и коррекция суммы критериев
    if total == 0:
        print("Ошибка: сумма критериев не может быть равна нулю.")
        return None

    for i in range(n_criteria):
        weight = criteria[i] / total
        weights.append(weight)

    return weights


def main():
    while True:
        try:
            n = int(input("Введите количество критериев: "))
            break
        except ValueError:
            print("Ошибка ввода! Попробуйте снова.")

    result = calculate_weights(n)

    if result:
        print("Весовые коэффициенты:")
        for weight in result:
            print(f"{weight:.2f}")


if __name__ == "__main__":
    main()
