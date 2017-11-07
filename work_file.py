#! /usr/bin/env python3
# coding: utf-8

#Script qui parse un petit fichier CSV

import numpy as np
import pandas as panda
import matplotlib as mpl 
mpl.use('TkAgg')
import matplotlib.pyplot as plt

races = panda.read_csv('triathlon.csv', sep=',')
distances = races['Distance'].dropna().unique()
#print(distances)

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

class Distance():
	def __init__(self, name):
		self.name = name

	def get_data(self, file):
		self.data = panda.read_csv(file, ",")

	def split_by_distance(self):
		data = self.data
		distances = data['Distance'].dropna().unique()
		print(distances)


def main():
	races = Distance('All races')
	races.get_data('triathlon.csv')
	races.split_by_distance()

#def main():
#	search_for_equal_distance(analyze('triathlon.csv', ','),
#								'Distance',
#								'XXL')


if __name__ == '__main__':
	main()

