# About

Scripts that interact with the website [BandMusic PDF Library](https://www.bandmusicpdf.org) to open 5 random pieces for sight-reading.

# Requirements

* Python 2 or 3

# Usage

The following sequence of instructions should open your default web browser with 5 tabs, each linked to a different song provided by *BandMusic PDF Library*.

* Download ```randomizer.py```
* Download ```urls.txt```

## On Mac

* Open terminal 
  * Applications => Utilities => Terminal
* Navigate to the directory to which you downloaded the previous files
  * For example, if you downloaded the files to your ```Downloads``` folder then enter ```cd ~/Downloads/```
  * Verify that the files you downloaded are in your present directory using ```ls```
* Enter ```cat urls.txt | python randomizer.py```
