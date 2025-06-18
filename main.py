import pandas as pd
import numpy as np
from scipy.optimize import linprog

aluminumSuppliers = ['PA', 'MM', 'EM']
thermoplasticSuppliers = ['PA', 'MM', 'EM']
pcbSuppliers = ['PA', 'MM', 'EM']
motorSuppliers = ['PA', 'MM', 'EM']
processors = ['WA', 'TGM', 'EF']
distributors = ['NeB', 'TS', 'PS']
products = ['who', 'what', 'thing']
materials = ['AL','TP', 'PCB', 'M']

#Supply costs
supply_costs_al = pd.DataFrame(
    data={m: [2.58, 2.91, 3.15] for m in materials},
    index=aluminumSuppliers
)
supply_costs_tp = pd.DataFrame(
    data={m: [6.53, 8.93, 10.21] for m in materials},
    index=aluminumSuppliers
)
supply_costs_pcb = pd.DataFrame(
    data={m: [1.43, 1.02, 1.61] for m in materials},
    index=aluminumSuppliers
)
supply_costs_m = pd.DataFrame(
    data={m: [0.85, 1.25, 1.05] for m in materials},
    index=aluminumSuppliers
)

#Supplier limits
supply_cap_m = pd.DataFrame(
    data={m: [0.85, 1.25, 1.05] for m in materials},
    index=aluminumSuppliers
)
supply_cap_m = pd.DataFrame(
    data={m: [0.85, 1.25, 1.05] for m in materials},
    index=aluminumSuppliers
)
supply_cap_m = pd.DataFrame(
    data={m: [0.85, 1.25, 1.05] for m in materials},
    index=aluminumSuppliers
)
supply_cap_m = pd.DataFrame(
    data={m: [0.85, 1.25, 1.05] for m in materials},
    index=aluminumSuppliers
)