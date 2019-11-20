import data_manager
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/mentors-with-best-first-name')
def mentor_names():
    # We get back dictionaries here (for details check 'database_common.py')
    mentor_names = data_manager.full_mentor_names()

    return render_template('mentor_names.html', mentor_names=mentor_names)


@app.route('/mentor-nicknames')
def mentor_nicknames():
    # nick_names = [dict(each_real_dict) for each_real_dict in data_manager.mentors_nicknames('Miskolc')]
    nick_names = data_manager.mentors_nicknames('Miskolc')
    return render_template('nicknames.html', nick_names=nick_names)


@app.route('/user-info-name')
def user_info_name():
    title = 'Results of the query by name'
    user_data = data_manager.find_user('Carol')
    return render_template('info.html', user_data=user_data, title=title)


@app.route('/user-info-mail')
def user_info_email():
    title = 'Results for the query by email'
    user_data = data_manager.find_by_email('%@adipiscingenimmi.edu')
    return render_template('info.html', user_data=user_data, title=title)


@app.route('/student-info')
def student_info():
    title = 'Full information of the new applicant'
    # data_manager.add_new_applicants('Markus', 'Schaffarzyk', '003620/725-2666', 'djnovus@groovecoverage.com', 54823)
    # can only run the code above once. a better solution required
    user_data = data_manager.get_student_info(54823)
    return render_template('info.html', user_data=user_data, title=title)


@app.route('/updated-phone-number')
def update_phone_number():
    title = 'Applicant\'s details after the update'
    user_data = data_manager.update_telephone_number('003670/223-7459')
    return render_template('info.html', user_data=user_data, title=title)


@app.route('/deleted')
def deleted():
    user_data = data_manager.data_to_be_deleted('%@mauriseu.net')
    title = 'Data that has been deleted'
    data_manager.delete_by_email_domain_name('%@mauriseu.net')
    return render_template('info.html', user_data=user_data, title=title)


if __name__ == '__main__':
    app.run(debug=True)


