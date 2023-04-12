import pandas as pd
import numpy as np


chat_id = 1124136722 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool: # Одна или две выборке на входе, заполняется исходя из условия
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    alfa = 0.07
    return (x.mean() - y.mean()) < alfa*x.mean() # Ваш ответ, True или False
