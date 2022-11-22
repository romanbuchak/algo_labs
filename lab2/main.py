def readMatrixFromFile(fileName: str):
    file = open(fileName)
    lines = file.readlines()
    Graph = []
    for line in lines:
        Graph.append(parseLine(line))
    file.close()
    return Graph

def parseLine(line: str):
    arr = []
    elements = line.split()
    for element in elements:
        arr.append(int(element))
    return arr


Graph = readMatrixFromFile("input.txt")


def activateMine():
    amountRows = len(Graph)
    if amountRows > 0:
        amountColumns = len(Graph[0])
    returnedGraph = []
    for rowIndex in range(amountRows):
        returnedGraph.append(list(Graph[rowIndex]))

    for rowIndex in range(amountRows):
        for elIndex in range(amountColumns):
            if Graph[rowIndex][elIndex] == 0:
                iStart = rowIndex - 1
                iEnd = rowIndex + 2
                jStart = elIndex - 1
                jEnd = elIndex + 2
                if iStart < 0:
                    iStart = 0
                if iEnd > amountRows:
                    iEnd = amountRows
                if jStart < 0:
                    jStart = 0
                if jEnd > amountColumns:
                    jEnd = amountColumns
                for i in range(iStart, iEnd):
                    for j in range(jStart, jEnd):
                        returnedGraph[i][j] = 0

    return returnedGraph

class GraphNode:
    def __init__(self, row, column):
        self.row = row
        self.column = column

    def getRow(self):
        return self.row

    def getColumn(self):
        return self.column

    def __hash__(self):
        return hash((self.row, self.column))

    def __eq__(self, other):
        return (self.row, self.column) == (other.row, other.column)

    def __ne__(self, other):
        return not (self == other)


def BFS(startNode: GraphNode, endNode: GraphNode):  # function for BFS
    graphRows = len(Graph)
    if graphRows == 0:
        return -1
    else:
        graphColumns = len(Graph[0])

    if Graph[startNode.getRow()][
        startNode.column] == 0 or startNode.getRow() > graphRows - 1 or startNode.getColumn() > graphColumns - 1:
        return -1
    visited = dict()
    for i in range(graphRows):
        visited[i] = list()
    visited[startNode.getRow()].append(startNode.getColumn())
    queue = [startNode]
    pathValue = dict()
    pathValue[startNode] = 0

    while len(queue) > 0:
        curNode = queue.pop(0)
        curCol = curNode.column
        curRow = curNode.row
        curPathValue = pathValue[curNode]
        if curNode == endNode:
            return pathValue[curNode]
        if curCol < graphColumns - 1 and Graph[curRow][curCol + 1] != 0 and ((curCol + 1) not in visited[curRow]):   #right
            newNode = GraphNode(curRow, curCol + 1)
            queue.append(newNode)
            visited[curRow].append(curCol + 1)
            pathValue[newNode] = curPathValue + 1
        if curRow > 0 and Graph[curRow - 1][curCol] != 0 and (curCol not in visited[curRow - 1]):   #up
            newNode = GraphNode(curRow - 1, curCol)
            queue.append(newNode)
            visited[curRow - 1].append(curCol)
            pathValue[newNode] = curPathValue + 1
        if curRow < graphRows - 1 and Graph[curRow + 1][curCol] != 0 and (curCol not in visited[curRow + 1]):   #down
            newNode = GraphNode(curRow + 1, curCol)
            queue.append(newNode)
            visited[curRow + 1].append(curCol)
            pathValue[newNode] = curPathValue + 1
        if curCol > 0 and Graph[curRow][curCol - 1] != 0 and ((curCol - 1) not in visited[curRow]):  #left
            newNode = GraphNode(curRow, curCol - 1)
            queue.append(newNode)
            visited[curRow].append(curCol - 1)
            pathValue[newNode] = curPathValue + 1

    return pathValue[endNode] if (endNode.column in visited[endNode.row]) else -1


ret = BFS(GraphNode(2, 0), GraphNode(0, 9))
file = open("output.txt", "a")
file.write(str(ret) + " ")
file.close()