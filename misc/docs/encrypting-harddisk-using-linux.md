# Encrypting Hard Disk in Linux using Cryptsetup

This is the documentation (extended description) for the [youtube video](https://www.youtube.com/watch?v=iAHcwOogrY8) on [my channel](https://www.youtube.com/channel/UCfp-xR7cpyLOXVW8MYr59WA). If you haven't watched the video yet, then go and check it out for a better practical experience. [Click here](https://www.youtube.com/watch?v=iAHcwOogrY8) to watch the video. Enjoy the detailed tutorial written below.

## Introduction

Today we are going to learn how to encrypt a hard disk in the linux operating system. We will use a linux utility named __cryptsetup__. First off we should learn what is disk encryption and why should we encrypt our hard disk. Hard disk encryption is the process of protecting our hard disk's data and all the information stored there in such a way that only we can access to that information inside that hard disk. Now, why should we encrypt our hard disks, is it neccessary? No, I am not saying that the disk encryption is neccessary, but I would surely say that this would assure your private data being more safe and secure. Now let us start learning on how the disk encryption works. We will use the LUKS (Linux Unified Key Setup) format for creating the encrypted hard disk. LUKS implements a platform-independent standard on-disk format for use in various tools. This not only facilitates compatibility and interoperability among different programs, but also assures that they all implement password management in a secure and documented manner. The tool _cryptsetup_ makes our encryption process more easier. Some arguments for the tool crypsetup are given below :
* _cryptsetup luksFormat <-device-name->_ :- The command is format a disk to a LUKS format, and also encrypts the disk with a password.

* _cryptsetup luksOpen <-device-name-> <-notation->_ :- The command is used to open an already encrypted hard disk (OR hard disk partition), the hard disk is then opened at /dev/mapper/<-notation->. The notation is the name with which we want to open the required LUKS partition.

* _cryptsetup luksClose <-notation->_ :- The command is used to close an already opened encrypted disk (OR partition).

We will use the above three commands mainly during the whole process of encrypting a hard disk and, also everytime we use the encrypted disk. 

## Process

First open up a linux terminal and get into the root user by using the command
```
sudo bash
```
Note that the user account you are using must have granted SUDO permissions, otherwise you will not be able to do the further processes.
Next we need to format our hard drive, before that we need to find which name is our hard drive being mounted. Generally, the base hard disk is mounted as _/dev/sda_ and rest all are started with _/dev/sdb_, _/dev/sdc_. Also the partitions of each hard disk are indicated by the numbers post the device name like _/dev/sda1_, _/dev/sda2_, _/dev_sda3_, etc. So, we need to find out which hard drive or hard disk partition we are going to format in LUKS. Also, if we are using a virtual hard disk image file, we can just use the virtual disk image file, and format it directly. In the tutorial video, we are using a virtual hard disk image file, but you can also do with a real device. So, let us assume that our hard disk is named as '_/dev/sdb1_' (According to linux, it is the 1st partition of the 2nd connected hard drive). To format the specified hard drive partition into the LUKS format, we will use the below command
```
cryptsetup luksFormat /dev/sda1
```
After pressing the enter key and launching the command, the software asks us for the password for our new encrypted hard drive. Give a strong and memorable password. Then, it will ask for the confirmation by typing uppercase 'YES' and pressing enter. After a few seconds, our hard drive is encrypted. Now, lets mount it and use it.
To open the newly encrypted hard drive, we need to open it under cryptsetup utility using the below command.
```
cryptsetup luksOpen /dev/sda1 <disk-name>
```
In the disk-name part, we can give any name of our choice. This is the name of the endpoint where our encrypted hard drive will be mapped to. So, if I give the name 'disk', then my encrypted drive will be mapped at _/dev/mapper/disk_. Also we need to enter the password before the hard disk is being opened. Now before mounting this hard drive, we need to format it to ext4 filesystem to use it for saving data. To format it in ext4 filesystem, use the below command.
```
mkfs.ext4 /dev/mapper/disk
```
After launching the command, our mapped device is formatted to ext4 filesystem and now it can be used as a regular hard drive. __Note__ : These processes of disk formatting is only one time.

Now, for mounting the hard drive we can use the command
```
mount /dev/mapper/disk /mnt
```
Where _/mnt_ is the mountpoint for our hard disk. Now, out hard disk is mounted at _/mnt_ folder. We can just create, copy or move files and folders at folder _/mnt_. For unmounting the hard disk, we can use the below command.
```
umount -R /mnt
```
Now, we also need to close the mapped encrypted hard disk which is opened at _/dev/mapper/disk_. We will use the below command for the purpose.
```
cryptsetup luksClose disk
```

Now, let's sum up the commands we will use for everyday for using the encrypted hard disk. Below are the commands.
```
# For mounting
cryptsetup luksOpen /dev/sdb1 disk
mount /dev/mapper/disk /mnt

# For unmounting
umount -R /mnt
cryptsetup luksClose disk
```

## Conclusion

So at the end, hope you have got all the important points in the process of the disk encryption. Even now, if you have any doubts, then kindly put a comment on the youtube video or just contact me at [my instagram account](https://instagram.com/rdofficial192) with username _@rdofficial_. Below are given some quick links for you :

* Creating a virtual hard disk using linux command line : [Click here](creating-virtual-harddisk-using-linux-commandline.md)
* A Brief Introduction to Linux : [Click here](../../LiveOnLinux/docs/video-1-doc.md)
