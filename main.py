import os

def createIfNotExist(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)


def move(foldername, files):
    for file in files:
        os.replace(file, f'{foldername}/{file}')

files = os.listdir()
files.remove('main.py')
print(files)

createIfNotExist('Images')
createIfNotExist('Media')
createIfNotExist('Docs')
createIfNotExist('CSV')
createIfNotExist('Others')


imgexts = ['.png', '.jpg', '.jpeg']
images = [file for file in files if os.path.splitext(file)[1].lower() in imgexts]

docExts = ['.txt', '.docx', '.doc', '.pdf']
docs = [file for file in files if os.path.splitext(file)[1].lower() in docExts]

mediaExts = ['.mp4', '.mp3', '.flv']
medias = [file for file in files if os.path.splitext(file)[1].lower() in mediaExts]

csvExts = ['.csv', '.xlsx']
csvs = [file for file in files if os.path.splitext(file)[1].lower() in csvExts]

others = []
for file in files:
    ext = os.path.splitext(file)[1].lower()
    if (ext not in imgexts) and (ext not in docExts) and (ext not in mediaExts) and (ext not in csvExts) and os.path.isfile(file):
        others.append(file)


move('Images', images)
move('Docs', docs)
move('Media', medias)
move('CSV', csvs)
move('Others', others)

