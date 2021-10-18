import matplotlib.pyplot as plt 
 
# Make a new plot (XKCD style)  
fig = plt.xkcd() 
 
# Add points as scatters - scatter(x, y, size, color) 
# zorder determines the drawing order, set to 3 to make the  
# grid lines appear behind the scatter points  
plt.scatter(0, 0, s=50, color=”red”, zorder=3)  
plt.scatter(0, 1, s=50, color=”red”, zorder=3)  
plt.scatter(1, 0, s=50, color=”red”, zorder=3)  
plt.scatter(1, 1, s=50, color=”green”, zorder=3) 
 
# Set the axis limits  
plt.xlim(-2, 2) 
plt.ylim(-2, 2) 
 
# Label the plot  
plt.xlabel(”Input 1”) 
plt.ylabel(”Input 2”) 
plt.title(”State Space of Input Vector”) 
 
# Turn on grid lines 
plt.grid(True, linewidth=1, linestyle=’:’) 
 
# Autosize (stops the labels getting cut off)  
plt.tight_layout() 
 
# Show the plot  
plt.show() 