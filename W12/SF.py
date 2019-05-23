'''
二叉树的遍历，有深度优先遍历和广度优先遍历，深度优先遍历又有先序、中序、后续遍历，广度优先遍历就是按层遍历。
'''

import time

import numpy as np 
from matplotlib import pyplot as plt

class Node(object):
	"""初始化一个节点,需要为节点设置值"""

	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None


class BinaryTree(object):
	"""
	创建二叉树,完成
	- 添加元素
	- 广度遍历
	- 深度遍历(先序遍历, 中序遍历, 后序遍历)
	"""

	def __init__(self):
		self.root = None
		pass

	# 添加元素
	def addNode(self, val):
		# 创建队列结构存储结点
		nodeStack = [self.root, ]

		# 如果根结点为空
		if self.root == None:
			self.root = Node(val)
			#print("添加根节点{0}成功!".format(self.root.val))
			return

		while len(nodeStack) > 0:
			# 队列元素出列
			p_node = nodeStack.pop()

			# 如果左子结点为空
			if p_node.left == None:
				p_node.left = Node(val)
				#print("添加左:{0} ".format(p_node.left.val))
				return

			# 如果右子节点为空
			if p_node.right == None:
				p_node.right = Node(val)
				#print("添加右:{0} ".format(p_node.right.val))
				return

			nodeStack.insert(0, p_node.left)
			nodeStack.insert(0, p_node.right)

	# 广度遍历(中序: 先读父节点,再读左子节点, 右子节点)
	def breadthFirst(self):
		nodeStack = [self.root, ]

		while len(nodeStack) > 0:
			my_node = nodeStack.pop()
			#print("-->", my_node.val)

			if my_node.left is not None:
				nodeStack.insert(0, my_node.left)

			if my_node.right is not None:
				nodeStack.insert(0, my_node.right)

	# 深度优先(先序遍历)

	def preorder(self, start_node):
		if start_node == None:
			return

		#print(start_node.val)
		self.preorder(start_node.left)
		self.preorder(start_node.right)

	# 深度优先(中序遍历)

	def inorder(self, start_node):
		if start_node == None:
			return

		self.inorder(start_node.left)
		#print(start_node.val)
		self.inorder(start_node.right)

	# 深度优先(后序遍历)
	def outorder(self, start_node):
		if start_node == None:
			return
		self.outorder(start_node.left)
		self.outorder(start_node.right)
		#print(start_node.val)

def ergodic_binarytree(NN):
	i = 0
	bt = BinaryTree()	#New binary tree object
	while i <= NN:
		bt.addNode(i)
		i+=1
	start = time.perf_counter()
	bt.breadthFirst()
	end = time.perf_counter()
	print('广度遍历-->用时:')
	we = end - start
	print(we)
	start = time.perf_counter()
	bt.preorder(bt.root)
	end = time.perf_counter()
	print('深度优先先序遍历-->用时:')
	dfe = end - start
	print(dfe)
	start = time.perf_counter()
	bt.inorder(bt.root)
	end = time.perf_counter()
	print('深度优先中序遍历-->用时:')
	dme = end - start
	print(dme)
	start = time.perf_counter()
	bt.outorder(bt.root)
	end = time.perf_counter()
	print('深度优先后序遍历-->用时:')
	dle = end - start
	print(dle)

	return we,dfe,dme,dle 


'''def draw(xlist, ylist):
	x = np.arange(xlist) 
	y = np.arange(ylist)
	plt.title("Matplotlib demo") 
	plt.xlabel("x axis caption") 
	plt.ylabel("y axis caption") 
	plt.plot(x,y)
	plt.show()'''

def main():
	#From 1000 To 10000 Skip 1000
	NodeNumList, TimeList = [], []
	y1, y2, y3, y4 = [], [] ,[] ,[]
	for NodeNum in range(100, 10000, 100) :
		'''
		print('当节点个数为：'+ str(NodeNum))
		print(ergodic_binarytree(NodeNum))
		'''
		NodeNumList.append(NodeNum)
		TimeList.append(ergodic_binarytree(NodeNum))
	'''
	print(NodeNumList)
	print(TimeList)
	'''
	for TL in TimeList:
		y1.append(TL[0])
		y2.append(TL[1])
		y3.append(TL[2])
		y4.append(TL[3])
	x = np.array(NodeNumList) 
	y1 = np.array(y1)
	f1 = np.polyfit(x, y1, 2)
	p1 = np.poly1d(f1)
	print(p1)
	yvals1 = p1(x)

	y2 = np.array(y2)
	f2 = np.polyfit(x, y2, 2)
	p2 = np.poly1d(f2)
	print(p2)
	yvals2 = p2(x)

	y3 = np.array(y3)
	f3 = np.polyfit(x, y3, 2)
	p3 = np.poly1d(f3)
	print(p3)
	yvals3 = p3(x)

	y4 = np.array(y4)
	f4 = np.polyfit(x, y4, 2)
	p4 = np.poly1d(f4)
	print(p4)
	yvals4 = p4(x)

	plt.title("Matplotlib demo") 
	plt.xlabel("x axis caption") 
	plt.ylabel("y axis caption")
	plt.plot(x,y1, 's') 
	plt.plot(x,yvals1)
	plt.plot(x,y2, 's')
	plt.plot(x,yvals2)
	plt.plot(x,y3, 's')
	plt.plot(x,yvals3)
	plt.plot(x,y4, 's')
	plt.plot(x,yvals4)
	plt.show()

if __name__ == '__main__':
    main() 
