import os 

def createifnotexists(folder):
    if not os.path.exists(folder):
        os.mkdir(folder)
def move(foldername,files):
    for file in files:
        os.replace(file,f'{foldername}/{file}')
files=os.listdir()
print(files)

createifnotexists('Images')
createifnotexists('Docs')
createifnotexists('Media')
imgext=['.png','.jpg','.jpeg']
doctext=['.xlsx','.csv','.pdf','.py']
medfile=['.mp4','.mp3','.mkv','.3gp']
images= [file for file in files if os.path.splitext(file)[1].lower() in imgext]
docs=[file for file in files if os.path.splitext(file)[1].lower() in doctext]
med=[file for file in files if os.path.splitext(file)[1].lower() in medfile]

print('documents ',docs)
print('images ',images)
print('media',med)

for media in med:
    os.replace(media,'Media')
move('Images',images)
move('Docs',docs)
move('Media',med)