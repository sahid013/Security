import math

m=12345567
a=16
k=5
alpha=10
N= 656692050181897513638241554199181923922955921760928836766304161790553989228223793461834703506872747071705167995972707253940099469869516422893633357693
phi=(N-1)
bita=pow(alpha,a,N)
y1=pow(alpha,k,N)

k_inverse=pow(k,-1,phi)
#signing
y2=(k_inverse*(m-(y1*a)))%phi
i1=pow(bita,y1,N)
i2=pow(y1,y2,N)
i=i1*i2
print('y1=',y1)
print('y2=',y2)
#verification
v=i%N
w=pow(alpha,m,N)
print('v=',v)
print('w=',w)
if(v==w):
    print('verified')
else:
    print('not verified')