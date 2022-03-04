import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
mpl.rc('text', usetex=True)


file = 'NameFile.txt'
output = 'figure.png'
dados =  np.loadtxt(file,dtype = float, delimiter= ",")
x0 = np.linspace(-2.0,2.0,1000)
y0 = np.linspace(-2.0,2.0,1000)

palette = 'Spectral_r'
fig, ax = plt.subplots(figsize=(8, 6))
figure = plt.imshow(dados, cmap = palette, extent = [x0.min(),x0.max(), y0.min(), y0.max()], interpolation ='gaussian', origin ='lower')
plt.colorbar(figure)
plt.xlabel('$x_0$', fontsize = 20)
plt.ylabel('$\dot{x}_0$', fontsize = 20)
plt.xticks(fontsize= 20)
plt.yticks(fontsize= 20)
plt.savefig(output)