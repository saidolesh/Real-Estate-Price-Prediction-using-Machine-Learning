import numpy as np

def gradientdescent(x,y):
    m_current=b_current=0;
    for i in range(1000):
        y_predicted=m_current*x+b_current;