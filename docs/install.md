# Install PyRaspControl

To get PyRaspControl install onto your Raspberry Pi should be fairly straight forward. The following are steps on what you need to install and manually configure to get PyRaspControl up and running.

1. Clone the project repository from GitHub:

  ```
  sudo git clone https://github.com/davidvuong/pyraspcontrol.git /var/www/pyraspcontrol
  cd /var/www/pyraspcontrol
  ```

1. Install the project (Python) dependencies:

  ```
  sudo pip install -r requirements.txt
  ```

1. Install and setup the Apache web server:

  ```
  sudo apt-get install apache2 libapache2-mod-wsgi
  ```

1. Link the PyRaspControl Apache configuration files:

  ```
  sudo cp /var/www/pyraspcontrol/pyraspcontrol.conf /etc/apache2/sites-available/pyraspcontrol.conf
  sudo ln -s /etc/apache2/sites-available/pyraspcontrol.conf /etc/apache2/sites-enabled/pyraspcontrol.conf
  ```

1. Restart Apache:

  ```
  sudo service apache2 restart
  ```
