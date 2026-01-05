# required data

graph = {
    "Chicago": {
        "Detroit": 283,
        "Cleveland": 345,
        "Indianapolis": 182
    },

    "Detroit": {
        "Chicago": 283,
        "Buffalo": 256,
        "Cleveland": 169
    },

    "Cleveland": {
        "Chicago": 345,
        "Detroit": 169,
        "Buffalo": 189,
        "Pittsburgh": 134,
        "Columbus": 144
    },

    "Columbus": {
        "Cleveland": 144,
        "Pittsburgh": 185,
        "Indianapolis": 176
    },

    "Indianapolis": {
        "Chicago": 182,
        "Columbus": 176
    },

    "Buffalo": {
        "Detroit": 256,
        "Cleveland": 189,
        "Pittsburgh": 215,
        "Syracuse": 150
    },

    "Syracuse": {
        "Buffalo": 150,
        "Boston": 312,
        "New York": 254,
        "Pittsburgh": 253
    },

    "Pittsburgh": {
        "Cleveland": 134,
        "Buffalo": 215,
        "Syracuse": 253,
        "Columbus": 185,
        "Philadelphia": 305,
        "Baltimore": 247
    },

    "Baltimore": {
        "Pittsburgh": 247,
        "Philadelphia": 101
    },

    "Philadelphia": {
        "Baltimore": 101,
        "Pittsburgh": 305,
        "New York": 97
    },

    "New York": {
        "Philadelphia": 97,
        "Boston": 215,
        "Providence": 181,
        "Syracuse": 254
    },

    "Providence": {
        "New York": 181,
        "Boston": 50
    },

    "Boston": {
        "Syracuse": 312,
        "New York": 215,
        "Providence": 50,
        "Portland": 107
    },

    "Portland": {
        "Boston": 107
    }
}


# bfs algorithm
from collections import deque

def bfs_all_paths(graph, start, goal):
    queue = deque([(start, [start], 0)])
    paths = []

    while queue:
        node, path, cost = queue.popleft()

        if node == goal:
            paths.append((path, cost))
            continue

        for neighbor, weight in graph[node].items():
            if neighbor not in path:
                queue.append((neighbor, path + [neighbor], cost + weight))

    return paths

def dfs_all_paths(graph, start, goal):
    paths = []

    def dfs(node, path, cost):
        if node == goal:
            paths.append((path, cost))
            return

        for neighbor, weight in graph[node].items():
            if neighbor not in path:
                dfs(neighbor, path + [neighbor], cost + weight)

    dfs(start, [start], 0)
    return paths

ans1=bfs_all_paths(graph,"Syracuse","Chicago")
print(ans1)

# output

