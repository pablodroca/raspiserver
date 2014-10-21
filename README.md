#RasPi Server

The RasPi Server provides a dasboard panel and management console for your Raspberry Pi.

##Install

This tutorial assumes no security concerns about running Pyramid projects in super user mode nor creation of specific users/groups to build your RasPiServer infrastructure.
For the tutorial purposes, it will be assumed '~/env' as directory for virtualenv instance, '~/code' as github source code folder, and '~/server' as destination folder for your server files. 

0. Install Python dev tools and RPi.GPIO libraries
```
sudo apt-get update
sudo apt-get install python-dev python-rpi.gpio
```

* Install SetupTools and VirtualEnv. Execute the following commands: 
```
cd /tmp
wget https://bitbucket.org/pypa/setuptools/raw/bootstrap/ez_setup.py
sudo python ez_setup.py
sudo easy_install virtualenv
virtualenv ~/env
~/env/bin/easy_install "pyramid==1.5.1"
~/env/bin/pip install psutil netifaces rpi.gpio
```

* Clone the RaspiServer repository and install the Pyramid distribution in your virtualenv instance:
```
mkdir ~/code
cd ~/code
git clone https://github.com/pablodroca/raspiserver.git
mkdir ~/server
ln -s ~/code/raspiserver/src/RasPiServer/ ~/server/RasPiServer
~/env/bin/python ~/server/RasPiServer/setup.py develop
cd ~/server/RasPiServer
~/env/bin/python setup.py develop
```
(Egg files are installed into the env first. Then, it is necessary to run the setup again from within the Pyramid project folder to install the project itself)

* Configure notify_ip_changes.py script in the cron (you need a gmail account and password. Here we will use the keywords RASPIEMAIL and RASPIPASS for this purpose. The keyword EMAIL will be the recipient address for notifications):
```
mkdir ~/server/cron
cp ~/code/raspiserver/scrips/notify_ip_changes.py ~/server/cron
sed -i 's/<youremail@gmail.com>/EMAIL/g' ~/server/cron/notify_ip_changes.py
sed -i 's/<raspiemail@gmail.com>/RASPIEMAIL/g' ~/server/cron/notify_ip_changes.py
sed -i 's/<raspiemail-password>/RASPIPASS/g' ~/server/cron/notify_ip_changes.py
crontab -e
```
(Here you need to add the following line at the bottom, save and close the editor: `*/5 * * * * python /home/pi/server/cron/notify_ip_changes.py` )

* Configure RasPiServer to run on startup:
```
sudo mkdir /var/log/raspiserver
sudo cp ~/code/raspiserver/scripts/etc/init.d/raspiserver /etc/init.d/
sudo update-rc.d raspiserver defaults
```

* Manually verify the server and IP notifier are working
```
python ~/server/cron/notify_ip_changes.py
```
(You should receive an email with the RasPiServer IP and URL to the dashboard)

```
sudo ~/env/bin/python ~/env/bin/pserve ~/server/RasPiServer/development.ini
```
(The dashboard should start running on port 80. Verify the URL link in your previous email)
 
* Reboot to verify the server is started at port 80 and IP changes are notified via email.
