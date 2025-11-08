from collections import deque

ROMANIA_MAP = {
    'Oradea': ['Zerind', 'Sibiu'],
    'Zerind': ['Oradea', 'Arad'],
    'Arad': ['Zerind', 'Sibiu', 'Timisoara'],
    'Timisoara': ['Arad', 'Lugoj'],
    'Lugoj': ['Timisoara', 'Mehadia'],
    'Mehadia': ['Lugoj', 'Drobeta'],
    'Drobeta': ['Mehadia', 'Craiova'],
    'Craiova': ['Drobeta', 'Rimnicu Vilcea', 'Pitesti'],
    'Sibiu': ['Oradea', 'Arad', 'Fagaras', 'Rimnicu Vilcea'],
    'Rimnicu Vilcea': ['Sibiu', 'Craiova', 'Pitesti'],
    'Fagaras': ['Sibiu', 'Bucharest'],
    'Pitesti': ['Rimnicu Vilcea', 'Craiova', 'Bucharest'],
    'Bucharest': ['Fagaras', 'Pitesti', 'Giurgiu', 'Urziceni'],
    'Giurgiu': ['Bucharest'],
    'Urziceni': ['Bucharest', 'Hirsova', 'Vaslui'],
    'Hirsova': ['Urziceni', 'Eforie'],
    'Eforie': ['Hirsova'],
    'Vaslui': ['Urziceni', 'Iasi'],
    'Iasi': ['Vaslui', 'Neamt'],
    'Neamt': ['Iasi']
}

def P1_route(start, goal):
    """
    หาเส้นทางใดก็ได้จาก start ไป goal โดยใช้ BFS [cite: 294]
    """
    if start == goal:
      return start
      
    # Queue เก็บ (city, path_list)
    queue = deque([(start, [start])])
    visited = set()
    
    while queue:
      current_city, path = queue.popleft()
      
      if current_city in visited:
        continue
      
      visited.add(current_city)
    
      # ตรวจสอบเพื่อนบ้าน
      for neighbor in ROMANIA_MAP.get(current_city, []):
        if neighbor == goal :
          # เจอแล้ว
          return " ".join(path + [goal])
        
        if neighbor not in visited:
          new_path = list(path)
          new_path.append(neighbor)
          queue.append((neighbor, new_path))
    
    return "No route found" # กรณีหาไม่เจอ

# --- Example run [cite: 308-318] ---
if __name__ == '__main__':
  print(P1_route("Arad", "Bucharest"))