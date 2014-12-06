# Get Started
This project uses vagrant to setup a VM to run in.
	
	# Initialize VM image and provision.
    vagrant up
    # SSH into VM.
    vagrant ssh

Run database migrations, crete a super user and load development data.

    ./manage.py migrate
    ./manage.py createsuperuser
    ./manage.py loaddata dev_data

Start a test server on port 8000 inside the VM. Port 8111 on your host machine is forwarded to port 8000 on the VM.

    ./manage.py runserver 0.0.0.0:8000


# Admin UI

Once you have created a super user you can load the admin UI in a web browser on your host machine and login. http://localhost:8111/admin


# REST API

Load the bikes API from your host machine.

    # API root
    curl http://localhost:8111/tw/api/
	# All bikes
    curl http://localhost:8111/tw/api/bikes
    # Bike detail
    curl http://localhost:8111/tw/api/bikes/1


# Vagrant

When you are done with the VM, you can suspend all of its resources until you need it again.

    vagrant suspend

When you are ready to begin development again, you only need a single command.

    vagrant up
