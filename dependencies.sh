#excute it using sudo sh dependencies.sh
apt-get update
apt-get -y upgrade
apt-get install -y python3-pip
apt-get install build-essential libssl-dev libffi-dev python-dev
apt-get install -y python3-venv
environments
cd environments
pyvenv my_env
ls my_env
source my_env/bin/activate
cd /usr/local/share
wget https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-1.9.7-linux-x86_64.tar.bz2
tar xjf phantomjs-1.9.7-linux-x86_64.tar.bz2
ln -s /usr/local/share/phantomjs-1.9.7-linux-x86_64/bin/phantomjs /usr/local/share/phantomjs
ln -s /usr/local/share/phantomjs-1.9.7-linux-x86_64/bin/phantomjs /usr/local/bin/phantomjs
ln -s /usr/local/share/phantomjs-1.9.7-linux-x86_64/bin/phantomjs /usr/bin/phantomjs
pip install beautifulsoup4
apt-get install aria2
apt-get install deluge-console
