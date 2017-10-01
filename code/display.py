"""
All plotting and animation functions for anylizing and visualizing the spread
of disease.
"""
import thinkplot

def plot_all_time_steps(infection_data):
    # thinkplot.preplot()
    thinkplot.plot(range(len(infection_data)), infection_data, color='gray')
    # thinkplot.config(xlabel='time', ylabel='rho', xlim=[0, len(infection_data)], ylim=[0.0, 1.0])

def plot():
    pass

def animation():
    pass
