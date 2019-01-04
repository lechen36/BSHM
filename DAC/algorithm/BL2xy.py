import math
def BL2xy(B,L,F):
    B=B*math.pi/180
    l=(L-F)*math.pi/180
    a=6378137
    b=6356752.3142451795  #84椭球短半轴半径   	
    e1=math.sqrt(pow(a,2)-pow(b,2))/a  #84椭球第一偏心率    	
    e2=math.sqrt(pow(a,2)-pow(b,2))/b  #84椭球的第二偏心率    	 
    N=a/math.sqrt(1-pow(e1,2)*pow(math.sin(B),2))	
    t=math.tan(B)
    h=e2*math.cos(B)
    A0=a*(1-pow(e1,2))*(1+3/4*pow(e1,2)+45/64*pow(e1,4)+350/512*pow(e1,6)+11025/16384*pow(e1,8))
    B0=-0.5*a*(1-pow(e1,2))*(3/4*pow(e1,2)+60/64*pow(e1,4)+525/512*pow(e1,6)+17640/16384*pow(e1,8))
    C0=0.25*a*(1-pow(e1,2))*(15/64*pow(e1,4)+210/512*pow(e1,6)+8820/16384*pow(e1,8))
    D0=-1/6*a*(1-pow(e1,2))*(35/512*pow(e1,6)+2520/16384*pow(e1,8))
    E0= 1/8*a*(1-pow(e1,2))*(315/16384*pow(e1,8))
    a1 =N*math.cos(B)
    #a2=(N*math.sin(B)*math.cos(B))/2
    a3=(N*(pow(math.cos(B),3)*(1-pow(t,2)+pow(h,2))))/6
    #a4=(N*math.sin(B)*(pow(math.cos(B),3)*(5-pow(t,2)+9*pow(h,2)+4*pow(h,4))))/24
    a5=(N*(pow(math.cos(B),5)*(5-18*pow(t,2)+pow(t,4)+14*pow(h,2)-58*pow(h,2)*pow(t,2))))/120
    #a6=(N*math.sin(B)*(pow(math.cos(B),5)*(61-58*pow(t,2)+pow(t,4))))/720
    Fx=B0*math.sin(2*B)+C0*math.sin(4*B)+D0*math.sin(6*B)+E0*math.sin(8*B)
    f1=(1/24)*(5-pow(t,2)+9*pow(h,2)+4*pow(h,4))
    f2=(61-58*pow(t,2)+pow(t,4))/720
    m=l*math.cos(B)
    Fxl=N*t*((1/2+(f1+f2*pow(m,2))*pow(m,2))*pow(m,2))	
    Fyl=a3*pow(l,3)+a5*pow(l,5)	
    x=A0*B+Fx+Fxl
    y=a1*l+Fyl
    
    return x,y
























