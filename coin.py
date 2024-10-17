import tkinter as tk
from tkinter import messagebox
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def coin():
    try:
       cointosstime = int(entry.get())
    except ValueError as e:
      messagebox.showerror("error,error")
      return

    result = np.random.choice(["Khat", "Shir"], size=cointosstime)

    khat_count= np.sum(result == "Khat")
    shir_count= np.sum(result == "Shir")

    prob_khat = khat_count / cointosstime
    prob_shir = shir_count / cointosstime

    result_label.config(text=f"Shir:{shir_count}\nkhat:{khat_count}")

    pro_label.config(text=f"prob of the shir:{prob_shir:.2f}\nprob of the khat:{prob_khat:.2f}")

    fig, ax= plt.subplots()
    ax.bar(["Shir", "Khat"], [shir_count, khat_count], color=['blue', 'orange'])
    canvas= FigureCanvasTkAgg(fig,master=window)
    canvas.draw()
    canvas.get_tk_widget().pack()

def close_window():
  window.destroy()


window = tk.Tk()
window.title("coin")
window.geometry("400x500")

lal=tk.Label(text="tedad partabe seke")
lal.pack()
entry=tk.Entry(window)
entry.pack()

btn=tk.Button(window,text="Start",command=coin)
btn.pack()
btn2=tk.Button(window, text="exit", command=close_window)
btn2.pack()


result_label=(tk.Label(text=""))
result_label.pack()

pro_label=(tk.Label(text=""))
pro_label.pack()

window.mainloop()

    
