
import sys
 
def conversion(number,type,ch):
  if type==ch:
    print("choose different! can't be converted to same type!")
    return "choose different! can't be converted to same type!"
    
    
  if type=="h":
    n=str(number)
  else:
    n=int(number)
  
  def t_b(n):
    binary=""
    while(n!=0):
      r=int(n%2)
      binary=binary+str(r)
      n=int(n/2)
    return binary[::-1]


  def t_h(n):
    hexa=""
    d={"10":"A","11":"B","12":"C","13":"D","14":"E","15":"F"}
    while(n!=0):
      r=int(n%16)
      if str(r) in d:r=d[str(r)]
      hexa=hexa+str(r)
      n=int(n/16)
    return hexa[::-1]


  def t_o(n):
    oct=""
    while(n!=0):
      r=int(n%8)
      oct=oct+str(r)
      n=int(n/8)
    return oct[::-1]


  def to_d(n):
    if type=="b":
      base=2
    if type=="h":
      d={"10":"A","11":"B","12":"C","13":"D","14":"E","15":"F"}
      for key, value in d.items():
          if value in str(n):
              n=str(n).replace(value,key+" ")
      
      base=16
    if type=="o":
      base=8
    k=0
    decimal=0
    hw=""
    st=""
    for i in str(n)[::-1]:
      if type=="h":
        if i!=" ":
         hw=hw+i
        st=st+hw
      decimal=decimal+pow(base,k)*int(i)
      k=k+1
    return decimal


  if type=="d":
    if ch=="b":
        print(t_b(n))
        
        return t_b(n)
        
    if ch=="h":
      print(t_h(n))
      return t_h(n)
    
    if ch=="o":
      print(t_o(n))
      return t_o(n)
    
  if ch=="d":
    print(to_d(n))
    return to_d(n)
      
  if type=="b" or type=="h" or type=="o" and ch!="d":
    r=to_d(n)
    if ch=="b":
        print(t_b(r))
        return t_b(r)
        
    if ch=="h":
      print(t_h(r))
      return t_h(r)
        
    if ch=="o":
      print(t_o(r))
      return t_o(r)
            
