# -*- encoding:utf-8 -*-
'''

 A --> B
 A --> C
 B --> C
 B --> D
 C --> D
 D --> C
 E --> F
 F --> C

'''


def find_path(graph, start, end, path=[]):
        '寻找一条路径'
        path = path + [start]
        if start == end:
            return path
        if not start in graph.keys():
            return None
        for node in graph[start]:
            if node not in path:
                newpath = find_path(graph, node, end, path)
                if newpath:  # 看是否有下一个节点，此节点能否接通
                    return newpath
        return path

def find_all_paths(graph, start, end, path=[]):
        '查找所有的路径'
        path = path + [start]
        if start == end:
            return [path]
        if not start in graph.keys():
            return []
        paths = []  # 存储所有路径
        g = graph[start]
        for node in g:
            print('node', node)
            if node not in path:
                # print('node_not_in_path', node)
                newpaths = find_all_paths(graph, node, end, path)
                print('newpaths', newpaths)
                for newpath in newpaths:
                    print('newpath', newpath)
                    paths.append(newpath)
                    print('paths', paths)
        return paths

def find_shortest_path(graph, start, end, path=[]):
        '查找最短路径'
        path = path + [start]
        if start == end:
            return path
        if not start in graph.keys():
            return None
        shortest = None
        for node in graph[start]:
            if node not in path:
                newpath = find_shortest_path(graph, node, end, path)
                if newpath:
                    if not shortest or len(newpath) < len(shortest):
                        shortest = newpath
        return shortest

# test

if __name__ == '__main__':
    graph = {'A': ['B', 'C'],
             'B': ['C', 'D'],
             'C': ['D'],
             'D': ['C'],
             'E': ['F'],
             'F': ['C']}
    print (find_path(graph,'A','D'))
    print('------------------------------------------------------')
    print (find_all_paths(graph,'A','D'))
    print('------------------------------------------------------')
    print (find_shortest_path(graph,'A','D'))
