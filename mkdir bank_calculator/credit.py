#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Модуль расчета кредита
ЗАГОТОВКА: Функция будет реализована разработчиком A
"""

def calculate_credit(amount, rate, years):
    """
    РАССЧИТЫВАЕТ ЕЖЕМЕСЯЧНЫЙ ПЛАТЕЖ И ОБЩУЮ СУММУ ПО КРЕДИТУ
    
    Args:
        amount (float): Сумма кредита
        rate (float): Годовая процентная ставка
        years (int): Срок кредита в годах
        
    Returns:
        tuple: (monthly_payment, total_amount) - ежемесячный платеж и общая сумма
        
    TODO: Реализовать разработчиком A
    """
    print(f"    [ЗАГЛУШКА] calculate_credit(amount={amount}, rate={rate}, years={years})")
    
    # Заглушка: возвращаем примерные значения
    monthly = amount / (years * 12)
    total = amount * 1.2
    
    return round(monthly, 2), round(total, 2)