#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Модуль валидации входных данных
ЗАГОТОВКА: Все функции будут реализованы разработчиком C
"""

def validate_positive_float(value):
    """
    ПРОВЕРЯЕТ, ЧТО ЧИСЛО ПОЛОЖИТЕЛЬНОЕ
    
    Args:
        value (str): Строка для проверки
        
    Returns:
        tuple: (bool, str) - (успех, сообщение об ошибке)
        
    TODO: Реализовать разработчиком C
    """
    print(f"    [ЗАГЛУШКА] validate_positive_float({value})")
    return True, ""  # Заглушка: всегда успех


def validate_year_range(years):
    """
    ПРОВЕРЯЕТ, ЧТО СРОК В ГОДАХ ОТ 1 ДО 30
    
    Args:
        years (str): Строка с количеством лет
        
    Returns:
        tuple: (bool, str) - (успех, сообщение об ошибке)
        
    TODO: Реализовать разработчиком C
    """
    print(f"    [ЗАГЛУШКА] validate_year_range({years})")
    return True, ""  # Заглушка: всегда успех


def get_valid_input(prompt, validator_func):
    """
    ЗАПРАШИВАЕТ ВВОД И ВАЛИДИРУЕТ ЕГО
    
    Args:
        prompt (str): Приглашение для ввода
        validator_func (function): Функция-валидатор
        
    Returns:
        float: Введенное число
        
    TODO: Реализовать разработчиком C
    """
    print(f"    [ЗАГЛУШКА] get_valid_input('{prompt}')")
    return 1000.0  # Заглушка: всегда возвращает 1000