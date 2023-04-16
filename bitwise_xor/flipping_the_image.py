# flip and invert the image

def flip_and_invert_image(image):

    # first reverse the image according to the rows -- we have flipped the image
    ''' for i in image:
            i.reverse()'''
    # we can use list comprehension as well here
    image = [i[::-1] for i in image]
    #print(image)


    # now we have invert the rows, to do this we are going to xor with 1
    # using list comprehension 
    '''image = [[j^1 for j in i] for i in image]'''
    
    # without list comprehension 
    for i in range(len(image)):
        for j in range(len(image[i])):
            image[i][j] = image[i][j] ^ 1 
    return image
if __name__=="__main__":

    image = [[1,1,0],[1,0,1],[0,0,0]]
    print(flip_and_invert_image(image))