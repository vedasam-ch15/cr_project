from modules import *
arr1 = np.array([[1,2,3,4],[2,3,4,5],[3,4,5,6],[4,5,6,7]])
arr2 = np.array([[4,5,6,7],[3,4,5,6],[2,3,4,5],[1,2,3,4]])

print (arr1)
print(arr2)

def patchify(arr1,arr2, size, n):
    l = []
    for i in range(size//n):
        for j in range(size//n):
            img_arr = arr1[i*n:(i+1)*n, j*n:(j+1)*n]
            mask_arr = arr2[i*n:(i+1)*n, j*n:(j+1)*n]
            if np.dot(img_arr, mask_arr).sum():
                l.append(img_arr)

    return l

l = patchify(arr1,arr2, 4, 2)
for i in l:
    print (i)