# Note-It ![](https://img.shields.io/badge/Status-Active%20-blue) ![](https://img.shields.io/badge/Django-v3.1.7-orange) ![](https://img.shields.io/badge/Python-v3.8.5-green)
WebApp to manage notes and tasks.</br>
It is live at : https://note-it-2.herokuapp.com/</br>


## Project Setup
1. Clone this repository.<br/>
`git clone https://github.com/bhawnachopra2002/NoteIt.git`
2. Make sure Python and pip are installed else install it.
3. Open up your IDE.
4. Create a virtual environment and activate it. (For windows use following code)<br/>
`python -m venv myenv`<br/>
`myenv\Scripts\activate` (for windows)<br/>
`source env/bin/activate` (for mac)
5. Install all the required libraries in terminal.<br/>
`pip install -r requirements.txt`
6. Install PostgreSQL.Choose default port as 5432
7. Update DATABASE variable of settings.py accordingly.
8. Now migrate the models.<br/>
`python manage.py makemigrations`<br/>
`python manage.py migrate`
9. Create the superuser(Admin).<br/>
`python manage.py createsuperuser`
10. Type in following command to run project locally now at http://127.0.0.1:8000/<br/>
`python manage.py runserver`

## Built with
- Django
- HTML
- CSS

#
It is built as a course project for Software Engineering course at I.I.T. Jodhpur under guidance of Dr. Sumit Kalra.

## Collaborators
| Name              | Roll No.     |
| ----------------- |:-------------|
|[Bhawna Chopra ](https://github.com/bhawnachopra2002)|B19CSE104|
|[Darsh Patel](https://github.com/patel-16)|B19CSE115|

