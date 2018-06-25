
# cephmaster

wget -q -O- 'https://download.ceph.com/keys/release.asc' | sudo apt-key add -

echo deb https://download.ceph.com/debian-luminous/ $(lsb_release -sc) main | sudo tee /etc/apt/sources.list.d/ceph.list

sudo apt update
sudo apt install ceph-deploy -y

sudo apt install whois
sudo useradd -d /home/cephuser -m cephuser
sudo usermod --password `mkpasswd 1`  cephuser




echo "cephuser ALL = (root) NOPASSWD:ALL" | sudo tee /etc/sudoers.d/cephuser
sudo chmod 0440 /etc/sudoers.d/cephuser

#
sudo cat hosts >> /etc/hosts
#
su cephuser 
cd

ssh-keygen

ssh-copy-id cephuser@ceph1
ssh-copy-id cephuser@ceph2
ssh-copy-id cephuser@ceph3

#
cat host.config >> ~/.ssh/config

mkdir my-cluster
cd my-cluster

ceph-deploy purge ceph1 ceph2 ceph3
ceph-deploy purgedata ceph1 ceph2 ceph3
ceph-deploy forgetkeys
rm ceph.*

ceph-deploy new ceph1

echo 'public network = 192.168.50.0/24' >> ceph.conf

echo "release = luminous" >> /home/cephuser/.cephdeploy.conf

ceph-deploy install ceph1 ceph2 ceph3

ceph-deploy mon create-initial

ceph-deploy admin ceph1 ceph2 ceph3

ceph-deploy mgr create ceph1

ceph-deploy osd create --data /dev/sdb ceph1
ceph-deploy osd create --data /dev/sdb ceph2
ceph-deploy osd create --data /dev/sdb ceph3

# test
ssh ceph1 sudo ceph health
ssh ceph1 sudo ceph -s

# ADD A METADATA SERVER
ceph-deploy mds create ceph1

# ADDING MONITORS
ceph-deploy mon add ceph2 
ceph-deploy mon add ceph3

# ADDING MANAGERS and CHECK
ceph-deploy mgr create ceph2 ceph3
ssh ceph1 sudo ceph -s

# ADD AN RGW INSTANCE
ceph-deploy rgw create ceph1
