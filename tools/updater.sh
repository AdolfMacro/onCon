crd=pwd
cd /tmp/
git clone https://github.com/adolfmacro/onCon.git
sudo -u root cp -R onCon/* /usr/src/oncon/
sudo -u root rm -rf onCon
cd $prc