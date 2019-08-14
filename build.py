from __future__ import print_function
import subprocess
import sys, getopt

# def main(argv):
#     try:
#         opts, args = getopt.getopt(argv, "hi:o:", ["ifile=","ofile="])
#     except getopt.GetoptError:
#         print('build.py user-directory-path <user directory path>')
#         sys.exit(2)
#     print('no exception', args)
#     ud_dir_path = '~/work/epmp-user-directory/'
#     command = ['mvn clean -f ~/work/epmp-user-directory/']
#     # # command = ['ls -l | wc']
#     # # subprocess.check_call(command, shell=True)
#     # proc = subprocess.Popen(command,
#     #                         stdout=subprocess.PIPE,
#     #                         stderr=subprocess.PIPE,
#     #                         shell=True)
#     # out, err = proc.communicate()
#     #
#     # print("exit code: ", proc.returncode)
#     # print("err: ", err)
#     #
#     # print("stdout: ", out)
#
#
# if __name__ == '__main__':
#     print("Number of arguments: ", len(sys.argv))
#     print("arguments list: ", str(sys.argv))
#     main(sys.argv[1:])


def build(path):
    mvncommand = 'mvn clean install -DskipTests -f '+path
    # command = ['mvn clean -f ~/work/epmp-user-directory/']
    command = [mvncommand]
    # subprocess.check_call(command, shell=True)
    proc = subprocess.Popen(command,
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE,
                            shell=True)
    out, err = proc.communicate()

    print("exit code: ", proc.returncode)
    print("err: ", err)

    print("stdout: ", out)


def dockerimage(imagename, path):
    buildimage = 'docker build -t '+imagename+' -f '+path
    command = [buildimage]
    proc = subprocess.Popen(command,
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE,
                            shell=True)
    out, err = proc.communicate()

    print("dockerimage command exit code: ", proc.returncode)

    print("error message while buiding docker image: ", err)

    print("stdout: ", out)


def main(argv):
    udPath = ''
    try:
        opts, args = getopt.getopt(argv, "p:", ["path="])
    except getopt.GetoptError:
        print ('build.py -p <user directory path>')
        sys.exit(2)
    print('opts', opts)
    if len(opts) > 0:
        for opt, arg in opts:
            if opt in ("-p", "--path"):
                udPath = arg
                print('building user directory path "', udPath)
                build(udPath)
            else:
                print('build.py -p <user directory path>')
                sys.exit()
    else:
        print('build.py -p <user directory path>')
        sys.exit()

# def main(argv):
#     inputfile = ''
#     outputfile = ''
#     try:
#         opts, args = getopt.getopt(argv, "hi:o:", ["ifile=", "ofile="])
#     except getopt.GetoptError:
#         print ('test.py -i <inputfile> -o <outputfile>')
#         sys.exit(2)
#     print('opts', opts)
#     if len(opts) > 0:
#         for opt, arg in opts:
#             if opt in ("-i", "--ifile"):
#                 inputfile = arg
#             elif opt in ("-o", "--ofile"):
#                 outputfile = arg
#             else:
#                 print('usage: test.py -i <inputfile> -o <outputfile>')
#                 sys.exit()
#         print('Input file is "', inputfile)
#         print('Output file is "', outputfile)
#     else:
#         print('usage: -i <inputfile> -o <outputfile>')
#         sys.exit()


if __name__ == "__main__":
   main(sys.argv[1:])