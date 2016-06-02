# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](http://cli.learncodethehardway.org/book/). This is a great,
quick tutorial. Each "chapter" focuses on a command. Type the commands
you see in the _Do This_ section, and read the _You Learned This_
section. Move on to the next chapter. You should be able to go through
these in a couple of hours.

---

###Q1.  Cheat Sheet of Commands  

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do, focused on things that are new, interesting, or otherwise worth remembering.

> > `grep`: search for text in file

> > `sort`: sort the content of files

> > `wc`: word count

> > `cut`: cut a part of a file

> > `man`: help info 

> > `&`: execute programs in the background

> > `w`: who is logged on and what they are doing

> > `at`: execute programs at another time

> > `sudo`: become super user root

> > `kill`: kill a process

---

###Q2.  List Files in Unix   

What do the following commands do:  
`ls`  
`ls -a`  
`ls -l`  
`ls -lh`  
`ls -lah`  
`ls -t`  
`ls -Glp`  

> > `ls`: lists all files in the directory that match the name.

> > `ls -a`: Displays all files.

> > `ls -l`: Displays the long format listing.

> > `ls -lh`: Displays the long format listing and print their sizes in human readable format.

> > `ls -lah`: Uses unit suffixes: Byte, Kilobyte, Megabyte, Gigabyte, Terabyte and Petabyte in order to reduce the number of digits to three or less using base 2 for sizes and displays the long format listing and print their sizes in human readable format.

> > `ls -t`: Sort by time modified (most recently modified first) before sorting the operands by lexicographical order.

> > `ls -Glp`: Displays the colorized and long format listing and writes a slash (`/') after each filename if that file is a directory.


---

###Q3.  More List Files in Unix  

Explore these other [ls options](http://www.techonthenet.com/unix/basic/ls.php) and pick 5 of your favorites:

> > -a -d -v -f -g

---

###Q4.  Xargs   

What does `xargs` do? Give an example of how to use it.

> > construct argument list(s) and execute utility

> > find /path -type f -print | xargs rm

 

