import re
path_to_header = 'D:\PATH_TO_GAME\GAME\Source\UPROJECT_NAME\UPROJECT_NAME.h' 
f = open(path_to_header, 'r')
data = f.readlines()
for i in range(len(data)):
    if '#define GAME_PUBLIC_BUILD' in data[i]:
        data[i] = re.sub(r'0', '1', data[i])
f.close()
with open(path_to_header, 'w') as newFile:
    newFile.writelines(data)
newFile.close()