# [(['Syracuse', 'Buffalo', 'Detroit', 'Chicago'], 689),
#  (['Syracuse', 'Buffalo', 'Cleveland', 'Chicago'], 684), 
#  (['Syracuse', 'Pittsburgh', 'Cleveland', 'Chicago'], 732), 
#  (['Syracuse', 'Buffalo', 'Detroit', 'Cleveland', 'Chicago'], 920), 
#  (['Syracuse', 'Buffalo', 'Cleveland', 'Detroit', 'Chicago'], 791), 
#  (['Syracuse', 'Buffalo', 'Pittsburgh', 'Cleveland', 'Chicago'], 844), 
#  (['Syracuse', 'Pittsburgh', 'Cleveland', 'Detroit', 'Chicago'], 839), 
#  (['Syracuse', 'Pittsburgh', 'Buffalo', 'Detroit', 'Chicago'], 1007), 
#  (['Syracuse', 'Pittsburgh', 'Buffalo', 'Cleveland', 'Chicago'], 1002), 
#  (['Syracuse', 'Pittsburgh', 'Columbus', 'Cleveland', 'Chicago'], 927), 
#  (['Syracuse', 'Pittsburgh', 'Columbus', 'Indianapolis', 'Chicago'], 796), 
#  (['Syracuse', 'Buffalo', 'Cleveland', 'Columbus', 'Indianapolis', 'Chicago'], 841), 
#  (['Syracuse', 'Buffalo', 'Pittsburgh', 'Cleveland', 'Detroit', 'Chicago'], 951), 
#  (['Syracuse', 'Buffalo', 'Pittsburgh', 'Columbus', 'Cleveland', 'Chicago'], 1039), 
#  (['Syracuse', 'Buffalo', 'Pittsburgh', 'Columbus', 'Indianapolis', 'Chicago'], 908), 
#  (['Syracuse', 'New York', 'Philadelphia', 'Pittsburgh', 'Cleveland', 'Chicago'], 1135), 
#  (['Syracuse', 'Pittsburgh', 'Cleveland', 'Buffalo', 'Detroit', 'Chicago'], 1115), 
#  (['Syracuse', 'Pittsburgh', 'Cleveland', 'Columbus', 'Indianapolis', 'Chicago'], 889), 
#  (['Syracuse', 'Pittsburgh', 'Buffalo', 'Detroit', 'Cleveland', 'Chicago'], 1238), 
#  (['Syracuse', 'Pittsburgh', 'Buffalo', 'Cleveland', 'Detroit', 'Chicago'], 1109), 
#  (['Syracuse', 'Pittsburgh', 'Columbus', 'Cleveland', 'Detroit', 'Chicago'], 1034), 
#  (['Syracuse', 'Buffalo', 'Detroit', 'Cleveland', 'Columbus', 'Indianapolis', 'Chicago'], 1077), 
#  (['Syracuse', 'Buffalo', 'Cleveland', 'Pittsburgh', 'Columbus', 'Indianapolis', 'Chicago'], 1016), 
#  (['Syracuse', 'Buffalo', 'Pittsburgh', 'Cleveland', 'Columbus', 'Indianapolis', 'Chicago'], 1001), 
#  (['Syracuse', 'Buffalo', 'Pittsburgh', 'Columbus', 'Cleveland', 'Detroit', 'Chicago'], 1146), 
#  (['Syracuse', 'Boston', 'New York', 'Philadelphia', 'Pittsburgh', 'Cleveland', 'Chicago'], 1408), 
#  (['Syracuse', 'New York', 'Philadelphia', 'Baltimore', 'Pittsburgh', 'Cleveland', 'Chicago'], 1178), 
#  (['Syracuse', 'New York', 'Philadelphia', 'Pittsburgh', 'Cleveland', 'Detroit', 'Chicago'], 1242), 
#  (['Syracuse', 'New York', 'Philadelphia', 'Pittsburgh', 'Buffalo', 'Detroit', 'Chicago'], 1410), 
#  (['Syracuse', 'New York', 'Philadelphia', 'Pittsburgh', 'Buffalo', 'Cleveland', 'Chicago'], 1405), 
#  (['Syracuse', 'New York', 'Philadelphia', 'Pittsburgh', 'Columbus', 'Cleveland', 'Chicago'], 1330), 
#  (['Syracuse', 'New York', 'Philadelphia', 'Pittsburgh', 'Columbus', 'Indianapolis', 'Chicago'], 1199), 
#  (['Syracuse', 'Pittsburgh', 'Buffalo', 'Cleveland', 'Columbus', 'Indianapolis', 'Chicago'], 1159), 
#  (['Syracuse', 'Pittsburgh', 'Columbus', 'Cleveland', 'Buffalo', 'Detroit', 'Chicago'], 1310), 
#  (['Syracuse', 'Buffalo', 'Detroit', 'Cleveland', 'Pittsburgh', 'Columbus', 'Indianapolis', 'Chicago'], 1252), 
#  (['Syracuse', 'Boston', 'New York', 'Philadelphia', 'Baltimore', 'Pittsburgh', 'Cleveland', 'Chicago'], 1451), 
#  (['Syracuse', 'Boston', 'New York', 'Philadelphia', 'Pittsburgh', 'Cleveland', 'Detroit', 'Chicago'], 1515), 
#  (['Syracuse', 'Boston', 'New York', 'Philadelphia', 'Pittsburgh', 'Buffalo', 'Detroit', 'Chicago'], 1683), 
#  (['Syracuse', 'Boston', 'New York', 'Philadelphia', 'Pittsburgh', 'Buffalo', 'Cleveland', 'Chicago'], 1678), 
#  (['Syracuse', 'Boston', 'New York', 'Philadelphia', 'Pittsburgh', 'Columbus', 'Cleveland', 'Chicago'], 1603), 
#  (['Syracuse', 'Boston', 'New York', 'Philadelphia', 'Pittsburgh', 'Columbus', 'Indianapolis', 'Chicago'], 1472), 
#  (['Syracuse', 'Boston', 'Providence', 'New York', 'Philadelphia', 'Pittsburgh', 'Cleveland', 'Chicago'], 1424), 
#  (['Syracuse', 'New York', 'Philadelphia', 'Baltimore', 'Pittsburgh', 'Cleveland', 'Detroit', 'Chicago'], 1285), 
#  (['Syracuse', 'New York', 'Philadelphia', 'Baltimore', 'Pittsburgh', 'Buffalo', 'Detroit', 'Chicago'], 1453), 
#  (['Syracuse', 'New York', 'Philadelphia', 'Baltimore', 'Pittsburgh', 'Buffalo', 'Cleveland', 'Chicago'], 1448), 
#  (['Syracuse', 'New York', 'Philadelphia', 'Baltimore', 'Pittsburgh', 'Columbus', 'Cleveland', 'Chicago'], 1373), 
#  (['Syracuse', 'New York', 'Philadelphia', 'Baltimore', 'Pittsburgh', 'Columbus', 'Indianapolis', 'Chicago'], 1242), 
#  (['Syracuse', 'New York', 'Philadelphia', 'Pittsburgh', 'Cleveland', 'Buffalo', 'Detroit', 'Chicago'], 1518), 
#  (['Syracuse', 'New York', 'Philadelphia', 'Pittsburgh', 'Cleveland', 'Columbus', 'Indianapolis', 'Chicago'], 1292), 
#  (['Syracuse', 'New York', 'Philadelphia', 'Pittsburgh', 'Buffalo', 'Detroit', 'Cleveland', 'Chicago'], 1641), 
#  (['Syracuse', 'New York', 'Philadelphia', 'Pittsburgh', 'Buffalo', 'Cleveland', 'Detroit', 'Chicago'], 1512), 
#  (['Syracuse', 'New York', 'Philadelphia', 'Pittsburgh', 'Columbus', 'Cleveland', 'Detroit', 'Chicago'], 1437), 
#  (['Syracuse', 'Pittsburgh', 'Buffalo', 'Detroit', 'Cleveland', 'Columbus', 'Indianapolis', 'Chicago'], 1395), 
#  (['Syracuse', 'Boston', 'New York', 'Philadelphia', 'Baltimore', 'Pittsburgh', 'Cleveland', 'Detroit', 'Chicago'], 1558), 
#  (['Syracuse', 'Boston', 'New York', 'Philadelphia', 'Baltimore', 'Pittsburgh', 'Buffalo', 'Detroit', 'Chicago'], 1726), 
#  (['Syracuse', 'Boston', 'New York', 'Philadelphia', 'Baltimore', 'Pittsburgh', 'Buffalo', 'Cleveland', 'Chicago'], 1721), (['Syracuse', 'Boston', 'New York', 'Philadelphia', 'Baltimore', 'Pittsburgh', 'Columbus', 'Cleveland', 'Chicago'], 1646), (['Syracuse', 'Boston', 'New York', 'Philadelphia', 'Baltimore', 'Pittsburgh', 'Columbus', 'Indianapolis', 'Chicago'], 1515), (['Syracuse', 'Boston', 'New York', 'Philadelphia', 'Pittsburgh', 'Cleveland', 'Buffalo', 'Detroit', 'Chicago'], 1791), (['Syracuse', 'Boston', 'New York', 'Philadelphia', 'Pittsburgh', 'Cleveland', 'Columbus', 'Indianapolis', 'Chicago'], 1565), (['Syracuse', 'Boston', 'New York', 'Philadelphia', 'Pittsburgh', 'Buffalo', 'Detroit', 'Cleveland', 'Chicago'], 1914), (['Syracuse', 'Boston', 'New York', 'Philadelphia', 'Pittsburgh', 'Buffalo', 'Cleveland', 'Detroit', 'Chicago'], 1785), (['Syracuse', 'Boston', 'New York', 'Philadelphia', 'Pittsburgh', 'Columbus', 'Cleveland', 'Detroit', 'Chicago'], 1710), (['Syracuse', 'Boston', 'Providence', 'New York', 'Philadelphia', 'Baltimore', 'Pittsburgh', 'Cleveland', 'Chicago'], 1467), (['Syracuse', 'Boston', 'Providence', 'New York', 'Philadelphia', 'Pittsburgh', 'Cleveland', 'Detroit', 'Chicago'], 1531), (['Syracuse', 'Boston', 'Providence', 'New York', 'Philadelphia', 'Pittsburgh', 'Buffalo', 'Detroit', 'Chicago'], 1699), (['Syracuse', 'Boston', 'Providence', 'New York', 'Philadelphia', 'Pittsburgh', 'Buffalo', 'Cleveland', 'Chicago'], 1694), (['Syracuse', 'Boston', 'Providence', 'New York', 'Philadelphia', 'Pittsburgh', 'Columbus', 'Cleveland', 'Chicago'], 1619), (['Syracuse', 'Boston', 'Providence', 'New York', 'Philadelphia', 'Pittsburgh', 'Columbus', 'Indianapolis', 'Chicago'], 1488), (['Syracuse', 'New York', 'Philadelphia', 'Baltimore', 'Pittsburgh', 'Cleveland', 'Buffalo', 'Detroit', 'Chicago'], 1561), (['Syracuse', 'New York', 'Philadelphia', 'Baltimore', 'Pittsburgh', 'Cleveland', 'Columbus', 'Indianapolis', 'Chicago'], 1335), (['Syracuse', 'New York', 'Philadelphia', 'Baltimore', 'Pittsburgh', 'Buffalo', 'Detroit', 'Cleveland', 'Chicago'], 1684), (['Syracuse', 'New York', 'Philadelphia', 'Baltimore', 'Pittsburgh', 'Buffalo', 'Cleveland', 'Detroit', 'Chicago'], 1555), (['Syracuse', 'New York', 'Philadelphia', 'Baltimore', 'Pittsburgh', 'Columbus', 'Cleveland', 'Detroit', 'Chicago'], 1480), (['Syracuse', 'New York', 'Philadelphia', 'Pittsburgh', 'Buffalo', 'Cleveland', 'Columbus', 'Indianapolis', 'Chicago'], 1562), (['Syracuse', 'New York', 'Philadelphia', 'Pittsburgh', 'Columbus', 'Cleveland', 'Buffalo', 'Detroit', 'Chicago'], 1713), (['Syracuse', 'Boston', 'New York', 'Philadelphia', 'Baltimore', 'Pittsburgh', 'Cleveland', 'Buffalo', 'Detroit', 'Chicago'], 1834), (['Syracuse', 'Boston', 'New York', 'Philadelphia', 'Baltimore', 'Pittsburgh', 'Cleveland', 'Columbus', 'Indianapolis', 'Chicago'], 1608), (['Syracuse', 'Boston', 'New York', 'Philadelphia', 'Baltimore', 'Pittsburgh', 'Buffalo', 'Detroit', 'Cleveland', 'Chicago'], 1957), (['Syracuse', 'Boston', 'New York', 'Philadelphia', 'Baltimore', 'Pittsburgh', 'Buffalo', 'Cleveland', 'Detroit', 'Chicago'], 1828), (['Syracuse', 'Boston', 'New York', 'Philadelphia', 'Baltimore', 'Pittsburgh', 'Columbus', 'Cleveland', 'Detroit', 'Chicago'], 1753), (['Syracuse', 'Boston', 'New York', 'Philadelphia', 'Pittsburgh', 'Buffalo', 'Cleveland', 'Columbus', 'Indianapolis', 'Chicago'], 1835), (['Syracuse', 'Boston', 'New York', 'Philadelphia', 'Pittsburgh', 'Columbus', 'Cleveland', 'Buffalo', 'Detroit', 'Chicago'], 1986), (['Syracuse', 'Boston', 'Providence', 'New York', 'Philadelphia', 'Baltimore', 'Pittsburgh', 'Cleveland', 'Detroit', 'Chicago'], 1574), (['Syracuse', 'Boston', 'Providence', 'New York', 'Philadelphia', 'Baltimore', 'Pittsburgh', 'Buffalo', 'Detroit', 'Chicago'], 1742), (['Syracuse', 'Boston', 'Providence', 'New York', 'Philadelphia', 'Baltimore', 'Pittsburgh', 'Buffalo', 'Cleveland', 'Chicago'], 1737), (['Syracuse', 'Boston', 'Providence', 'New York', 'Philadelphia', 'Baltimore', 'Pittsburgh', 'Columbus', 'Cleveland', 'Chicago'], 1662), (['Syracuse', 'Boston', 'Providence', 'New York', 'Philadelphia', 'Baltimore', 'Pittsburgh', 'Columbus', 'Indianapolis', 'Chicago'], 1531), (['Syracuse', 'Boston', 'Providence', 'New York', 'Philadelphia', 'Pittsburgh', 'Cleveland', 'Buffalo', 'Detroit', 'Chicago'], 1807), (['Syracuse', 'Boston', 'Providence', 'New York', 'Philadelphia', 'Pittsburgh', 'Cleveland', 'Columbus', 'Indianapolis', 'Chicago'], 1581), (['Syracuse', 'Boston', 'Providence', 'New York', 'Philadelphia', 'Pittsburgh', 'Buffalo', 'Detroit', 'Cleveland', 'Chicago'], 1930), (['Syracuse', 'Boston', 'Providence', 'New York', 'Philadelphia', 'Pittsburgh', 'Buffalo', 'Cleveland', 'Detroit', 'Chicago'], 1801), (['Syracuse', 'Boston', 'Providence', 'New York', 'Philadelphia', 'Pittsburgh', 'Columbus', 'Cleveland', 'Detroit', 'Chicago'], 1726), (['Syracuse', 'New York', 'Philadelphia', 'Baltimore', 'Pittsburgh', 'Buffalo', 'Cleveland', 'Columbus', 'Indianapolis', 'Chicago'], 1605), (['Syracuse', 'New York', 'Philadelphia', 'Baltimore', 'Pittsburgh', 'Columbus', 'Cleveland', 'Buffalo', 'Detroit', 'Chicago'], 1756), (['Syracuse', 'New York', 'Philadelphia', 'Pittsburgh', 'Buffalo', 'Detroit', 'Cleveland', 'Columbus', 'Indianapolis', 'Chicago'], 1798), (['Syracuse', 'Boston', 'New York', 'Philadelphia', 'Baltimore', 'Pittsburgh', 'Buffalo', 'Cleveland', 'Columbus', 'Indianapolis', 'Chicago'], 1878), (['Syracuse', 'Boston', 'New York', 'Philadelphia', 'Baltimore', 'Pittsburgh', 'Columbus', 'Cleveland', 'Buffalo', 'Detroit', 'Chicago'], 2029), (['Syracuse', 'Boston', 'New York', 'Philadelphia', 'Pittsburgh', 'Buffalo', 'Detroit', 'Cleveland', 'Columbus', 'Indianapolis', 'Chicago'], 2071), (['Syracuse', 'Boston', 'Providence', 'New York', 'Philadelphia', 'Baltimore', 'Pittsburgh', 'Cleveland', 'Buffalo', 'Detroit', 'Chicago'], 1850), (['Syracuse', 'Boston', 'Providence', 'New York', 'Philadelphia', 'Baltimore', 'Pittsburgh', 'Cleveland', 'Columbus', 'Indianapolis', 'Chicago'], 1624), (['Syracuse', 'Boston', 'Providence', 'New York', 'Philadelphia', 'Baltimore', 'Pittsburgh', 'Buffalo', 'Detroit', 'Cleveland', 'Chicago'], 1973), (['Syracuse', 'Boston', 'Providence', 'New York', 'Philadelphia', 'Baltimore', 'Pittsburgh', 'Buffalo', 'Cleveland', 'Detroit', 'Chicago'], 1844), (['Syracuse', 'Boston', 'Providence', 'New York', 'Philadelphia', 'Baltimore', 'Pittsburgh', 'Columbus', 'Cleveland', 'Detroit', 'Chicago'], 1769), (['Syracuse', 'Boston', 'Providence', 'New York', 'Philadelphia', 'Pittsburgh', 'Buffalo', 'Cleveland', 'Columbus', 'Indianapolis', 'Chicago'], 1851), (['Syracuse', 'Boston', 'Providence', 'New York', 'Philadelphia', 'Pittsburgh', 'Columbus', 'Cleveland', 'Buffalo', 'Detroit', 'Chicago'], 2002), (['Syracuse', 'New York', 'Philadelphia', 'Baltimore', 'Pittsburgh', 'Buffalo', 'Detroit', 'Cleveland', 'Columbus', 'Indianapolis', 'Chicago'], 1841), (['Syracuse', 'Boston', 'New York', 'Philadelphia', 'Baltimore', 'Pittsburgh', 'Buffalo', 'Detroit', 'Cleveland', 'Columbus', 'Indianapolis', 'Chicago'], 2114), (['Syracuse', 'Boston', 'Providence', 'New York', 'Philadelphia', 'Baltimore', 'Pittsburgh', 'Buffalo', 'Cleveland', 'Columbus', 'Indianapolis', 'Chicago'], 1894), (['Syracuse', 'Boston', 'Providence', 'New York', 'Philadelphia', 'Baltimore', 'Pittsburgh', 'Columbus', 'Cleveland', 'Buffalo', 'Detroit', 'Chicago'], 2045), (['Syracuse', 'Boston', 'Providence', 'New York', 'Philadelphia', 'Pittsburgh', 'Buffalo', 'Detroit', 'Cleveland', 'Columbus', 'Indianapolis', 'Chicago'], 2087), (['Syracuse', 'Boston', 'Providence', 'New York', 'Philadelphia', 'Baltimore', 'Pittsburgh', 'Buffalo', 'Detroit', 'Cleveland', 'Columbus', 'Indianapolis', 'Chicago'], 2130)]

