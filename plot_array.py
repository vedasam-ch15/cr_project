from functions import *

'''numpy array of the image (3,256,256)'''
img_array = np.load('2_1.npy')
#print(img_array)

print(img_array.shape)
print(img_array[0].shape) #image
print(img_array[1].shape) #mask
print(img_array[2].shape)

#image
plt.imshow(img_array[0], vmin = 0, vmax = 255,cmap = 'gray' )
plt.savefig('image.png',bbox_inches='tight')  
plt.show() 
plt.close()

#mask
plt.imshow(img_array[1], vmin = 0, vmax = 255,cmap = 'gray' )
plt.savefig('mask.png',bbox_inches='tight')  
plt.show() 
plt.close()

#forget

