import os
import time

unsafe_ext = ('.jpg', '.gif', '.png', '.tiff', '.psd', '.eps', '.raw', '.mp4', '.avi', '.wav', '.mp3', '.exe')

def getAllFiles(osType):
    start = time.time()
    file_paths = []
    totalFilesLookedThrough = 0
    if str(osType) == 'lnx':
        osType = 'linuxOS'
        for root, dirs, files in os.walk('/'):
            for file in files:
                totalFilesLookedThrough += 1
                file_path, file_ext = os.path.splitext(root+'/'+file)
                if file_ext in unsafe_ext:
                    file_paths.append(root+'/'+file)
    elif str(osType) == 'win':
        osType = 'windows'
        for root, dirs, files in os.walk('C:\\'):
            for file in files:
                totalFilesLookedThrough += 1
                file_path, file_ext = os.path.splitext(root+'\\'+file)
                if file_ext in unsafe_ext:
                    file_paths.append(root+'\\'+file)
    else:
        return None
    stop = time.time()
    final = stop - start
    totalF = len(file_paths)
    
    return [file_paths, final, totalF, totalFilesLookedThrough, osType]

def displayStats(files, time, total, looked, os):
    display = input('Show Files (Y = All, N = None, M = First 5, S = Save To .txt)>>>')
    if display.lower() == 'y':
        for file in files:
            print(file)
    elif display.lower() == 'n':
        pass
    elif display.lower() == 'm':
        i = 0
        for file in files:
            if i != 5:
                print(file)
                i += 1
            else:
                break
    elif display.lower() == 's':
        addFiles = ''
        for file in files:
            addFiles = addFiles + file + '\n'
        with open('Files.txt', 'wb') as filetxt:
            filetxt.write(bytes(str(addFiles), 'utf-8'))
            print('Files Saved To Files.txt')
    print('Stats For Infected ' + str(os) + ' Computer')
    print('-----------------------------------')
    print('Time: ' + str(time) + ' Seconds')
    print('Files In Category: ' + str(total))
    print('Files Looked Through: '+ str(looked))
    print('OS: ' + str(os))


if __name__ == '__main__':
    x = getAllFiles('lnx')
    files = x[0]
    totalTime = x[1]
    totalFiles = x[2]
    totallooked = x[3]
    osType = x[4]

    displayStats(files, totalTime, totalFiles, totallooked, osType)

# for file in files:
#     print(file)

# print('Found Files In ' + str(totalTime).partition('.')[0] + ' Seconds')
# print('Total Files in Genere ' + str(totalFiles))
# print('Total Files Looked Through ' + str(totallooked))
# print('OS Type Is ' + str(osType))
