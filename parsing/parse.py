#using defaultdict approach
from collections import defaultdict

channel = open('ff.txt').readlines();

element_list = []

#primary approach
file_dict = {}
#default dict approach
#file_dict = defaultdict(list)

#loop for all the categories
for elements in range(0, len(channel[0].split())) :
    #renew the element_list container
    element_list.clear()
    #loop across all the values per category
    for rows in range(1, len(channel)) :
        element_list.insert(rows - 1, channel[rows].split()[elements])
    #primary approach
    file_dict[channel[0].split()[elements]] = element_list
    #defalut dick approach
    #file_dict[channel[0].split()[elements]].append(element_list)
print(file_dict)
