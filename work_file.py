#! /usr/bin/env python3
# coding: utf-8

#Script qui parse un petit fichier CSV

import pandas as pd 

races = pd.read_csv('triathlon.csv', sep=',')
names = races['Nom'].unique()

#Afficher les distances uniquement XXL
long_races = races.Nom[races["Distance"] == "XXL"]
print(long_races)