#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Модуль расчета депозита
ЗАГОТОВКА: Функция будет реализована разработчиком B
"""

def calculate_deposit(amount, rate, years):
    """
    РАССЧИТЫВАЕТ ИТОГОВУЮ СУММУ ПО ДЕПОЗИТУ
    
    Args:
        amount (float): Сумма вклада
        rate (float): Годовая процентная ставка
        years (int): Срок вклада в годах
        
    Returns:
        float: Итоговая сумма вклада
        
    TODO: Реализовать разработчиком B
    """
    print(f"    [ЗАГЛУШКА] calculate_deposit(amount={amount}, rate={rate}, years={years})")
    
    # Заглушка: простые проценты
    result = amount * (1 + rate / 100 * years)
    
    return round(result, 2)