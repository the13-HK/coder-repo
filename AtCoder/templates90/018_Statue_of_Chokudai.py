import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()
readline = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)
import math

T = II()
L,X,Y = MI()
def angle(x,y,z):
    leng_X = X-x
    leng_Y = Y-y
    XY = (leng_X**2+leng_Y**2)**(1/2)
    radian = math.atan2(z,XY)
    print(math.degrees(radian))
    
Q = II()
for q in range(Q):
    E = II()
    degree = 360*E/T#�x���@
    theta = math.radians(degree)#�x���@����ʓx�@�ɕϊ�
    y,z = -L/2*math.sin(theta),L/2 -L/2*math.cos(theta)#�ϗ��Ԃ̈ʒu�����߂�
    angle(0,y,z)