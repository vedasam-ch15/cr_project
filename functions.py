from modules import *


def cr(img_array, size_arr, size_patch):
    l = []
    
    for i in range(size_arr//size_patch):
        for j in range(size_arr//size_patch):

            img_patch = img_array[0][i*size_patch:(i+1)*size_patch, j*size_patch:(j+1)*size_patch]
            mask_patch = img_array[1][i*size_patch:(i+1)*size_patch, j*size_patch:(j+1)*size_patch]
            ign_patch = img_array[2][i*size_patch:(i+1)*size_patch, j*size_patch:(j+1)*size_patch]
            if (np.any(mask_patch) and not np.any(ign_patch)) :
                l.append(img_patch)

    return l



def non_cr(img_array, size_arr, size_patch):
    l = []
    
    for i in range(size_arr//size_patch):
        for j in range(size_arr//size_patch):

            img_patch = img_array[0][i*size_patch:(i+1)*size_patch, j*size_patch:(j+1)*size_patch]
            mask_patch = img_array[1][i*size_patch:(i+1)*size_patch, j*size_patch:(j+1)*size_patch]
            ign_patch = img_array[2][i*size_patch:(i+1)*size_patch, j*size_patch:(j+1)*size_patch]
            if (not np.any(mask_patch) or (np.any(mask_patch) and np.any(ign_patch))):
                l.append(img_patch)

    return l