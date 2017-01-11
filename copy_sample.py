# auther = Cheng Chang(SA)
# Date = 2016/11/25
import os
import sys
import shutil


def copy_sample(name_list, src_folder, des_folder):
    count = 0
    if not os.path.exists(os.path.join(des_folder, "malicious")):
        os.mkdir(os.path.join(des_folder, "malicious"))
    if not os.path.exists(os.path.join(des_folder, "monitoring")):
        os.mkdir(os.path.join(des_folder, "monitoring"))
    if not os.path.exists(os.path.join(des_folder, "undetermined")):
        os.mkdir(os.path.join(des_folder, "undetermined"))
    des_folder_dir = des_folder
    with open(name_list, "r") as f:
        for line in f:
            count += 1
            print count            
            name = line.strip()
            if "malicious" in name:
                des_folder = os.path.join(des_folder_dir, "malicious")
            elif "monitoring" in name:
                des_folder = os.path.join(des_folder_dir, "monitoring")
            else:
                des_folder = os.path.join(des_folder_dir, "undetermined")
            name = line[line.find("-") + 1:-1]
            print os.path.join(src_folder, name)
            if os.path.exists(os.path.join(src_folder, name)):
                f_path = os.path.join(src_folder, name)
                shutil.copyfile(f_path, os.path.join(des_folder, name))
            else:
                print '[ERROR] %s do not exists in %s ' % (name, src_folder)


def main():
    if len(sys.argv) != 4:
        print """
Usage:
    python copy_sample.py sha1s.txt src_folder des_folder

copy sample in sha1s.txt from src_folder to des_folder
    """
        exit(0)
    if not os.path.exists(sys.argv[1]):
        print "name_list don't exists"
        exit(0)
    if not os.path.exists(sys.argv[2]):
        print "src_folder don't exists"
        exit(0)
    if not os.path.exists(sys.argv[3]):
        os.makedirs(sys.argv[3])
    copy_sample(sys.argv[1], sys.argv[2], sys.argv[3])


if __name__ == '__main__':
    main()
