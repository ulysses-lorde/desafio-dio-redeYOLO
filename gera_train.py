import os

imagens = []
os.chdir(os.path.join('data', 'obj'))
for filename in os.listdir(os.getcwd()):
    if filename.endswith('.jpg'):
        imagens.append('data/obj/' + filename)
os.chdir('..')

with open('train.txt', 'w') as outfile:
    for img in imagens:
        outfile.write(img)
        outfile.write('\n')
    outfile.close()
os.chdir('..')