ans2=dfs_all_paths(graph,"Syracuse","Chicago")
print(ans2)

# output

# [(['Syracuse', 'Buffalo', 'Detroit', 'Chicago'], 689), (['Syracuse', 'Buffalo', 'Detroit', 'Cleveland', 'Chicago'], 920), (['Syracuse', 'Buffalo', 'Detroit', 'Cleveland', 'Pittsburgh', 'Columbus', 'Indianapolis', 'Chicago'], 1252), (['Syracuse', 'Buffalo', 'Detroit', 'Cleveland', 'Columbus', 'Indianapolis', 'Chicago'], 1077), (['Syracuse', 'Buffalo', 'Cleveland', 'Chicago'], 684), (['Syracuse', 'Buffalo', 'Cleveland', 'Detroit', 'Chicago'], 791), (['Syracuse', 'Buffalo', 'Cleveland', 'Pittsburgh', 'Columbus', 'Indianapolis', 'Chicago'], 1016), (['Syracuse', 'Buffalo', 'Cleveland', 'Columbus', 'Indianapolis', 'Chicago'], 841), (['Syracuse', 'Buffalo', 'Pittsburgh', 'Cleveland', 'Chicago'], 844), (['Syracuse', 'Buffalo', 'Pittsburgh', 'Cleveland', 'Detroit', 'Chicago'], 951), (['Syracuse', 'Buffalo', 'Pittsburgh', 'Cleveland', 'Columbus', 'Indianapolis', 'Chicago'], 1001), (['Syracuse', 'Buffalo', 'Pittsburgh', 'Columbus', 'Cleveland', 'Chicago'], 1039), (['Syracuse', 'Buffalo', 'Pittsburgh', 'Columbus', 'Cleveland', 'Detroit', 'Chicago'], 1146), (['Syracuse', 'Buffalo', 'Pittsburgh', 'Columbus', 'Indianapolis', 'Chicago'], 908), (['Syracuse', 'Boston', 'New York', 'Philadelphia', 'Baltimore', 'Pittsburgh', 'Cleveland', 'Chicago'], 1451), (['Syracuse', 'Boston', 'New York', 'Philadelphia', 'Baltimore', 'Pittsburgh', 'Cleveland', 'Detroit', 'Chicago'], 1558), (['Syracuse', 'Boston', 'New York', 'Philadelphia', 'Baltimore', 'Pittsburgh', 'Cleveland', 'Buffalo', 'Detroit', 'Chicago'], 1834), (['Syracuse', 'Boston', 'New York', 'Philadelphia', 'Baltimore', 'Pittsburgh', 'Cleveland', 'Columbus', 'Indianapolis', 'Chicago'], 1608), (['Syracuse', 'Boston', 'New York', 'Philadelphia', 'Baltimore', 'Pittsburgh', 'Buffalo', 'Detroit', 'Chicago'], 1726), (['Syracuse', 'Boston', 'New York', 'Philadelphia', 'Baltimore', 'Pittsburgh', 'Buffalo', 'Detroit', 'Cleveland', 'Chicago'], 1957), (['Syracuse', 'Boston', 'New York', 'Philadelphia', 'Baltimore', 'Pittsburgh', 'Buffalo', 'Detroit', 'Cleveland', 'Columbus', 'Indianapolis', 'Chicago'], 2114), (['Syracuse', 'Boston', 'New York', 'Philadelphia', 'Baltimore', 'Pittsburgh', 'Buffalo', 'Cleveland', 'Chicago'], 1721), (['Syracuse', 'Boston', 'New York', 'Philadelphia', 'Baltimore', 'Pittsburgh', 'Buffalo', 'Cleveland', 'Detroit', 'Chicago'], 1828), (['Syracuse', 'Boston', 'New York', 'Philadelphia', 'Baltimore', 'Pittsburgh', 'Buffalo', 'Cleveland', 'Columbus', 'Indianapolis', 'Chicago'], 1878), (['Syracuse', 'Boston', 'New York', 'Philadelphia', 'Baltimore', 'Pittsburgh', 'Columbus', 'Cleveland', 'Chicago'], 1646), (['Syracuse', 'Boston', 'New York', 'Philadelphia', 'Baltimore', 'Pittsburgh', 'Columbus', 'Cleveland', 'Detroit', 'Chicago'], 1753), (['Syracuse', 'Boston', 'New York', 'Philadelphia', 'Baltimore', 'Pittsburgh', 'Columbus', 'Cleveland', 'Buffalo', 'Detroit', 'Chicago'], 2029), (['Syracuse', 'Boston', 'New York', 'Philadelphia', 'Baltimore', 'Pittsburgh', 'Columbus', 'Indianapolis', 'Chicago'], 1515), (['Syracuse', 'Boston', 'New York', 'Philadelphia', 'Pittsburgh', 'Cleveland', 'Chicago'], 1408), (['Syracuse', 'Boston', 'New York', 'Philadelphia', 'Pittsburgh', 'Cleveland', 'Detroit', 'Chicago'], 1515), (['Syracuse', 'Boston', 'New York', 'Philadelphia', 'Pittsburgh', 'Cleveland', 'Buffalo', 'Detroit', 'Chicago'], 1791), (['Syracuse', 'Boston', 'New York', 'Philadelphia', 'Pittsburgh', 'Cleveland', 'Columbus', 'Indianapolis', 'Chicago'], 1565), (['Syracuse', 'Boston', 'New York', 'Philadelphia', 'Pittsburgh', 'Buffalo', 'Detroit', 'Chicago'], 1683), (['Syracuse', 'Boston', 'New York', 'Philadelphia', 'Pittsburgh', 'Buffalo', 'Detroit', 'Cleveland', 'Chicago'], 1914), (['Syracuse', 'Boston', 'New York', 'Philadelphia', 'Pittsburgh', 'Buffalo', 'Detroit', 'Cleveland', 'Columbus', 'Indianapolis', 'Chicago'], 2071), (['Syracuse', 'Boston', 'New York', 'Philadelphia', 'Pittsburgh', 'Buffalo', 'Cleveland', 'Chicago'], 1678), (['Syracuse', 'Boston', 'New York', 'Philadelphia', 'Pittsburgh', 'Buffalo', 'Cleveland', 'Detroit', 'Chicago'], 1785), (['Syracuse', 'Boston', 'New York', 'Philadelphia', 'Pittsburgh', 'Buffalo', 'Cleveland', 'Columbus', 'Indianapolis', 'Chicago'], 1835), (['Syracuse', 'Boston', 'New York', 'Philadelphia', 'Pittsburgh', 'Columbus', 'Cleveland', 'Chicago'], 1603), (['Syracuse', 'Boston', 'New York', 'Philadelphia', 'Pittsburgh', 'Columbus', 'Cleveland', 'Detroit', 'Chicago'], 1710), (['Syracuse', 'Boston', 'New York', 'Philadelphia', 'Pittsburgh', 'Columbus', 'Cleveland', 'Buffalo', 'Detroit', 'Chicago'], 1986), (['Syracuse', 'Boston', 'New York', 'Philadelphia', 'Pittsburgh', 'Columbus', 'Indianapolis', 'Chicago'], 1472), (['Syracuse', 'Boston', 'Providence', 'New York', 'Philadelphia', 'Baltimore', 'Pittsburgh', 'Cleveland', 'Chicago'], 1467), (['Syracuse', 'Boston', 'Providence', 'New York', 'Philadelphia', 'Baltimore', 'Pittsburgh', 'Cleveland', 'Detroit', 'Chicago'], 1574), (['Syracuse', 'Boston', 'Providence', 'New York', 'Philadelphia', 'Baltimore', 'Pittsburgh', 'Cleveland', 'Buffalo', 'Detroit', 'Chicago'], 1850), (['Syracuse', 'Boston', 'Providence', 'New York', 'Philadelphia', 'Baltimore', 'Pittsburgh', 'Cleveland', 'Columbus', 'Indianapolis', 'Chicago'], 1624), (['Syracuse', 'Boston', 'Providence', 'New York', 'Philadelphia', 'Baltimore', 'Pittsburgh', 'Buffalo', 'Detroit', 'Chicago'], 1742), (['Syracuse', 'Boston', 'Providence', 'New York', 'Philadelphia', 'Baltimore', 'Pittsburgh', 'Buffalo', 'Detroit', 'Cleveland', 'Chicago'], 1973), (['Syracuse', 'Boston', 'Providence', 'New York', 'Philadelphia', 'Baltimore', 'Pittsburgh', 'Buffalo', 'Detroit', 'Cleveland', 'Columbus', 'Indianapolis', 'Chicago'], 2130), (['Syracuse', 'Boston', 'Providence', 'New York', 'Philadelphia', 'Baltimore', 'Pittsburgh', 'Buffalo', 'Cleveland', 'Chicago'], 1737), (['Syracuse', 'Boston', 'Providence', 'New York', 'Philadelphia', 'Baltimore', 'Pittsburgh', 'Buffalo', 'Cleveland', 'Detroit', 'Chicago'], 1844), (['Syracuse', 'Boston', 'Providence', 'New York', 'Philadelphia', 'Baltimore', 'Pittsburgh', 'Buffalo', 'Cleveland', 'Columbus', 'Indianapolis', 'Chicago'], 1894), (['Syracuse', 'Boston', 'Providence', 'New York', 'Philadelphia', 'Baltimore', 'Pittsburgh', 'Columbus', 'Cleveland', 'Chicago'], 1662), (['Syracuse', 'Boston', 'Providence', 'New York', 'Philadelphia', 'Baltimore', 'Pittsburgh', 'Columbus', 'Cleveland', 'Detroit', 'Chicago'], 1769), (['Syracuse', 'Boston', 'Providence', 'New York', 'Philadelphia', 'Baltimore', 'Pittsburgh', 'Columbus', 'Cleveland', 'Buffalo', 'Detroit', 'Chicago'], 2045), (['Syracuse', 'Boston', 'Providence', 'New York', 'Philadelphia', 'Baltimore', 'Pittsburgh', 'Columbus', 'Indianapolis', 'Chicago'], 1531), (['Syracuse', 'Boston', 'Providence', 'New York', 'Philadelphia', 'Pittsburgh', 'Cleveland', 'Chicago'], 1424), (['Syracuse', 'Boston', 'Providence', 'New York', 'Philadelphia', 'Pittsburgh', 'Cleveland', 'Detroit', 'Chicago'], 1531), (['Syracuse', 'Boston', 'Providence', 'New York', 'Philadelphia', 'Pittsburgh', 'Cleveland', 'Buffalo', 'Detroit', 'Chicago'], 1807), (['Syracuse', 'Boston', 'Providence', 'New York', 'Philadelphia', 'Pittsburgh', 'Cleveland', 'Columbus', 'Indianapolis', 'Chicago'], 1581), (['Syracuse', 'Boston', 'Providence', 'New York', 'Philadelphia', 'Pittsburgh', 'Buffalo', 'Detroit', 'Chicago'], 1699), (['Syracuse', 'Boston', 'Providence', 'New York', 'Philadelphia', 'Pittsburgh', 'Buffalo', 'Detroit', 'Cleveland', 'Chicago'], 1930), (['Syracuse', 'Boston', 'Providence', 'New York', 'Philadelphia', 'Pittsburgh', 'Buffalo', 'Detroit', 'Cleveland', 'Columbus', 'Indianapolis', 'Chicago'], 2087), (['Syracuse', 'Boston', 'Providence', 'New York', 'Philadelphia', 'Pittsburgh', 'Buffalo', 'Cleveland', 'Chicago'], 1694), (['Syracuse', 'Boston', 'Providence', 'New York', 'Philadelphia', 'Pittsburgh', 'Buffalo', 'Cleveland', 'Detroit', 'Chicago'], 1801), (['Syracuse', 'Boston', 'Providence', 'New York', 'Philadelphia', 'Pittsburgh', 'Buffalo', 'Cleveland', 'Columbus', 'Indianapolis', 'Chicago'], 1851), (['Syracuse', 'Boston', 'Providence', 'New York', 'Philadelphia', 'Pittsburgh', 'Columbus', 'Cleveland', 'Chicago'], 1619), (['Syracuse', 'Boston', 'Providence', 'New York', 'Philadelphia', 'Pittsburgh', 'Columbus', 'Cleveland', 'Detroit', 'Chicago'], 1726), (['Syracuse', 'Boston', 'Providence', 'New York', 'Philadelphia', 'Pittsburgh', 'Columbus', 'Cleveland', 'Buffalo', 'Detroit', 'Chicago'], 2002), (['Syracuse', 'Boston', 'Providence', 'New York', 'Philadelphia', 'Pittsburgh', 'Columbus', 'Indianapolis', 'Chicago'], 1488), (['Syracuse', 'New York', 'Philadelphia', 'Baltimore', 'Pittsburgh', 'Cleveland', 'Chicago'], 1178), (['Syracuse', 'New York', 'Philadelphia', 'Baltimore', 'Pittsburgh', 'Cleveland', 'Detroit', 'Chicago'], 1285), (['Syracuse', 'New York', 'Philadelphia', 'Baltimore', 'Pittsburgh', 'Cleveland', 'Buffalo', 'Detroit', 'Chicago'], 1561), (['Syracuse', 'New York', 'Philadelphia', 'Baltimore', 'Pittsburgh', 'Cleveland', 'Columbus', 'Indianapolis', 'Chicago'], 1335), (['Syracuse', 'New York', 'Philadelphia', 'Baltimore', 'Pittsburgh', 'Buffalo', 'Detroit', 'Chicago'], 1453), (['Syracuse', 'New York', 'Philadelphia', 'Baltimore', 'Pittsburgh', 'Buffalo', 'Detroit', 'Cleveland', 'Chicago'], 1684), (['Syracuse', 'New York', 'Philadelphia', 'Baltimore', 'Pittsburgh', 'Buffalo', 'Detroit', 'Cleveland', 'Columbus', 'Indianapolis', 'Chicago'], 1841), (['Syracuse', 'New York', 'Philadelphia', 'Baltimore', 'Pittsburgh', 'Buffalo', 'Cleveland', 'Chicago'], 1448), (['Syracuse', 'New York', 'Philadelphia', 'Baltimore', 'Pittsburgh', 'Buffalo', 'Cleveland', 'Detroit', 'Chicago'], 1555), (['Syracuse', 'New York', 'Philadelphia', 'Baltimore', 'Pittsburgh', 'Buffalo', 'Cleveland', 'Columbus', 'Indianapolis', 'Chicago'], 1605), (['Syracuse', 'New York', 'Philadelphia', 'Baltimore', 'Pittsburgh', 'Columbus', 'Cleveland', 'Chicago'], 1373), (['Syracuse', 'New York', 'Philadelphia', 'Baltimore', 'Pittsburgh', 'Columbus', 'Cleveland', 'Detroit', 'Chicago'], 1480), (['Syracuse', 'New York', 'Philadelphia', 'Baltimore', 'Pittsburgh', 'Columbus', 'Cleveland', 'Buffalo', 'Detroit', 'Chicago'], 1756), (['Syracuse', 'New York', 'Philadelphia', 'Baltimore', 'Pittsburgh', 'Columbus', 'Indianapolis', 'Chicago'], 1242), (['Syracuse', 'New York', 'Philadelphia', 'Pittsburgh', 'Cleveland', 'Chicago'], 1135), (['Syracuse', 'New York', 'Philadelphia', 'Pittsburgh', 'Cleveland', 'Detroit', 'Chicago'], 1242), (['Syracuse', 'New York', 'Philadelphia', 'Pittsburgh', 'Cleveland', 'Buffalo', 'Detroit', 'Chicago'], 1518), (['Syracuse', 'New York', 'Philadelphia', 'Pittsburgh', 'Cleveland', 'Columbus', 'Indianapolis', 'Chicago'], 1292), (['Syracuse', 'New York', 'Philadelphia', 'Pittsburgh', 'Buffalo', 'Detroit', 'Chicago'], 1410), (['Syracuse', 'New York', 'Philadelphia', 'Pittsburgh', 'Buffalo', 'Detroit', 'Cleveland', 'Chicago'], 1641), (['Syracuse', 'New York', 'Philadelphia', 'Pittsburgh', 'Buffalo', 'Detroit', 'Cleveland', 'Columbus', 'Indianapolis', 'Chicago'], 1798), (['Syracuse', 'New York', 'Philadelphia', 'Pittsburgh', 'Buffalo', 'Cleveland', 'Chicago'], 1405), (['Syracuse', 'New York', 'Philadelphia', 'Pittsburgh', 'Buffalo', 'Cleveland', 'Detroit', 'Chicago'], 1512), (['Syracuse', 'New York', 'Philadelphia', 'Pittsburgh', 'Buffalo', 'Cleveland', 'Columbus', 'Indianapolis', 'Chicago'], 1562), (['Syracuse', 'New York', 'Philadelphia', 'Pittsburgh', 'Columbus', 'Cleveland', 'Chicago'], 1330), (['Syracuse', 'New York', 'Philadelphia', 'Pittsburgh', 'Columbus', 'Cleveland', 'Detroit', 'Chicago'], 1437), (['Syracuse', 'New York', 'Philadelphia', 'Pittsburgh', 'Columbus', 'Cleveland', 'Buffalo', 'Detroit', 'Chicago'], 1713), (['Syracuse', 'New York', 'Philadelphia', 'Pittsburgh', 'Columbus', 'Indianapolis', 'Chicago'], 1199), (['Syracuse', 'Pittsburgh', 'Cleveland', 'Chicago'], 732), (['Syracuse', 'Pittsburgh', 'Cleveland', 'Detroit', 'Chicago'], 839), (['Syracuse', 'Pittsburgh', 'Cleveland', 'Buffalo', 'Detroit', 'Chicago'], 1115), (['Syracuse', 'Pittsburgh', 'Cleveland', 'Columbus', 'Indianapolis', 'Chicago'], 889), (['Syracuse', 'Pittsburgh', 'Buffalo', 'Detroit', 'Chicago'], 1007), (['Syracuse', 'Pittsburgh', 'Buffalo', 'Detroit', 'Cleveland', 'Chicago'], 1238), (['Syracuse', 'Pittsburgh', 'Buffalo', 'Detroit', 'Cleveland', 'Columbus', 'Indianapolis', 'Chicago'], 1395), (['Syracuse', 'Pittsburgh', 'Buffalo', 'Cleveland', 'Chicago'], 1002), (['Syracuse', 'Pittsburgh', 'Buffalo', 'Cleveland', 'Detroit', 'Chicago'], 1109), (['Syracuse', 'Pittsburgh', 'Buffalo', 'Cleveland', 'Columbus', 'Indianapolis', 'Chicago'], 1159), (['Syracuse', 'Pittsburgh', 'Columbus', 'Cleveland', 'Chicago'], 927), (['Syracuse', 'Pittsburgh', 'Columbus', 'Cleveland', 'Detroit', 'Chicago'], 1034), (['Syracuse', 'Pittsburgh', 'Columbus', 'Cleveland', 'Buffalo', 'Detroit', 'Chicago'], 1310), (['Syracuse', 'Pittsburgh', 'Columbus', 'Indianapolis', 'Chicago'], 796)]

