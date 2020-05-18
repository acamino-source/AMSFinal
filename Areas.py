from rp import * #pip install rp

resolution=1000
size=1.5
grid=np.linspace(-size,size,resolution)+1j*np.expand_dims(np.linspace(-size,size,resolution),1)
x=grid.real
y=grid.imag
Θ=np.angle(grid)
r=np.abs(grid)

def area_of(matrix):
	#Given a binary matrix calculate the area that we see in it, adjusted for resolution and size
	return np.sum(matrix)/resolution**2*size**2

heart=np.abs(x)**2+(y-np.abs(x)**(2/3))**2<=1/2
cv_imshow(heart)

clover=r<=np.abs(np.sin(2*Θ))
cv_imshow(clover)

def rotated_clover(angle=0):
	return r<=np.abs(np.sin(2*(Θ+angle)))
