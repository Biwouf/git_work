#! /usr/bin/env python3
# coding: utf-8

#Script qui parse un petit fichier CSV

import pandas as panda 

races = panda.read_csv('triathlon.csv', sep=',')
distances = races['Distance'].dropna().unique()
print(distances)

#Afficher les distances uniquement XXL
long_races = races.Nom[races["Distance"] == "XXL"]
#print(long_races)