<!--
category: Homelab
-->

# Mariadb on Debian 10

## Installing

I followed the excellent tutorial below, and everything seemed to be up and running when I finished the tutorial.

(https://www.digitalocean.com/community/tutorials/how-to-install-mariadb-on-debian-10)

## Mariadb failed to start on reboot

After shuting down the server, and rebooting, I noticed that MariaDB was not running, it would fail to start. It turned out that this was due to `/var/lib/mysql` was not created during the install. It is possible that I messed this up when I put a `root` password into Mariadb against the advice of the tutorial above. So I followed the directions to purge and manually `rm` that directory. Whatever the case, if Mariadb fails to start it could be because it doesn't have the directory it needs to write files too. The fix was simple. Simply run:

`sudo mysql_install_db`

This created the directory with the proper permissions. I could then start mariadb with `sudo systemctl start mariadb` and see that is was running now with `sudo systemctl status mariadb`.

