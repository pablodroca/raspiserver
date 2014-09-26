raspiserver
===========

The RasPi Server provides a dasboard panel and management console for your Raspberry Pi.

Install
=======
1- Install SetupTools and VirtualEnv. Execute the following commands: 
cd /tmp
wget https://bitbucket.org/pypa/setuptools/raw/bootstrap/ez_setup.py /tmp/ez_setup.py
sudo python ez_setup.py
sudo easy_install virtualenv
VENV=~/env
virtualenv $VENV
$VENV/bin/easy_install "pyramid==1.5.1"

2- Clone the RaspiServer repository:
mkdir ~/code
cd ~/code
git clone https://github.com/pablodroca/raspiserver.git

3- Configure notify_ip_changes.py script in the cron (you need a gmail account and password. Here we will use the keywords RASPIEMAIL and RASPIPASS. The keyword EMAIL will be the recipient address for notifications):
mkdir ~/code/cron
cp ~/code/raspiserver/scrips/notify_ip_changes.py ~/code/cron
sed -i 's/<youremail@gmail.com>/EMAIL/g' ~/code/cron/notify_ip_changes.py
sed -i 's/<raspiemail@gmail.com>/RASPIEMAIL/g' ~/code/cron/notify_ip_changes.py
sed -i 's/<raspiemail-password>/RASPIPASS/g' ~/code/cron/notify_ip_changes.py
crontab -e
(
Here you need to add the following line, save and close the editor:
*/5 * * * * python /home/pi/code/cron/notify_ip_changes.py
)

4- Configure RasPiServer to run on startup:
ln -s ~/code/raspiserver/src/RasPiServer/ ~/code/server
sudo cp ~/code/raspiserver/scripts/etc/init.d/raspiserver /etc/init.d
sudo update-rc.d raspiserver defaults

5- Reboot and verify the server is working at port 80 when you receive the email.
