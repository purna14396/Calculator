
import math
while(True):
    def Calculator():
        if(choice=="+"):
            n1=float(input("enter the n1 :"))
            n2=float(input("enter the n2 :"))
            print(n1+n2)
        elif(choice=="-"):
            n1=float(input("enter the n1 :"))
            n2=float(input("enter the n2 :"))
            if(n1>n2):
                print(n1-n2)
                
            elif(n1<n2):
                print(f"-{n2-n1}")  
        elif(choice=="*"):
            n1=float(input("enter the n1 :"))
            n2=float(input("enter the n2 :"))
            print(n1*n2)
        elif(choice=="/"):
            n1=float(input("enter the n1 :"))
            n2=float(input("enter the n2 :"))
            if(n2 != 0):
                print(n1/n2)   
            elif(n2 == 0):
                print("Zero division error  and can't find value !!")
        elif(choice=="//"):
            n1=float(input("enter the n1 :"))
            n2=float(input("enter the n2 :"))
            if(n2 != 0):
                print(n1//n2)
            elif(n2 == 0):
                print("Zero division error  and can't find value !!")    
        elif(choice=="%"):
            n1=float(input("enter the n1 :"))
            n2=float(input("enter the n2 :"))
            if(n2 != 0):
                print(n1%n2)
                
            elif(n2 == 0):
                print("Zero division error  and can't find value !!")    
        elif(choice=="s"):
            n=float(input("enter the num : "))
            result=n**(1/2)
            print(f"squareroot of  num {n} is {result}")   
        elif(choice=="c"):
            n=float(input("enter the num : "))
            result=n**(1/3)
            print(f"Cuberoot of  num {n} is {result}")            
        elif(choice=="^"):
            n1=float(input("enter the num : "))
            n2=float(input("enter the power : "))
            print(f"{n1} power {n2} is {pow(n1,n2)}")            
        elif(choice=="sin"):
            n=eval(input("Enter the angle :"))
            result=math.sin(math.radians(n))
            print(f"sin({n}) = {round(result,3)} ")            
        elif(choice=="cosec"):
            n=eval(input("Enter the angle :"))
            x=math.sin(math.radians(n))
            result= 1 / x
            print(f"cosec({n}) = {round(result,3)} ")            
        elif(choice=="cos"):
            n=eval(input("Enter the angle :"))
            result=math.cos(math.radians(n))
            print(f"cos({n}) = {round(result,3)} ")            
        elif(choice=="tan"):
            n=eval(input("Enter the angle :"))
            result=math.tan(math.radians(n))
            print(f"tan({n}) = {round(result,3)} ")            
        elif(choice=="cot"):
            n=eval(input("Enter the angle :"))
            x=math.tan(math.radians(n))
            result= 1 / x
            print(f"cot({n}) = {round(result,3)} ")            
        elif(choice=="sec"):
            n=eval(input("Enter the angle :"))
            x=math.cos(math.radians(n))
            result= 1 / x
            print(f"sec({n}) = {round(result,3)} ")            
        elif(choice=="asec"):
            n=eval(input("Enter the value :"))
            x=math.acos(n)
            result= 1 / x
            print(f"secINV({n}) = {result} ")           
        elif(choice=="acosec"):
            n=eval(input("Enter the value :"))
            x=math.asin(n)
            result= 1 / x
            print(f"cosecINV({n}) = {result} ")            
        elif(choice=="acot"):
            n=eval(input("Enter the value :"))
            x=math.atan(n)
            result= 1 / x
            print(f"cotINV({n}) = {result} ")            
        elif(choice=="atan"):
            n=eval(input("Enter the value :"))
            result=math.atan(n)
            print(f"tanINV({n}) = {result} ")            
        elif(choice=="asin"):
            n=eval(input("Enter the value :"))
            result=math.asin(n)
            print(f"sinINV({n}) = {result} ")            
        elif(choice=="acos"):
            n=eval(input("Enter the value :"))
            result=math.acos(n)
            print(f"cosINV({n}) = {result} ")            
        else:
            print("please enter the valid input and operator !")
    choice = str(input("enter the command in {+,-,*,/,//,%,^,square_root=s,cube_root=c,sin,cos,tan,sec,cosec,cot,asin,acos,atan,assec,acosec,acot}  : "))
    Calculator()