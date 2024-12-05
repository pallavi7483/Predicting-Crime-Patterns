# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 17:28:05 2024

@author: Lenovo
"""
import sys
def mapper(line):
    fields = line.strip().split(',')
    year, location, crime = fields[1], fields[2], fields[3]
    return (year, location, crime, 1)

def reducer(grouped_data):
    for key, value in grouped_data:
        year, location, crime, count = key + (0,)
        for v in value:
            count += v[-1]
        yield year, location, crime, count

if __name__ == '__main__':
    with open('crime.csv', 'r') as csvfile:
        data = csvfile.readlines()
        mapped_data = [mapper(line) for line in data]
        grouped_data = {key: [val for val in mapped_data if val[:3] == key] for key in set(tuple(val[:3]) for val in mapped_data)}
        for key, value in grouped_data.items():
           print(key, value)

if __name__ == '__main__':
    mapped_data = [mapper(line) for line in sys.stdin]
    grouped_data = {key: [val for val in mapped_data if val[:3] == key] for key in set(tuple(val[:3]) for val in mapped_data)}
    for key, value in grouped_data.items():
        print(key, value)
