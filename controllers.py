from views import render_template
from models import User, Phone, JobPlace



def default_controller(data=None, cls=True):
    """Default controller"""
    render_template(context={}, template="default.jinja2", cls=cls)
    return (input(), None)


def exit_controller(data=None, cls=True):
    render_template(context={}, template="exit.jinja2", cls=cls)
    exit()


def all_users_controller(data=None, cls=True):
    users = User.all()
    render_template(context={'users':users}, template="all_users.jinja2", cls=cls)
    input("Continue?")
    return 'main', None # (next state, data)


def add_user_controller(data=None, cls=True):
    render_template(context={}, template="add_user.jinja2", cls=cls)
    username = input()
    user = User.add(username)
    return 51, user # (next state, data)


# def add_user_controller(data=None, cls=True):
#     render_template(context={}, template="add_user.jinja2", cls=cls)
#     username = input()
#     user = User.add(username)
#     return 51, user # (next state, data)


def add_job_place_controller(user, cls=True):
    render_template(context={}, template="add_job_place.jinja2", cls=cls)
    jobplace = input()
    job_place = JobPlace.add(jobplace, user)
    return 21, user # (next state, data)



def add_phone_controller(user, cls=True):
    render_template(context={}, template="add_phone.jinja2", cls=cls)
    phone_number = input()
    phone = Phone.add(phone_number, user)
    return 249, user # (next state, data)


def add_more_controller(user, cls=True):
    render_template(context={}, template="add_more.jinja2", cls=cls)
    answer = input()
    if answer == 'Y' or answer == 'y':
        return 21, user
    return "1", user # (next state, data)    

   
def _controllers(data=None, cls=True):
    users = User.all()
    render_template(context={}, template="default.jinja2", cls=cls)
    return 'main', None # (next state, data)

def get_controller(state):
    return controllers_dict.get(state, default_controller)





controllers_dict = { # use dict type instead of if else chain
    '0': exit_controller,
    '1': all_users_controller,
    '2': add_user_controller,
    # '3': update_user_controller,
    #'4': delete_user_controller,
    # '5': show_user_controller,
    21: add_phone_controller, # user can't enter 21 of int type
    51: add_job_place_controller,
    249: _controllers,
    212: add_more_controller
}