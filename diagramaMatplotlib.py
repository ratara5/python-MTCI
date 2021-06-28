#Importar el módulo de pyplot y la librería de matplotlib
import matplotlib.pyplot as plt
#Crear la fugura con sus ejes
fig, ax = plt.subplots()
#Dibujar los puntos
ax.scatter(x=[1,2,3], y=[3,2,1])
#Guargar el gráfico en formato png
plt.savefig('Diagrama1.png')
#Mostrar el gráfico
plt.show()


#Otr
import matplotlib.pyplot as plt
fig, ax = plt.subplots()
ax.scatter([1,2,3,4],[1,2,0,0.5])
plt.savefig('Diagrama2.png')
plt.show()

#Otr
import matplotlib.pyplot as plt
fig, ax = plt.subplots()
ax.plot([1,2,3,4],[1,2,0,0.5])
plt.savefig('Diagrama3.png')
plt.show()

#Otr
import matplotlib.pyplot as plt
fig, ax = plt.subplots()
ax.fill_between([1,2,3,4],[1,2,0,0.5])
plt.savefig('Diagrama4.png')
plt.show()

#La 11
import matplotlib.pyplot as plt
import numpy as np
fig, ax = plt.subplots()
x = np.linspace(-3.0,3.0,100)
y = np.linspace(-3.0,3.0,100)
x,y = np.meshgrid(x,y)
z = np.sqrt(x**2 + 2*y**2)
ax.contourf(x,y,z)
plt.savefig('Diagrama11')
plt.show()

#La 12
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()
x = np.random.random((16,16))
ax.imshow(x)
plt.savefig('Diagrama12')
plt.show()

#13
import matplotlib.pyplot as plt
import numpy as np
fig, ax = plt.subplots()
x,y = np.random.multivariate_normal(mean=[0.0,0.0], cov=[[1.0, 0.4], [0.4,1.0]], size= 1000).T
ax.hist2d(x,y)
plt.show()


