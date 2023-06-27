import os

imagens = []
os.chdir(os.path.join('data', 'valid'))
for filename in os.listdir(os.getcwd()):
    if filename.endswith('.jpg'):
        imagens.append('data/valid/' + filename)
os.chdir('..')

with open('test.txt', 'w') as outfile:
    for img in imagens:
        outfile.write(img)
        outfile.write('\n')
    outfile.close()
os.chdir('..')
