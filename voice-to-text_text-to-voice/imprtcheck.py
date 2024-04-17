from emotion_image_new import essential

def avaj(): 
    if (essential() == 'Male'):
        avaj = "nova"
        return avaj
    if (essential() == 'Female'):
        avaj = "echo"
        return avaj
    


print(avaj())