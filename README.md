Installation
============

Following are the steps for creating a local development environment for Donor9:

1. Install pip aka the cheeseshop - Python package manager

    sudo apt-get install python-pip

2. Install virtualenv - a pakage that will create an isolated environment our project:

    sudo pip install virtualenv

3. Create our virtualenv:

    virtualenv Donor9

4. Activate virtualenv:

    cd Donor9
    source bin/activate

5. Install git:

    sudo apt-get install git

6. Clone Donor9 reposiotry:

    git clone https://github.com/hacker9/Donor9.git

7. Install requirements:

    Pre-req for this step on Debian is installing `libpq-dev` and `python-dev` packages

    pip install -r requirements.txt

8. Sync DB:

    python manage.py syncdb --settings=Donor9.settings_local

9. Run development server:

    python manage.py runserver --settings=Donor9.settings_local

10. Rock on:

    http://localhost:8000/admin

11. If you were using the pre-created DB, following are the login credentials:

    uname: admin
    pwd: admin


