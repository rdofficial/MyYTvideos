# Fixing the Kali Linux 2020 Wireless Connectivity Issue

This is the extended description / documentation for the youtube video of the same name, if you have not watched the video, yet then [click here](). The video covers a quick tutorial on how to fix the wireless connections issue in the freshly installed kali linux. Below starts the documentation.

We often face certain driver issues when we install a newer operating system. Same here with Kali Linux 2020 operating system, there occurs certain driver and modules issues. These issues occur due to the poor hardware or not so famous companies of whose hardware products we use ( Simple it means error occurs when we buy a local company's hardware ). Today we are going to cover the wireless connection issue.

First off __Kali Linux__ is a debian based linux operating system, intened for pentesting and to be used by the cyber security experts. Kali Linux comes installed with over more than a thousands of hacking tools. Current latest version of kali linux is the 2020.3.

Now what is that wireless connection error. So, often after a fresh installation of a kali linux operating system. But after booting the second timem, we get some wireless networking issues. This happen in many cases, and the reason for this is the _missing kernel headers_. This issue looks and sounds easy, but not for everyone. There are many methods for fixing that issue. We can either re compile the kernel headers for the system or can change teh package manager's repository.
