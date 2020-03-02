#!/usr/bin/python3.7

import dataReader as reader

AList = reader.readDataFromFile("testData.json")

AList = AList.exportToAdajcencyMatrix().exportToIncidenceMatrix().prettyPrint()
