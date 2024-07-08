basic_operations = 0

def BFS(maze, start, end):
    '''"Brute-Force Search"
    :param maze(list): 탐색할 미로
    :param start(tuple): 시작 좌표 (행, 열)
    :param end(tuple): 끝 좌표 (행, 열)
    :return: 시작점에서 끝점까지의 최단 경로 길이
    '''
    queue = [start]  # BFS 탐색을 위한 큐, 시작점 추가
    visited = set()  # 방문한 노드를 추적하기 위한 집합

    while len(queue) != 0:
        if queue[0] == start:
            # 시작점은 따로 처리, 큐에서 제거하여 경로로 저장
            path = [queue.pop(0)]
        else:
            path = queue.pop(0)  # 큐에서 경로를 하나 꺼냄
        front = path[-1]  # 현재 경로의 마지막 노드를 가져옴
        if front == end:
            return len(path)  # 도착점에 도달하면 경로의 길이를 반환
        elif front not in visited:
            for adjacentSpace in getAdjacentSpaces(maze, front, visited):
                newPath = list(path)  # 새로운 경로 생성
                newPath.append(adjacentSpace)  # 인접 노드를 새로운 경로에 추가
                queue.append(newPath)  # 새로운 경로를 큐에 추가
                global basic_operations
                basic_operations += 1  # 기본 연산 횟수를 증가
            visited.add(front)  # 현재 노드를 방문한 노드에 추가
    return 0  # 경로를 찾지 못한 경우 0을 반환


def getAdjacentSpaces(maze, space, visited):
    ''' 인접한 모든 합법적인 공간을 반환
    :param space: 현재 공간의 좌표 (행, 열)을 포함하는 튜플
    :return: 모든 합법적인 공간
    '''
    spaces = list()
    spaces.append((space[0]-1, space[1]))  # 위쪽 공간
    spaces.append((space[0]+1, space[1]))  # 아래쪽 공간
    spaces.append((space[0], space[1]-1))  # 왼쪽 공간
    spaces.append((space[0], space[1]+1))  # 오른쪽 공간

    final = list()
    for i in spaces:
        # 미로에서 1이 아닌 공간과 방문하지 않은 공간만 선택
        if maze[i[0]][i[1]] != 1 and i not in visited:
            final.append(i)
    return final  # 합법적인 공간 리스트 반환
