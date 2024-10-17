import tkinter as tk
from tkinter import messagebox
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
def coin():
    cointosstime= int(Entry.get())

    except ValueError as e:
    messagebox.showerror("error,error")
    return

    result= np.random.choice(["khat","Shir"], size=cointosstime)

    khat_count= np.sum(result== "Khat")
    shir_count= np.sum(result== "Shir")

    prob_khat= khat_count / cointosstime
    prob_shir= shir_count / cointosstime

    result_label.config(text=f"Shir:{shir_count}\n khat:{khat_count}")

    pro_label.config(text=f"")

    
