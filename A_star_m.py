import math
import time
from sys import getsizeof
from construir_grafo_m import *

def harvesine(lon1, lat1, lon2, lat2):
    # haversine formula  
    a = math.sin(math.radians(lat2) - math.radians(lat1)/2)**2 + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(math.radians(lon2) - math.radians(lon1) /2)**2
    c = 2 * math.asin(math.sqrt(a)) 
    return c * 6371

def euclidean_distance(lat1, lon1, lat2, lon2):
    # Calculando a distância euclidiana
    return math.sqrt((math.radians(lat2) - math.radians(lat1))**2 + (math.radians(lon2) - math.radians(lon1))**2) * 6371.0

def A_star_harvesine(start_node, end_node, graph, coordinates, timeout=10):
    runtime = time.time()
    closed = []             
    opened = []             
    g_cost = {}
    expanded_nodes = 0
    g_cost[start_node[0]] = 0

    opened.append(start_node)

    while len(opened) > 0:
        used_memory = getsizeof(closed) + getsizeof(opened) + getsizeof(g_cost) + getsizeof(expanded_nodes)
        f_cost_opened_list = [node[1] for node in opened]
        min_f_cost = min(f_cost_opened_list)
        chosen_index = f_cost_opened_list.index(min_f_cost)
        node = opened[chosen_index][0]
        closed.append(opened[chosen_index])
        opened.pop(chosen_index)
        expanded_nodes = expanded_nodes + 1

        if node == end_node[0]:
            break
        for item in graph[node]:
            if item[0] in [closed_item[0] for closed_item in closed]:
                continue
            g_cost[item[0]] = g_cost[node] + item[1]           
            f_cost_node = g_cost[node] + harvesine(coordinates[item[0]][0][0],coordinates[item[0]][0][1], coordinates[end_node[0]][0][0], coordinates[end_node[0]][0][1]) + item[1]
            opened.append([item[0], f_cost_node])

        if (time.time() - runtime) > timeout:
            break                       

    return closed, expanded_nodes, used_memory

def A_star_euclidian_distance(start_node, end_node, graph, coordinates, timeout=10):
    runtime = time.time()
    closed = []             
    opened = []             
    g_cost = {}
    expanded_nodes = 0
    g_cost[start_node[0]] = 0

    opened.append(start_node)

    while len(opened) > 0:
        used_memory = getsizeof(closed) + getsizeof(opened) + getsizeof(g_cost) + getsizeof(expanded_nodes)
        f_cost_opened_list = [node[1] for node in opened]
        min_f_cost = min(f_cost_opened_list)
        chosen_index = f_cost_opened_list.index(min_f_cost)
        node = opened[chosen_index][0]
        closed.append(opened[chosen_index])
        opened.pop(chosen_index)
        expanded_nodes = expanded_nodes + 1

        if node == end_node[0]:
            break
        for item in graph[node]:
            if item[0] in [closed_item[0] for closed_item in closed]:
                continue
            g_cost[item[0]] = g_cost[node] + item[1]           
            f_cost_node = g_cost[node] + euclidean_distance(coordinates[item[0]][0][0],coordinates[item[0]][0][1], coordinates[end_node[0]][0][0], coordinates[end_node[0]][0][1]) + item[1]
            opened.append([item[0], f_cost_node])

        if (time.time() - runtime) > timeout:
            break                       

    return closed, expanded_nodes, used_memory