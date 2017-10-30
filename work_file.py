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


#Fonction qui prend un fichier en paramètre
def get_data(file_to_analyze, separator):
	data = panda.read_csv(file_to_analyze, separator)
	return data

def search_for_equal_distance(data, data_to_compare, value_to_match):
	display = data.Nom[data[data_to_compare] == value_to_match]
	print(display)

def main():
	search_for_equal_distance(analyze('triathlon.csv', ','),
								'Distance',
								'XXL')
>>>>>>> fonction_test

if __name__ == '__main__':
	main()

