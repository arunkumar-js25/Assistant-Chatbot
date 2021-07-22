import zipfile
import datetime
import os


def zip(zip,files=[]):
    my_zipfile = zipfile.ZipFile(zip, mode='w', compression=zipfile.ZIP_DEFLATED)
    
    if files == []:
        print("No Files mentioned")
    else:
        for x in files:
            # Write to zip file
            my_zipfile.write(x)
    print('Zipping Completed..')
    my_zipfile.close()


def get_all_file_paths(directory):
    file_paths = []

    for root, directories, files in os.walk(directory):
        for filename in files:
            filepath = os.path.join(root, filename)
            file_paths.append(filepath)

    return file_paths

def zipbydir(zip,dir):
    my_zipfile = zipfile.ZipFile(zip, mode='w', compression=zipfile.ZIP_DEFLATED)
    
    files = get_all_file_paths(dir)

    if files == []:
        print("No Files mentioned")
    else:
        for x in files:
            # Write to zip file
            my_zipfile.write(x)
    print('Zipping Completed..')
    my_zipfile.close()


def readzipfile(zip,file):
    my_zipfile = zipfile.ZipFile(zip, mode='w', compression=zipfile.ZIP_DEFLATED)
    # Reading Zip File
    print("\n",my_zipfile.read(file))
    my_zipfile.close()

def unzip(zip,files=[]):
    #Open the zip file in read mode
    my_zipfile = zipfile.ZipFile(zip, mode='r')
    my_zipfile.printdir() 

    if(files == []):
        print('Extracting all file...')
        my_zipfile.extractall()
    else:
        for x in files:
            print('Extracting file '+x)
            try:
                my_zipfile.extract(x)
            except:
                print(x+'file not found')


    print('Extracting Done!')
    my_zipfile.close()

def unzipwithpassword(zip,password):
    #Open the zip file in read mode
    my_zipfile = zipfile.ZipFile(zip, mode='r')
    my_zipfile.printdir() 
    #Specify password, in my case it is login 
    #password = "login"

    print('Extracting all file...')
    my_zipfile.extractall(pwd = bytes(password, 'utf-8'))

    print('Extracting Done!')
    my_zipfile.close()
    
def zipinfo(file_name):
    # opening the zip file in READ mode
    with zipfile.ZipFile(file_name, 'r') as zip: 
        for info in zip.infolist(): 
                print(info.filename) 
                print('\tModified:\t' + str(datetime.datetime(*info.date_time))) 
                print('\tSystem:\t\t' + str(info.create_system) + '(0 = Windows, 3 = Unix)') 
                print('\tZIP version:\t' + str(info.create_version)) 
                print('\tCompressed:\t' + str(info.compress_size) + ' bytes') 
                print('\tUncompressed:\t' + str(info.file_size) + ' bytes') 


#zip("Compress-Decompress\\NewZipfile.zip",['extracted\\test.txt','extracted\\test_folder'])
#unzip("Compress-Decompress\\NewZipfile.zip")
#zipinfo("Compress-Decompress\\NewZipfile.zip")
zipbydir("Compress-Decompress\\NewZipfile.zip",'extracted' )#