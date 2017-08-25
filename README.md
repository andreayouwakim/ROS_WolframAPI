# ROS Expansion of Robotic Knowledgebase 
Summer Research Fellowship ROS Project:

First year summer research fellowship project.

## Prerequisites:

### WolframAlpha - App Code

A wolfram alpha app request needs to be made by whomever is using my 
code if the more than fifty queries are to be made. 
To request an appcode, go to https://developer.wolframalpha.com,
make a free account, login and register for an app code.
It is important to note that the user needs to save this appcode and
(if the user is going to further develop this project )this code should 
not be shared with anyone.

### Pip:

Pip is a better alternative to Easy Install for installing Python packages. 
If you don't have Pip installed already, you definitely need it 
for this project. Here are the three terminal commands needed 
to install Pip.

$ sudo apt-get install python-pip python-dev build-essential 

$ sudo pip install --upgrade pip 

$ sudo pip install --upgrade virtualenv 

### WolframAlpha - Dependencies:

Wolfram Alpha needs to be installed on whichever computer is 
running this code.
You can find more usage, extended documentation, and instructions 
for installing here:
https://pypi.python.org/pypi/wolframalpha


### Running the code:
This code needs to be directly placed in your catkin_ws (right in the src folder).
Your pathfile should look like this:
user:~/catkin_ws/src$ 
That way when you type the terminal command "ls", you can see that
the option for "my_pkg" is available.
The command to execute the code is:
$ rosrun my_pkg wolfram.py

At this point you'll be prompted to input a question to your 
machine (don't forget the '?' ). 
After this has been done, hit 'enter' and then you should recieve 
your answer.
