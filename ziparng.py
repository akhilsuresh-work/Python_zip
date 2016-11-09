import sys, getopt, os, math, shutil

# This function extracts the contents from the command line in the form python ziparrange.py -s <sourcefolder> -d <outputfolder>
def main(argv):

       try:
          args, opts = getopt.getopt(argv,"s:d:")

       except getopt.GetoptError:
          print '\n\nError!: Please check the syntax\n'
          print 'Syntax:'
          print 'python ziparrange.py -s <sourcefolder> -d <outputfolder>\n\n'
          sys.exit(2)

       sourcedir = ""
       destinationdir = ""

       for opt, arg in args:
          if opt in ("-s"):
             sourcedir = arg
          elif opt in ("-d"):
             destinationdir = arg
       pathcheck(sourcedir)
       pathcheck(destinationdir)
       return [sourcedir,destinationdir]


# This function check whether the file path exists or not

def pathcheck(path):
     if not os.path.exists(path):
               print "\n\nError!: %s path doesn't exist"%path
               sys.exit(1)



def copyanything(path):

    file_size = []
    file_name = os.listdir(path[0])
    MB = math.pow(1024,2)
    max_size = 100 * MB

    for row in file_name:
        file_size.append(os.path.getsize(path[0]+"/"+row))
    # print "\n\n"
    dictionary = dict(zip(file_name,file_size))
    for key in dictionary:
        print key, ':', dictionary[key]
    print "\n"


    main_folder = []
    flag = 1
    while flag == 1:
            list_folder = []
            size_reached = 0
            for keychain in dictionary:
                if (size_reached <= max_size):
                    size_reached += dictionary[keychain]
                if(size_reached <= max_size):
                    list_folder.append(keychain)
                if(size_reached > max_size):
                    size_reached -= dictionary[keychain]


            temp = 0
            for key in list_folder:
                temp += dictionary[key]
                del(dictionary[key])
            main_folder.append(list_folder)
            print temp/math.pow(1024,2),"MB"
            print temp
            if len(dictionary) == 0 :
                flag = 0

    folder_pointer = 1
    for row in main_folder:

            try:
                test_folder = path[1] +"/"+"test_"+str(folder_pointer)
                os.makedirs(test_folder,0755)
            except OSError as e:
                shutil.rmtree(test_folder)
                # test_folder = path[1] +"/"+"test_"+str(folder_pointer)
                os.makedirs(test_folder,0755)


            for key in row:
                 path_1 = path[0]+"/"+key
                 try:
                    shutil.copy(path_1, test_folder)
                 except OSError as e:
                    raise

            folder_pointer += 1

# This is executed at the start of project
if __name__ == "__main__":
    pathlist = main(sys.argv[1:])
    copyanything(pathlist)