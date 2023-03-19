from collections import deque

def bfs(maze, start, end):
    # Definimos una cola para almacenar las celdas a visitar
    queue = deque([start])
    
    # Definimos un diccionario para almacenar las celdas visitadas
    visited = {start: None}
    
    # Mientras haya celdas por visitar
    while queue:
        # Sacamos la primera celda de la cola
        current = queue.popleft()
        
        # Si llegamos a la celda de salida, terminamos la búsqueda
        if current == end:
            break
        
        # Para cada celda adyacente no visitada, la añadimos a la cola y marcamos como visitada
        row, col = current
        for neighbor in [(row+1, col), (row-1, col), (row, col+1), (row, col-1)]:
            if neighbor in maze and neighbor not in visited:
                queue.append(neighbor)
                visited[neighbor] = current
    
    # Reconstruimos el camino desde la celda de salida hasta la de inicio
    path = []
    while current != start:
        path.append(current)
        current = visited[current]
    path.append(start)
    path.reverse()
    
    # Devolvemos el camino y el número de pasos necesarios
    return path, len(path)-1
