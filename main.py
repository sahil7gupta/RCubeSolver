import copy
def rubik(i_state):
  list_o=[[],[]]
  list_k=[]
  j=[]
  k=0
  for i in range(len(i_state)):
    def rc_do(rc_state):
      new_state=rc_state
      temp=new_state[0][1]
      new_state[0][1]=new_state[5][1]
      new_state[5][1]=new_state[2][1]
      new_state[2][1]=new_state[4][1]
      new_state[4][1]=temp
      
      temp=new_state[0][3]
      new_state[0][3]=new_state[5][3]
      new_state[5][3]=new_state[2][3]
      new_state[2][3]=new_state[4][3]
      new_state[4][3]=temp
      
      temp=new_state[1][0]
      new_state[1][0]=new_state[1][2]
      new_state[1][2]=new_state[1][3]
      new_state[1][3]=new_state[1][1]
      new_state[1][1]=temp
      return new_state
    def ra_do(ra_state):
      new_state=ra_state
      temp=new_state[0][1]
      new_state[0][1]=new_state[4][1]
      new_state[4][1]=new_state[2][1]
      new_state[2][1]=new_state[5][1]
      new_state[5][1]=temp
      
      temp=new_state[0][3]
      new_state[0][3]=new_state[4][3]
      new_state[4][3]=new_state[2][3]
      new_state[2][3]=new_state[5][3]
      new_state[5][3]=temp
      
      temp=new_state[1][0]
      new_state[1][0]=new_state[1][1]
      new_state[1][1]=new_state[1][3]
      new_state[1][3]=new_state[1][2]
      new_state[1][2]=temp
      
      return new_state
    def dc_do(dc_state):
      new_state=dc_state
      temp=new_state[0][2]
      new_state[0][2]=new_state[3][2]
      new_state[3][2]=new_state[2][1]
      new_state[2][1]=new_state[1][2]
      new_state[1][2]=temp
        
      temp=new_state[0][3]
      new_state[0][3]=new_state[3][3]
      new_state[3][3]=new_state[2][0]
      new_state[2][0]=new_state[1][3]
      new_state[1][3]=temp
      
      temp=new_state[5][0]
      new_state[5][0]=new_state[5][2]
      new_state[5][2]=new_state[5][3]
      new_state[5][3]=new_state[5][1]
      new_state[5][1]=temp
      
      return new_state
    def da_do(da_state):
      new_state=da_state
      temp=new_state[0][2]
      new_state[0][2]=new_state[1][2]
      new_state[1][2]=new_state[2][1]
      new_state[2][1]=new_state[3][2]
      new_state[3][2]=temp
      
      
      temp=new_state[0][3]
      new_state[0][3]=new_state[1][3]
      new_state[1][3]=new_state[2][0]
      new_state[2][0]=new_state[3][3]
      new_state[3][3]=temp
      
      temp=new_state[5][0]
      new_state[5][0]=new_state[5][1]
      new_state[5][1]=new_state[5][3]
      new_state[5][3]=new_state[5][2]
      new_state[5][2]=temp
      
      return new_state
    def bc_do(bc_state):
      new_state=bc_state
      temp=new_state[4][0]
      new_state[4][0]=new_state[1][1]
      new_state[1][1]=new_state[5][3]
      new_state[5][3]=new_state[3][2]
      new_state[3][2]=temp
      
      temp=new_state[4][1]
      new_state[4][1]=new_state[1][3]
      new_state[1][3]=new_state[5][2]
      new_state[5][2]=new_state[3][0]
      new_state[3][0]=temp
      
      temp=new_state[2][0]
      new_state[2][0]=new_state[2][2]
      new_state[2][2]=new_state[2][3]
      new_state[2][3]=new_state[2][1]
      new_state[2][1]=temp
      
      return new_state
    def ba_do(ba_state):
      new_state=ba_state
      temp=new_state[4][0]
      new_state[4][0]=new_state[3][2]
      new_state[3][2]=new_state[5][3]
      new_state[5][3]=new_state[1][1]
      new_state[1][1]=temp
  
      temp=new_state[4][1]
      new_state[4][1]=new_state[3][0]
      new_state[3][0]=new_state[5][2]
      new_state[5][2]=new_state[1][3]
      new_state[1][3]=temp
      
      temp=new_state[2][0]
      new_state[2][0]=new_state[2][1]
      new_state[2][1]=new_state[2][3]
      new_state[2][3]=new_state[2][2]
      new_state[2][2]=temp
      
      return new_state

    def make_list_o(i,j):
      rc_state=copy.deepcopy(i_state[i])
      rc=rc_do(rc_state)
      if rc not in list_o[0] and rc!=i_state[i]:
        list_o[0].append(rc)
        j.append(["rc",i])

      ra_state=copy.deepcopy(i_state[i])
      ra=ra_do(ra_state)
      if ra not in list_o[0] and ra!=i_state[i]:
        list_o[0].append(ra)
        j.append(["ra",i])
        
      dc_state=copy.deepcopy(i_state[i])
      dc=dc_do(dc_state)
      if dc not in list_o[0] and dc!=i_state[i]:
        list_o[0].append(dc)
        j.append(["dc",i])
        
      da_state=copy.deepcopy(i_state[i])
      da=da_do(da_state)
      if da not in list_o[0] and da!=i_state[i]:
        list_o[0].append(da)
        j.append(["da",i])
        
      bc_state=copy.deepcopy(i_state[i])
      bc=bc_do(bc_state)
      if bc not in list_o[0] and bc!=i_state[i]:
        list_o[0].append(bc)
        j.append(["bc",i])
        
      ba_state=copy.deepcopy(i_state[i])
      ba=ba_do(ba_state)
      if ba not in list_o[0] and ba!=i_state[i]:
        list_o[0].append(ba)
        j.append(["ba",i])

      return j
    j=make_list_o(i,j)
    
    if [[1,1,1,1],[2,2,2,2],[3,3,3,3],[4,4,4,4],[5,5,5,5],[6,6,6,6]] in list_o[0]:
      print j[list_o[0].index([[1,1,1,1],[2,2,2,2],[3,3,3,3],[4,4,4,4],[5,5,5,5],[6,6,6,6]])][0]
      list_o[1]=j[list_o[0].index([[1,1,1,1],[2,2,2,2],[3,3,3,3],[4,4,4,4],[5,5,5,5],[6,6,6,6]])][1]
      return list_o
    
  list_k.append(list_o[0])
  m=rubik(list_o[0])
  list_k=list_k+[m[0]]
  print j[m[1]][0]
  return [list_k,j[m[1]][1]]
  
inp_state=input("Enter input state:")
#Example of input=[[[1,3,2,2],[5,2,1,5],[4,4,4,1],[6,4,6,6],[1,6,5,2],[3,5,3,3]]]
print ""
print "Do the following from bottom to top: "
states=rubik(inp_state)
print ""