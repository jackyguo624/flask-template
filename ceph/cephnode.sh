
sudo apt install ntp -y

sudo apt install -y whois 
sudo useradd -d /home/cephuser -m cephuser
sudo usermod --password `mkpasswd 1`  cephuser
sudo apt update

echo "cephuser ALL = (root) NOPASSWD:ALL" | sudo tee /etc/sudoers.d/cephuser
sudo chmod 0440 /etc/sudoers.d/cephuser

sudo vi /etc/ssh/sshd_config
sudo service sshd restart

sudo apt install -y python-minimal 

# after ceph-deploy admin 
sudo chmod +r /etc/ceph/ceph.client.admin.keyring


# check quorum_status
ceph quorum_status --format json-pretty

# after add RGW  add data
echo "Test-data" > testfile.txt
ceph osd pool create mytest 8
rados put test-object-1 testfile.txt --pool=mytest
