#Вычисление весовых коэффициентов критериев в анализе парных сравнений. 
def calculate_weights(num_criteria):
    pairwise_matrix = [[0 for _ in range(num_criteria)] for _ in range(num_criteria)]
#Заполнение матрицы. Начиная с первого критерия, пользователю предлагается ввести значение сравнения для каждой пары критериев, и эти значения сохраняются в матрицу `pairwise_matrix`.
    for i in range(num_criteria):
        for j in range(i+1, num_criteria):
            try:
                value = float(input(f"Введите значение сравнения критерия {i+1} и {j+1}: "))
                pairwise_matrix[i][j] = value
                pairwise_matrix[j][i] = 1 / value
            #Контроль правильности ввода
            except ValueError:
                print("Ошибка ввода! Попробуйте снова.")
                return

    sum_columns = [sum(column) for column in zip(*pairwise_matrix)]
    #Вычисление для нормализованной матрицы `normalized_matrix`
    normalized_matrix = [[value/sum_col for value in row] for row, sum_col in zip(pairwise_matrix, sum_columns)]
    #Вычисление весовых коэффициентов путем усреднения значений в строках нормализованной матрицы. Весовой коэффициент для критерия `i+1` равен среднему значению в строке `i`.
    weights = [sum(row) / num_criteria for row in normalized_matrix]

    return weights

#Ввод количества критериев пользователем и вызов функции `calculate_weights` для расчета весовых коэффициентов
def main():
    try:
        num_criteria = int(input("Введите количество критериев: "))
        weights = calculate_weights(num_criteria)
        print("Весовые коэффициенты:")
        for weight in weights:
            print(f"{weight:.2f}")
    #Контроль правильности ввода
    except ValueError:
        print("Ошибка ввода! Проверьте правильность введенного количества критериев.")


if __name__ == "__main__":
    main()
