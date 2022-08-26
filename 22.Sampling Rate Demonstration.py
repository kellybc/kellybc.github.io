import matplotlib.pyplot as plt
import numpy as np

# start and end time to inspect
t_start = 0
t_end = 1

# signal frequency, in the real world this would be unknown
signal_frequency = 10 # Hz

# time and value series of the signal
t = np.linspace(t_start, t_end, 100 * signal_frequency)
S = np.sin(2 * np.pi * signal_frequency * t)

# The inital sampling frequency
sample_frequency = 0 # Hz

# declare x and y values for the data acquisition (DAQ)
x = []
y = []

# define function that will update the x and y values of the DAQ
def update_DAQ_data(f):
    global x
    global y
    x = np.arange(t_start, t_end + 1 / f, 1 / f)
    y = np.sin(2 * np.pi * signal_frequency * x)

# turn on interactive mode
plt.ion()

# create plot and set title, x and y axis label, and add horizontal line
fig, ax = plt.subplots(1, 1)
ax.set_title(str(signal_frequency) + 'Hz Signal Analysis')
ax.set_xlabel('Time (s)')
ax.set_ylabel('Signal Value')
ax.axhline(y = 0, color = 'k')

# add signal data to plot
ax.plot(t, S, 'r-', label = 'Signal (in real world, unknown frequency)')

# add DAQ data to plot and create handle for series
dataPlot, = ax.plot(x, y, 'bo-', label = 'DAQ')

# set the x and y axis limits
ax.set_xlim(t_start, t_end)
ax.set_ylim(-1.2, 1.2)

# define function that handles user keystroke inputs
def user_input(event):
    global sample_frequency
    global x
    global y
    
    # if q or exscape is pressed close the plot
    if event.key in ['q', 'escape']:
        plt.close('all')
    else:
        # if right or down arrow is pressed
        if event.key in ['right', 'down']:
            # add one to the sampling frequency
            sample_frequency += 1
        
        # if left or up arrow is pressed
        elif event.key in ['left', 'up']:
            # subtract one from the sampling frequency if the frequency is
            # greater than 1 (avoids having a zero or negative frequency)
            if sample_frequency > 1:
                sample_frequency -= 1
        
        # if p or plus sign is pressed
        elif event.key in ['p', '+']:
            # add 0.1 to the sampling frequency
            sample_frequency += 0.1
        
        # if m or minus sign is pressed
        elif event.key in ['m', '-']:
            # substract 0.1 from the sampling frequency if the frequency is
            # greater than 0.1 (avoids having a zero or negative frequency)
            if sample_frequency > 0.1:
                sample_frequency -= 0.1
        
        if sample_frequency > 0:
            # update the DAQ data with the new sampling frequency
            update_DAQ_data(sample_frequency)
        
            # set the x and y data of the DAQ series on the plot
            dataPlot.set_xdata(x)
            dataPlot.set_ydata(y)
            
            # update the legend to indicate the sampling frequency
            dataPlot.set_label('DAQ ({:.1f}Hz)'.format(sample_frequency))
            
            # draw the legend
            plt.legend(loc = 'upper right')
            
            # put slight pause so script won't hang up
            plt.pause(0.1)

# add legend to plot
plt.legend(loc = 'upper right')

# draw plot
plt.draw()

# bind userInput function to key press event
# this essentially enables the use of user input
fig.canvas.mpl_connect('key_press_event', user_input)