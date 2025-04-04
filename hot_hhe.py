import heapq

class priorityQueue:

    def __init__(self):
        self.cities = []

    def push(self, city, cost):
        heapq.heappush(self.cities, (cost, city))

    def pop(self):
        return heapq.heappop(self.cities)[1]

    def isEmpty(self):
        return len(self.cities) == 0

    def check(self):
        print(self.cities)

class ctNode:
    def __init__(self, city, distance):
        self.city = str(city)
        self.distance = str(distance)

romania = {}

def makedict():
    file = open(r"D:\hicheel\AI\lab_3\romania.txt", 'r')
    for string in file:
        line = string.split(',')
        ct1 = line[0]
        ct2 = line[1]
        dist = int(line[2])
        romania.setdefault(ct1, []).append(ctNode(ct2, dist))
        romania.setdefault(ct2, []).append(ctNode(ct1, dist))


def makehuristikdict():
    h = {}
    with open(r"C:\hackathon\romania_sld.txt", 'r') as file:
        for line in file:
            line = line.strip().split(",")
            node = line[0].strip()
            sld = int(line[1].strip())
            h[node] = sld
    return h


def heuristic(node, values):
    return values[node]

def astar(start, end):
    path = {}
    distance = {}
    q = priorityQueue()
    h = makehuristikdict()

    q.push(start, 0)
    distance[start] = 0
    path[start] = None
    expandedList = []

    while not q.isEmpty():
        current = q.pop()
        expandedList.append(current)

        if current == end:
            break

        for new in romania[current]:
            g_cost = distance[current] + int(new.distance)

            if new.city not in distance or g_cost < distance[new.city]:
                distance[new.city] = g_cost
                f_cost = g_cost + heuristic(new.city, h)
                q.push(new.city, f_cost)
                path[new.city] = current
    printoutput(start, end, path, distance, expandedList)

def printoutput(start, end, path, distance, expandedlist):
    finalpath = []
    i = end

    while path.get(i) is not None:
        finalpath.append(i)
        i = path[i]
    finalpath.append(start)
    finalpath.reverse()

    print("TIIMEE BI CHADLAAA")
    print(f"{start} => {end}")
    print("Hamgiin bogino zam: " + str(finalpath))
    print("Hamgiin bogino zamiin urt : " + str(len(finalpath)))
    print("Zardal : " + str(distance[end]))

def main():
    src = "Arad"
    dst = "Bucharest"
    makedict()
    astar(src, dst)

if __name__ == "__main__":
    main()
