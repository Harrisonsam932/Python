# -*- coding: utf-8 -*-
"""
Created on Thu Sep 13 20:23:47 2018

@author: nelson
"""
class BankAccount:
    def make_account():
        return {'balance': 0}

    def deposit(account, amount):
        account['balance'] += amount
        return account['balance']

    def withdraw(account, amount):
        account['balance'] -= amount
        return account['balance']

a = BankAccount()