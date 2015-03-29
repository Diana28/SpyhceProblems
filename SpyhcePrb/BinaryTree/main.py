'''
Created on Mar 29, 2015

@author: Diana User
''' 
   
def main():
    # the given tree represented as a list
    myTree = [50, # ROOT
                [17, # LEFT
                    [12,
                        [ 9, [], []],
                        [14, [], []],
                    ],
                    [23,
                        [19, [], []],
                        [],
                    ],
                ],
                [72, # RIGHT
                    [54,
                        [],
                        [67, [], []],
                    ],
                    [76,
                        [],
                        [],
                    ],
                ]
             ]

    result = [] # nodes we search
    
    # ask the user for the interval he wants
    x1 = input("Give the first node: ");
    x2 = input ("Give the second node: ")
    
    inOrderTraversal(result, x1, x2, myTree)
       
    if len(result) == 0:
        print("Sorry!") # no nodes in the specified interval
    else:
        print("The nodes you are looking for are: ")
        print (result)
 
"""
    The function which will traverse the tree in order, building a sorted list of nodes, from which we select
the ones in the [x1,x2] interval
"""          
def inOrderTraversal(result, x1, x2, tree):
  
    if tree[1] != []:
        inOrderTraversal(result, x1, x2, tree[1])          

    if tree[0] >= x1 and tree[0] <= x2:
        result.append(tree[0]);
    
    if tree[2] != []:
        inOrderTraversal(result, x1, x2, tree[2])   
            
main()