import pandas as pd
import numpy as np
from scipy.stats import mannwhitneyu

chat_id = 1124136722 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool: # Одна или две выборке на входе, заполняется исходя из условия
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    alfa = 0.07
    x_list = [i for i in x]
    y_list = [k for k in y]
    p = mannwhitneyu(x_list, y_list, alternative="greater").pvalue
    return p < alfa # Ваш ответ, True (отклонить Но, конверсия уменьшилась) или False (не отклонять Но, конверсия не изменилась)
