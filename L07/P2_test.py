from P2 import P2_route
import os 

#file_path = os.path.join(os.path.dirname(__file__), "P2romania.txt")
# print(file_path)
if __name__ == '__main__':
    r = P2_route('P2romania.txt', 'Arad', 'Bucharest')
    print(r)