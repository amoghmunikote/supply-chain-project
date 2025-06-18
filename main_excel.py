import pandas as pd
import numpy as np
from scipy.optimize import linprog

dist = pd.read_excel('Data - Distances.xlsx', sheet_name='Sheet1')
distri = pd.read_excel('Data - Distributors - A.xlsx', sheet_name='Sheet1')
proc = pd.read_excel('Data - Processors - B.xlsx', sheet_name='Sheet1')
supp = pd.read_excel('Data - Suppliers - A.xlsx', sheet_name='Sheet1')
prmc = pd.read_excel('Data - Product Raw Material Components.xlsx', sheet_name='Sheet1')
ship = pd.read_excel('Data - Shipping Costs.xlsx', sheet_name='Sheet1')