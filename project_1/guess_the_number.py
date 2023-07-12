import numpy as np

def score_game(random_predict) -> int:
    """За какое количество попыток в среднем за 10000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(10000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за: {score} попытки(-ок)")


def game_core_v3(number: int = 1) -> int:
    """
    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    
    count = 0 #Счетчик попыток
    lower_bound = 1 #Начальное значение интервала
    upper_bound = 100 #Конечное значение интервала
    
    while True: 
        count += 1
        predict = (lower_bound + upper_bound) // 2 #Переменная для предположительного результата отгадывания
        
        if predict == number: #если угадали - выходим из цикла
            break

        if predict < number: 
            lower_bound = predict + 1 #если предположительный результат меньше, то присваиваем новое начальное значение интервала деленное на 2, +1
        else:
            upper_bound = predict - 1#если предположительный результат больше, то присваиваем новое конечное значение интервала деленное на 2, -1

    return count

if __name__ == '__main__':
    score_game(game_core_v3) #для импорта в ipynb
    
