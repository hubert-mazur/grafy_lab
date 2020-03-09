#!/usr/bin/python3.7
from tasks import dataReader as reader

print('# adjacencyList to others')

aList = reader.readDataFromFile("examples/testData1.json")
aList.prettyPrint()

aMatrix = aList.exportToAdjacencyMatrix()
aMatrix.prettyPrint()

aIndiceMatrix = aList.exportToIncidenceMatrix()
aIndiceMatrix.prettyPrint()

print('#adjacencyMatrix to others')

aMatrix2 = reader.readDataFromFile("examples/testData2.json")
aMatrix2.prettyPrint()

aList2 = aMatrix2.exportToAdjacencyList()
aList2.prettyPrint()

aIndiceMatrix2 = aMatrix2.exportToIncidenceMatrix()
aIndiceMatrix2.prettyPrint()

print('#incidenceMatrix to others')

aIndiceMatrix3 = reader.readDataFromFile("examples/testData3.json")
aIndiceMatrix3.prettyPrint()

aMatrix3 = aIndiceMatrix3.exportToAdjacencyMatrix()
aMatrix3.prettyPrint()

aList3 = aIndiceMatrix3.exportToAdjacencyList()
aList3.prettyPrint()
