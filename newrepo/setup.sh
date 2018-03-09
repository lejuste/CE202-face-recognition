#docker setup script

#Prior to pulling image
#	build docker file to dockerize program
#	include (RunTest.py,toplev.py,runThreads.py,throughputRun)
#	must take in arguments (thread and size, output file?)

#pull docker image
#pull 
sudo apt-get -y update
sudo apt-get install -y --fix-missing parallel git wget curl python-numpy


# get docker


curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
sudo apt-get update
apt-cache policy docker-ce
sudo apt-get install -y docker-ce
#sudo systemctl status docker


#get files for plotting baby
sudo apt install git
mkdir ce202-jusclee
cd ce202-jusclee/
git clone https://github.com/lejuste/CE202-face-recognition

#pull docker image dude
sudo docker pull jusclee/ce-202:firstTry

#install pip!!!
sudo apt-get install python-pip
sudo apt-get install linux-tools-common linux-tools-generic linux-tools-`uname -r`
sudo apt-get install python-matplotlib



