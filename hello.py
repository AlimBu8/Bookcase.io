print("_____== = Algorithme d'Euclide = ==_____")

a, b = int(input("a [espace] b: "))

if a//b > 0:
  q = a//b
  while q > 0:
    q= q//b
    if q>=0:
      print(f"q = {q} > 0, dans ce cas oncontinu")
try:
  if b== 0: 
    print("impossible")
except: 
  pass

message =f"""  Voila ce qu'on a fait : 
   Soient (a= {a} , b= {b}) € NxN*.
   Si {a}//{b} == {q}, et {q}>0:
     tantque ({q}>0): 
       {q}={q}//{b}
     fintantque
   finsi

"""
print(message)
