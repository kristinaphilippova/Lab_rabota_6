def calculate_weights(num_criteria):
    pairwise_matrix = [[0 for _ in range(num_criteria)] for _ in range(num_criteria)]

    for i in range(num_criteria):
        for j in range(i+1, num_criteria):
            try:
                value = float(input(f"Введите значение сравнения критерия {i+1} и {j+1}: "))
                pairwise_matrix[i][j] = value
                pairwise_matrix[j][i] = 1 / value
            except ValueError:
                print("Ошибка ввода! Попробуйте снова.")
                return

    sum_columns = [sum(column) for column in zip(*pairwise_matrix)]
    normalized_matrix = [[value/sum_col for value in row] for row, sum_col in zip(pairwise_matrix, sum_columns)]

    weights = [sum(row) / num_criteria for row in normalized_matrix]

    return weights


def main():
    try:
        num_criteria = int(input("Введите количество критериев: "))
        weights = calculate_weights(num_criteria)
        print("Весовые коэффициенты:")
        for weight in weights:
            print(f"{weight:.2f}")
    except ValueError:
        print("Ошибка ввода! Проверьте правильность введенного количества критериев.")


if __name__ == "__main__":
    main()
