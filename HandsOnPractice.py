import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#Carrega os dados
ddos_database = pd.read_csv("/run/media/aktsu_user/Mem_linux/Databases/01-12/Syn.csv", low_memory=False)
print(ddos_database.info())
