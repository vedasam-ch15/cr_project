from modules import *
from functions import *

img_array = np.load('C:\\vscode\cr_project\\files\\2_1.npy')

cr_patches = cr(img_array, 256, 11)
print(len(cr_patches))

non_cr_patches = non_cr(img_array, 256, 11)
print(len(non_cr_patches))


for i in range(len(cr_patches)):
    plt.subplot(8,8, i+1)
    
    plt.imshow(cr_patches[i], vmin = 10, vmax = 200,cmap = 'gray' )
    
    plt.axis('off')

plt.show()
plt.savefig('C:\\vscode\cr_project\images\cr_patches.png')  
plt.close()

for i in range(len(non_cr_patches)):
    plt.subplot(22,22, i+1)
    
    plt.imshow(non_cr_patches[i], vmin = 10, vmax = 200, cmap = 'gray' )
    
    plt.axis('off')
plt.show()
plt.savefig('C:\\vscode\cr_project\images\\noncr_patches.png')  
plt.close()




    

