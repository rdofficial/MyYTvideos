# Creating A Virtual Hard Disk Using Linux Command Line

This is the documentation (extended description) for the youtube video with same name on [my channel](https://www.youtube.com/channel/UCfp-xR7cpyLOXVW8MYr59WA). If you haven't watched the video yet, then [click here](https://www.youtube.com/watch?v=P9FENXil9tU) to watch the video, the video will give you a better practical experience. Let's begin the documentation.

# Introduction

So in this documentation, we are going to see the tutorial of creating a virtual hard disk file using simple linux commands. Before knowing on how to create a virtual hard disk, we shall read a small definition of the virtual hard disk. If you feel bored, you can skip to the process section ;-). _In a computer system, the hard disk plays an important role. In the same way, a Virtual hard disk plays an important role in a Virtual machine. It’s just like a physical HDD, and it may contain disk partitions, file systems, and other files and folders. The primary function of a virtual hard disk is to allow multiple operating systems to reside on a single machine used as a host system._
But we are not going to use multiple operating systems, we are just going to show you on how to create a virtual hard disk. We will use the __dd__ command to complete this process. Let us learm about dd command. dd is a command-line utility for Unix and Unix-like operating systems whose primary purpose is to convert and copy files. On Unix, device drivers for hardware (such as hard disk drives) and special device files (such as /dev/zero and /dev/random) appear in the file system just like normal files. dd can also read and/or write from/to these files, provided that function is implemented in their respective drivers. As a result, dd can be used for tasks such as backing up the boot sector of a hard drive, and obtaining a fixed amount of random data. The dd program can also perform conversions on the data as it is copied, including byte order swapping and conversion to and from the ASCII and EBCDIC text encodings.

# Process

First we have to open our linux terminal (command line). Then, we have to create a virtual hard disk file (.img extension) using the command __dd__. Here is the syntax of the command that we are using.
```
dd if=/dev/zero of=<harddisk-filename>.img bs=1M count=<size in MegaBytes>
```
Let me break this down for you guys. First we are calling the _dd_ command and then we are transferring the disk data from the /dev/zero device, and the target point where we are transferring all those information of the hard drive is given by the _of_ parameter. You can give any name to that virtual hard disk file, but remember to give it a extension of _.img_. And then follow as usual. After that we have another parameter to look on and that is _count_. This parameter specifies the size of the virtual hard disk, and note that the parameter takes the size in megabytes (MBs). On pressing the enter key, this command starts creating the virtual hard disk file. The process from minutes to a while depending upon of what size virtual hard disk is being created.

After this, we need to format our blank hard drive to a specific filesystem in order to use properly. We will format it in ext4 filesystem, but you can do it any form. Below are given the command syntaxes for each filesystem type.
* For ext4 filesystem
```
mkfs.ext4 <harddisk-filename>.img
```
* For NTFS filesystem
```
mkfs.ntfs <harddisk-filename>.img
```
* For FAT32 filesystem
```
mkfs.vfat <harddisk-filename>.img
```

After formatting the newly created virtual hard disk we can mount it and use it like a normal hard drive. To mount the hard drive, we will use the below command
```
sudo mount <harddisk-filename>.img /mnt
```
Here, _/mnt_ is the mountpoint location where our newly created hard drive is mounted. We can move inside that folder and create files, or copy files. After doing our work, we need to unmount it. For unmouting a hard drive, we will use the below command.
```
sudo umount -R /mnt
```
Using the same way we can use our virtual hard drive at anytime as per our need ;-). Note that the commands for mounting and unmounting a hard drive required SUDO permissions, so the user account of the linux system that you are using must have granted these SUDO privileges.

# Conclusion

So after this tutorial, hope so your all doubts are clear. If this bulky documentation based tutorial feels boring, then you can check out the practical version tutorial on my youtube channel, [click here](). Also leave a comment, if you have any doubts regarding the tutorial.

Some related content for you are listed below :
* Cracking WiFi passwords using Kali Linux : [Click here](https://www.youtube.com/watch?v=9N71dtcgIaY)
* A Brief Introduction to Linux : [Click here](https://www.youtube.com/watch?v=iWtg9L8ZJTA)
* Why we cannot hack facebook anymore : [Click here](https://www.youtube.com/watch?v=-UaFtxFcT_4)
