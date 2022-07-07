from modules import *
from functions import *

img_array = np.load('2_1.npy')

cr_patches = cr(img_array, 256, 11)
print(len(cr_patches))

non_cr_patches = non_cr(img_array, 256, 11)
print(len(non_cr_patches))


for i in range(len(cr_patches)):
    plt.subplot(10,11, i+1)
    
    plt.imshow(cr_patches[i], vmin = 0, vmax = 255,cmap = 'gray' )
    
    plt.axis('off')

plt.show()
plt.savefig('C:\\vscode\cr_project\image_and_mask\cr_patches.png')  
plt.close()

for i in range(len(non_cr_patches)):
    plt.subplot(21,21, i+1)
    
    plt.imshow(non_cr_patches[i], vmin = 0, vmax = 255, cmap = 'gray' )
    
    plt.axis('off')
plt.show()
plt.savefig('C:\\vscode\cr_project\image_and_mask\\noncr_patches.png')  
plt.close()




    

