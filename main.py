def getMatrix():
	data=[]
	
	with open("./mat1.txt","r") as matrix_file:
		mat=matrix_file.read()	#read the file

		lignes=mat.split("\n") #parse line by line

		for case in lignes:	#parse each line
			elem=case.split(" ")
			data.append(elem)

	matrix_file.close()
	
	return(data)


class graph:
	
	def __init__(self):

		self.verticesList=[] #List of the vertex of the graph
		self.neighboursList=[] #List of the neighbours, composed by list of list.

		self.levels = []

		self.levelContent = []
		self.levelsNeighbours = []

		pass


	""" Fuction creating the graph by using the data received by getMatrix"""
	def createGraph(self,matrix):
		
		"""We read the number of vertices in the graph"""
		length = int(matrix[0][0])
		Line = 1 #Variable that parse the line of the matrix

		while Line <= length:
			self.verticesList.append(Line)

			tempNeighbours = [] #Represent the neighbours of one vertex.
			Column = 0 #variable that parse the column of the matrix
			
			while Column < length:
				if int(matrix[Line][Column]) == 1:
					tempNeighbours.append(Column+1)
				Column = Column + 1

			self.neighboursList.append(tempNeighbours)	
			Line = Line + 1

		
		pass

	def tarjan(self):
		seenVertices=[]
		lowestIndex = []
		stack=[]
		def parcours(vertex):
			seenVertices.append(vertex)
			lowestIndex.append(seenVertices.index(vertex))
			stack.append(vertex)

			for neighbour in self.neighboursList[vertex-1]:
				if not neighbour in seenVertices:
					parcours(neighbour)
					lowestIndex[seenVertices.index(vertex)] = min(lowestIndex[seenVertices.index(vertex)],lowestIndex[seenVertices.index(neighbour)])
				elif neighbour in stack:
					lowestIndex[seenVertices.index(vertex)] = min(lowestIndex[seenVertices.index(vertex)],seenVertices.index(neighbour))

			if seenVertices.index(vertex) == lowestIndex[seenVertices.index(vertex)]:
				tempStronglyConnectedComponent = []
				
				if not stack == []:
					newComponent = stack.pop()

					while newComponent != vertex:
						tempStronglyConnectedComponent.append(newComponent)
						if not stack ==[]:
							newComponent = stack.pop()

					tempStronglyConnectedComponent.append(newComponent)
					tempStronglyConnectedComponent.sort()
					self.levelContent.append(tempStronglyConnectedComponent)
					
			pass
		
		for vertex in self.verticesList:
			if not (vertex) in seenVertices:
				parcours(vertex)

		
		pass

	def levelMatrix(self):

		for boucleLevel in self.levelContent:
			lineMatrix = []
			connectedLevels = []
			self.levels.append(self.levelContent.index(boucleLevel)+1)
			
			for levElem in boucleLevel:
				for boucleNeighbours in self.neighboursList[levElem-1]:
					for otherLevel in self.levelContent:
						if not boucleLevel == otherLevel:
							if boucleNeighbours in otherLevel:
								connectedLevels.append(self.levelContent.index(otherLevel)+1)


			i=1
			temp=[]
			while i <= len(self.levelContent):
				lineMatrix.append(connectedLevels.count(i))
				if not connectedLevels.count(i) == 0:
					temp = i

				i=i+1
			self.levelsNeighbours.append(temp)
			print(lineMatrix)
		pass	


if __name__ == "__main__":
	
	"""Recuperation of the text file"""
	dataFile = getMatrix()

	"""Creation of the graph and assignation of the vertex and neighbours"""
	
	dataGraph = graph()
	dataGraph.createGraph(dataFile)
	print(" ")
	print("The graph is")
	print(dataGraph.verticesList)
	print(dataGraph.neighboursList)
	print(" ")
	dataGraph.tarjan()

	

	print("Adjacency matrix of the levels ")
	dataGraph.levelMatrix()

	print(" ")
	print("List of levels :")
	print(" ")
	print(dataGraph.levels)
	print(" ")
	print("Content of each levels : ")
	print(" ")
	print(dataGraph.levelContent)
	print(" ")

	

	