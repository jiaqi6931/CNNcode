import numpy as np
from numpy import linalg as LA
import re
import os
import inspect
import copy
import math

def partialshuffle(inp,n):
    out= copy.deepcopy(inp)
    if n>0:
        #randomly selects n position in the list
        indexes=list(range(len(inp)))
        np.random.shuffle(indexes)
        args=indexes[:n]
        #defines copy of input and 
        c = copy.deepcopy(args)
        #generate target position by shuffling copy of args
        np.random.shuffle(c)
        for i in range(len(args)):
            out[args[i]]=inp[c[i]]
    
    return out

def f(h,th,g):
    if (h-th)>0:
        return g*(h-th)
    else:
        return 0.0


def Kgauss2D(r_i,r_j,sigma,cutoff):
        if np.abs(r_i[0]-r_j[0])<0.5:
            dx=np.abs(r_i[0]-r_j[0])
        else:
            dx=1-np.abs(r_i[0]-r_j[0])
            
        if np.abs(r_i[1]-r_j[1])<0.5:
            dy=np.abs(r_i[1]-r_j[1])
        else:
            dy=1-np.abs(r_i[1]-r_j[1])
        
        d=np.sqrt(pow(dx,2)+pow(dy,2))
        
        if d<=cutoff:
            out=(1.0/(np.sqrt(2*math.pi))*sigma)*np.exp(-(pow(d,2)/(2*pow(sigma,2))))
        else:
            out=0    
        return out
    
def positive_mean(v,th):
    return np.mean([x-th for x in v if x-th>0])
    
def fix_parameters(V,h,g,h0,a,a2,b,tolerance,maxiter):
    fixed=False
    it=0
    while (not fixed) and it<maxiter:
        h0=h0+b*((pow(np.mean(V),2)/float(np.mean(pow(V,2))))-a2)
        V=np.asarray(list(map(lambda h: f(h,h0,g),h)))
        fixed=(np.abs(((pow(np.mean(V),2)/float(np.mean(pow(V,2))))-a2))/a2 <= tolerance)
        it=it+1
    if it>=maxiter:
        print("fixing failed")
    
    return h0

def overlap(matA,matB):
        m=np.multiply(matA,matB).sum()
        m=m/float(LA.norm(matA)*LA.norm(matB))
        return m

def save_parameters(simulation_name,N,ksigma,kcut,a,sparsity,Nuncorr,eta,gamma,timesteps,normalization):
    f= open(simulation_name+"/parameters.txt","w+")
    f.writelines("N: "+str(N)+"\n")
    f.writelines("ksigma: "+str(ksigma)+"\n")
    f.writelines("kcut: "+str(kcut)+"\n")
    f.writelines("a: "+str(a)+"\n")
    f.writelines("sparsity: "+str(sparsity)+"\n")
    f.writelines("Nuncorr: "+str(Nuncorr)+"\n")
    f.writelines("eta: "+str(eta)+"\n")
    f.writelines("gamma: "+str(gamma)+"\n")
    f.writelines("timesteps: "+str(timesteps)+"\n")
    f.writelines("normalization: "+str(normalization)+"\n")
    f.close() 
    return
    
def save_parametersRC(simulation_name,N,ksigma,kcut,a,sparsity,Nuncorr,eta,timesteps,t1,s,normalization):
    f= open(simulation_name+"/parameters.txt","w+")
    f.writelines("N: "+str(N)+"\n")
    f.writelines("ksigma: "+str(ksigma)+"\n")
    f.writelines("kcut: "+str(kcut)+"\n")
    f.writelines("a: "+str(a)+"\n")
    f.writelines("sparsity: "+str(sparsity)+"\n")
    f.writelines("Nuncorr: "+str(Nuncorr)+"\n")
    f.writelines("eta: "+str(eta)+"\n")
    f.writelines("s: "+str(s)+"\n")
    f.writelines("timesteps: "+str(timesteps)+"\n")
    f.writelines("t1: "+str(t1)+"\n")
    f.writelines("normalization: "+str(normalization)+"\n")
    f.close() 
    return