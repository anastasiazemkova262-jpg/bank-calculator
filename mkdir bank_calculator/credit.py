#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Модуль расчета кредита
РЕАЛИЗОВАНО: разработчиком A
"""

# Импортируем модуль валидации
# (пока он не готов, но мы его импортируем для будущей интеграции)
# from validation import validate_positive_float, validate_year_range, get_valid_input


def calculate_credit(amount, rate, years):
    """
    РАССЧИТЫВАЕТ ЕЖЕМЕСЯЧНЫЙ ПЛАТЕЖ И ОБЩУЮ СУММУ ПО КРЕДИТУ
    
    Используется АННУИТЕТНАЯ СХЕМА платежей:
    - Ежемесячный платеж одинаковый весь срок
    - P = (S * i) / (1 - (1 + i)^(-n))
    
    где:
    S - сумма кредита
    i - месячная процентная ставка (годовая ставка / 12 / 100)
    n - количество месяцев (срок в годах * 12)
    
    Args:
        amount (float): Сумма кредита
        rate (float): Годовая процентная ставка
        years (int): Срок кредита в годах
        
    Returns:
        tuple: (monthly_payment, total_amount) - ежемесячный платеж и общая сумма
    """
    print(f"    Расчет кредита: сумма={amount}, ставка={rate}%, срок={years} лет")
    
    # Месячная процентная ставка (в долях)
    monthly_rate = rate / 100 / 12
    
    # Количество месяцев
    months = years * 12
    
    if monthly_rate == 0:
        # Если ставка 0% - просто делим на месяцы
        monthly_payment = amount / months
    else:
        # Аннуитетный платеж
        # P = (S * i * (1 + i)^n) / ((1 + i)^n - 1)
        monthly_payment = amount * monthly_rate * (1 + monthly_rate)  months / ((1 + monthly_rate)  months - 1)
    
    # Общая сумма выплат
    total_amount = monthly_payment * months
    
    # Округляем до копеек
    return round(monthly_payment, 2), round(total_amount, 2)


def calculate_credit_differentiated(amount, rate, years):
    """
    АЛЬТЕРНАТИВНЫЙ МЕТОД: ДИФФЕРЕНЦИРОВАННЫЕ ПЛАТЕЖИ
    
    Args:
        amount (float): Сумма кредита
        rate (float): Годовая процентная ставка
        years (int): Срок кредита в годах
        
    Returns:
        tuple: (first_payment, last_payment, total_amount)
    """
    monthly_rate = rate / 100 / 12
    months = years * 12
    main_debt = amount / months  # Основной долг в месяц
    
    # Первый платеж (проценты на полную сумму)
    first_payment = main_debt + amount * monthly_rate
    
    # Последний платеж (проценты на остаток)
    last_payment = main_debt + main_debt * monthly_rate
    
    # Общая сумма (сумма арифметической прогрессии)
    total_amount = main_debt * months + monthly_rate * (amount + main_debt) * months / 2
    
    return round(first_payment, 2), round(last_payment, 2), round(total_amount, 2)
