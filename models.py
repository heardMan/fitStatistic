import os
from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from flask_sqlalchemy import SQLAlchemy

'''Instantiate a sequel alchemy instance'''
db = SQLAlchemy()

#database path set as an environment variable
database_path = os.getenv("SQLALCHEMY_DATABASE_URI")


def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    db.drop_all()
    db.create_all()


def seed_db():
    # db.drop_all()
    '''DEFINE AND CREATE SOME DEFAULT PERMISSIONS'''

    #define client related permissions
    get_clients = Permission(name='get:clients', description='allow user to get clients from the database')
    get_clients_detail = Permission(name='get:clients-detail', description='allow user to get detailed client object from the database')
    post_clients = Permission(name='get:clients', description='allow user to post clients to the database')
    patch_clients = Permission(name='get:clients', description='allow user to patch clients in the database')
    delete_clients = Permission(name='get:clients', description='allow user to delete clients from the database')
    #create client related permissions
    get_clients.insert()
    post_clients.insert()
    patch_clients.insert()
    delete_clients.insert()

    #define trainer related permissions
    get_trainers = Permission(name='get:trainers', description='allow user to get trainers from the database')
    get_trainers_detail = Permission(name='get:trainers-detail', description='allow user to get detailed trainers object from the database')
    post_trainers = Permission(name='get:trainers', description='allow user to post trainers to the database')
    patch_trainers = Permission(name='get:trainers', description='allow user to patch trainers in the database')
    delete_trainers = Permission(name='get:trainers', description='allow user to delete trainers from the database')
    #create trainer related permissions
    get_trainers.insert()
    post_trainers.insert()
    patch_trainers.insert()
    delete_trainers.insert()

    #define exercise related permissions
    get_exercises = Permission(name='get:exercises', description='allow user to get exercises from the database')
    post_exercises = Permission(name='post:exercises', description='allow user to post exercises to the database')
    patch_exercises = Permission(name='patch:exercises', description='allow user to patch exercises in the database')
    delete_exercises = Permission(name='delete:exercises', description='allow user to delete exercises in the database')
    #create exercise related permissions
    get_exercises.insert()
    post_exercises.insert()
    patch_exercises.insert()
    delete_exercises.insert()

    #define workout related permissions
    get_workouts = Permission(name='get:workouts', description='allow user to get workouts from the database')
    post_workouts = Permission(name='post:workouts', description='allow user to post workouts to the database')
    patch_workouts = Permission(name='patch:workouts', description='allow user to patch workouts in the database')
    delete_workouts = Permission(name='delete:workouts', description='allow user to delete workouts in the database')
    #create workout related permissions
    get_workouts.insert()
    post_workouts.insert()
    patch_workouts.insert()
    delete_workouts.insert()

    # define workout_exercise related permissions
    get_workout_exercises = Permission(name='get:workout_exercises', description='allow user to get workout_exercises from the database')
    post_workout_exercises = Permission(name='post:workout_exercises', description='allow user to post workout_exercises to the database')
    patch_workout_exercises = Permission(name='patch:workout_exercises', description='allow user to patch workout_exercises in the database')
    delete_workout_exercises = Permission(name='delete:workout_exercises', description='allow user to delete workout_exercises in the database')
    # create workout_exercise related permissions
    get_workout_exercises.insert()
    post_workout_exercises.insert()
    patch_workout_exercises.insert()
    delete_workout_exercises.insert()

    # define user_workout related permissions
    get_user_workouts = Permission(name='get:user_workouts', description='allow user to get user_workouts from the database')
    post_user_workouts = Permission(name='post:user_workouts', description='allow user to post user_workouts to the database')
    patch_user_workouts = Permission(name='patch:user_workouts', description='allow user to patch user_workouts in the database')
    delete_user_workouts = Permission(name='delete:user_workouts', description='allow user to delete user_workouts in the database')
    # create user_workout related permissions
    get_user_workouts.insert()
    post_user_workouts.insert()
    patch_user_workouts.insert()
    delete_user_workouts.insert()

    # define user_exercise related permissions
    get_user_exercises = Permission(name='get:user_exercises', description='allow user to get user_exercises from the database')
    post_user_exercises = Permission(name='post:user_exercises', description='allow user to post user_exercises to the database')
    patch_user_exercises = Permission(name='patch:user_exercises', description='allow user to patch user_exercises in the database')
    delete_user_exercises = Permission(name='delete:user_exercises', description='allow user to delete user_exercises in the database')
    # create user_exercise related permissions
    get_user_exercises.insert()
    post_user_exercises.insert()
    patch_user_exercises.insert()
    delete_user_exercises.insert()

    # define exercise_sets related permissions
    get_exercise_sets = Permission(name='get:exercise_sets', description='allow user to get exercise_sets from the database')
    post_exercise_sets = Permission(name='post:exercise_sets', description='allow user to post exercise_sets to the database')
    patch_exercise_sets = Permission(name='patch:exercise_sets', description='allow user to patch exercise_sets in the database')
    delete_exercise_sets = Permission(name='delete:exercise_sets', description='allow user to delete exercise_sets in the database')
    # create exercise_sets related permissions
    get_exercise_sets.insert()
    post_exercise_sets.insert()
    patch_exercise_sets.insert()
    delete_exercise_sets.insert()

    '''CREATE ADMIN ROLE WITH PERMISSIONS'''

    admin_role = Role(name='Administrator', description='user can perform all allowed actions')
    admin_role.insert()

    # define permissions allow trainers to manage clients
    admin_get_clients = Role_Permission(role_id=admin_role.id, permission_id=get_clients.id)
    admin_get_clients_detail = Role_Permission(role_id=admin_role.id, permission_id=get_clients_detail.id)
    admin_post_clients = Role_Permission(role_id=admin_role.id, permission_id=post_clients.id)
    admin_patch_clients = Role_Permission(role_id=admin_role.id, permission_id=patch_clients.id)
    admin_delete_clients = Role_Permission(role_id=admin_role.id, permission_id=delete_clients.id)
    # create permissions allow admins to manage clients
    admin_get_clients.insert()
    admin_get_clients_detail.insert()
    admin_post_clients.insert()
    admin_patch_clients.insert()
    admin_delete_clients.insert()

    # define permissions allow admins to manage trainers
    admin_get_trainers = Role_Permission(role_id=admin_role.id, permission_id=get_trainers.id)
    admin_get_trainers_detail = Role_Permission(role_id=admin_role.id, permission_id=get_trainers_detail.id)
    admin_post_trainers = Role_Permission(role_id=admin_role.id, permission_id=post_trainers.id)
    admin_patch_trainers = Role_Permission(role_id=admin_role.id, permission_id=patch_trainers.id)
    admin_delete_trainers = Role_Permission(role_id=admin_role.id, permission_id=delete_trainers.id)
    # create permissions allow admins to manage trainers
    admin_get_trainers.insert()
    admin_get_trainers_detail.insert()
    admin_post_trainers.insert()
    admin_patch_trainers.insert()
    admin_delete_trainers.insert()

    # define permissions allow admins to manage exercises
    admin_get_exercises = Role_Permission(role_id=admin_role.id, permission_id=get_exercises.id)
    admin_post_exercises = Role_Permission(role_id=admin_role.id, permission_id=post_exercises.id)
    admin_patch_exercises = Role_Permission(role_id=admin_role.id, permission_id=patch_exercises.id)
    admin_delete_exercises = Role_Permission(role_id=admin_role.id, permission_id=delete_exercises.id)
    # create permissions allow admins to manage exercises
    admin_get_exercises.insert()
    admin_post_exercises.insert()
    admin_patch_exercises.insert()
    admin_delete_exercises.insert()

    # define permissions allow admins to manage workouts
    admin_get_workouts = Role_Permission(role_id=admin_role.id, permission_id=get_workouts.id)
    admin_post_workouts = Role_Permission(role_id=admin_role.id, permission_id=post_workouts.id)
    admin_patch_workouts = Role_Permission(role_id=admin_role.id, permission_id=patch_workouts.id)
    admin_delete_workouts = Role_Permission(role_id=admin_role.id, permission_id=delete_workouts.id)
    # create permissions allow admins to manage workouts
    admin_get_workouts.insert()
    admin_post_workouts.insert()
    admin_patch_workouts.insert()
    admin_delete_workouts.insert()

    # define permissions allow admins to manage workout_exercises
    admin_get_workout_exercises = Role_Permission(role_id=admin_role.id, permission_id=get_workout_exercises.id)
    admin_post_workout_exercises = Role_Permission(role_id=admin_role.id, permission_id=post_workout_exercises.id)
    admin_patch_workout_exercises = Role_Permission(role_id=admin_role.id, permission_id=patch_workout_exercises.id)
    admin_delete_workout_exercises = Role_Permission(role_id=admin_role.id, permission_id=delete_workout_exercises.id)
    # create permissions allow admins to manage workout_exercises
    admin_get_workout_exercises.insert()
    admin_post_workout_exercises.insert()
    admin_patch_workout_exercises.insert()
    admin_delete_workout_exercises.insert()

    # define permissions allow admins to manage user_workout
    admin_get_user_workouts = Role_Permission(role_id=admin_role.id, permission_id=get_user_workouts.id)
    admin_post_user_workouts = Role_Permission(role_id=admin_role.id, permission_id=post_user_workouts.id)
    admin_patch_user_workouts = Role_Permission(role_id=admin_role.id, permission_id=patch_user_workouts.id)
    admin_delete_user_workouts = Role_Permission(role_id=admin_role.id, permission_id=delete_user_workouts.id)
    # create permissions allow admins to manage user_workout
    admin_get_user_workouts.insert()
    admin_post_user_workouts.insert()
    admin_patch_user_workouts.insert()
    admin_delete_user_workouts.insert()

    # define permissions allow admins to manage user_exercise
    admin_get_user_exercises = Role_Permission(role_id=admin_role.id, permission_id=get_user_exercises.id)
    admin_post_user_exercises = Role_Permission(role_id=admin_role.id, permission_id=post_user_exercises.id)
    admin_patch_user_exercises = Role_Permission(role_id=admin_role.id, permission_id=patch_user_exercises.id)
    admin_delete_user_exercises = Role_Permission(role_id=admin_role.id, permission_id=delete_user_exercises.id)
    # create permissions allow admins to manage user_exercise
    admin_get_user_exercises.insert()
    admin_post_user_exercises.insert()
    admin_patch_user_exercises.insert()
    admin_delete_user_exercises.insert()

    # define permissions allow admins to manage exercise_sets
    admin_get_user_exercises = Role_Permission(role_id=admin_role.id, permission_id=get_user_exercises.id)
    admin_post_user_exercises = Role_Permission(role_id=admin_role.id, permission_id=post_user_exercises.id)
    admin_patch_user_exercises = Role_Permission(role_id=admin_role.id, permission_id=patch_user_exercises.id)
    admin_delete_user_exercises = Role_Permission(role_id=admin_role.id, permission_id=delete_user_exercises.id)
    # create permissions allow admins to manage exercise_sets
    admin_get_user_exercises.insert()
    admin_post_user_exercises.insert()
    admin_patch_user_exercises.insert()
    admin_delete_user_exercises.insert()

    '''CREATE TRAINER ROLE WITH PERMISSIONS'''

    trainer_role = Role(name='Trainer', description='can create/edit exercises and workouts and can create/edit client userworkouts')
    trainer_role.insert()

    # define permissions allow trainers to manage clients
    trainer_get_clients = Role_Permission(role_id=trainer_role.id, permission_id=get_clients.id)
    trainer_get_clients_detail = Role_Permission(role_id=trainer_role.id, permission_id=get_clients_detail.id)
    trainer_post_clients = Role_Permission(role_id=trainer_role.id, permission_id=post_clients.id)
    trainer_patch_clients = Role_Permission(role_id=trainer_role.id, permission_id=patch_clients.id)
    trainer_delete_clients = Role_Permission(role_id=trainer_role.id, permission_id=delete_clients.id)
    # create permissions allow trainers to manage clients
    trainer_get_clients.insert()
    trainer_get_clients_detail.insert()
    trainer_post_clients.insert()
    trainer_patch_clients.insert()
    trainer_delete_clients.insert()

    # define permissions allow trainers to manage exercises
    trainer_get_exercises = Role_Permission(role_id=trainer_role.id, permission_id=get_exercises.id)
    trainer_post_exercises = Role_Permission(role_id=trainer_role.id, permission_id=post_exercises.id)
    trainer_patch_exercises = Role_Permission(role_id=trainer_role.id, permission_id=patch_exercises.id)
    trainer_delete_exercises = Role_Permission(role_id=trainer_role.id, permission_id=delete_exercises.id)
    # create permissions allow trainers to manage exercises
    trainer_get_exercises.insert()
    trainer_post_exercises.insert()
    trainer_patch_exercises.insert()
    trainer_delete_exercises.insert()

    # define permissions allow trainers to manage workouts
    trainer_get_workouts = Role_Permission(role_id=trainer_role.id, permission_id=get_workouts.id)
    trainer_post_workout = Role_Permission(role_id=trainer_role.id, permission_id=post_workouts.id)
    trainer_patch_workouts = Role_Permission(role_id=trainer_role.id, permission_id=patch_workouts.id)
    trainer_delete_workouts = Role_Permission(role_id=trainer_role.id, permission_id=delete_workouts.id)
    # create permissions allow trainers to manage workouts
    trainer_get_workouts.insert()
    trainer_post_workout.insert()
    trainer_patch_workouts.insert()
    trainer_delete_workouts.insert()

    # define permissions allow trainers to manage workout_exercises
    trainer_get_workout_exercises = Role_Permission(role_id=trainer_role.id, permission_id=get_workout_exercises.id)
    trainer_post_workout_exercises = Role_Permission(role_id=trainer_role.id, permission_id=post_workout_exercises.id)
    trainer_patch_workout_exercises = Role_Permission(role_id=trainer_role.id, permission_id=patch_workout_exercises.id)
    trainer_delete_workout_exercises = Role_Permission(role_id=trainer_role.id, permission_id=delete_workout_exercises.id)
    # create permissions allow trainers to manage workout_exercises
    trainer_get_workout_exercises.insert()
    trainer_post_workout_exercises.insert()
    trainer_patch_workout_exercises.insert()
    trainer_delete_workout_exercises.insert()

    # define permissions allow trainers to manage user_workout
    trainer_get_user_workouts = Role_Permission(role_id=trainer_role.id, permission_id=get_user_workouts.id)
    trainer_post_user_workouts = Role_Permission(role_id=trainer_role.id, permission_id=post_user_workouts.id)
    trainer_patch_user_workouts = Role_Permission(role_id=trainer_role.id, permission_id=patch_user_workouts.id)
    trainer_delete_user_workouts = Role_Permission(role_id=trainer_role.id, permission_id=delete_user_workouts.id)
    # create permissions allow trainers to manage user_workout
    trainer_get_user_workouts.insert()
    trainer_post_user_workouts.insert()
    trainer_patch_user_workouts.insert()
    trainer_delete_user_workouts.insert()

    # define permissions allow trainers to manage user_exercise
    trainer_get_user_exercises = Role_Permission(role_id=trainer_role.id, permission_id=get_user_exercises.id)
    trainer_post_user_exercises = Role_Permission(role_id=trainer_role.id, permission_id=post_user_exercises.id)
    trainer_patch_user_exercises = Role_Permission(role_id=trainer_role.id, permission_id=patch_user_exercises.id)
    trainer_delete_user_exercises = Role_Permission(role_id=trainer_role.id, permission_id=delete_user_exercises.id)
    # create permissions allow trainers to manage user_exercise
    trainer_get_user_exercises.insert()
    trainer_post_user_exercises.insert()
    trainer_patch_user_exercises.insert()
    trainer_delete_user_exercises.insert()
    
    # define permissions allow trainers to manage exercise_sets
    trainer_get_exercise_sets = Role_Permission(role_id=trainer_role.id, permission_id=get_exercise_sets.id)
    trainer_post_exercise_sets = Role_Permission(role_id=trainer_role.id, permission_id=post_exercise_sets.id)
    trainer_patch_exercise_sets = Role_Permission(role_id=trainer_role.id, permission_id=patch_exercise_sets.id)
    trainer_delete_exercise_sets = Role_Permission(role_id=trainer_role.id, permission_id=delete_exercise_sets.id)
    # create permissions allow trainers to manage exercise_sets
    trainer_get_exercise_sets.insert()
    trainer_post_exercise_sets.insert()
    trainer_patch_exercise_sets.insert()
    trainer_delete_exercise_sets.insert()

    # define permissions allow trainers to get trainers (limited)
    trainer_get_trainer = Role_Permission(role_id=trainer_role.id, permission_id=get_trainers.id)
    # create permissions allow trainers to get trainers (limited)
    trainer_get_trainer.insert()


    '''
    CREATE CLIENT ROLE WITH PERMISSIONS
    '''

    client_role = Role(name='Client', description='can create/edit own userworkouts')
    client_role.insert()
    
    # define permissions allow clients to manage user_workout
    client_get_user_workouts = Role_Permission(role_id=trainer_role.id, permission_id=get_user_workouts.id)
    client_post_user_workouts = Role_Permission(role_id=trainer_role.id, permission_id=post_user_workouts.id)
    client_patch_user_workouts = Role_Permission(role_id=trainer_role.id, permission_id=patch_user_workouts.id)
    client_delete_user_workouts = Role_Permission(role_id=trainer_role.id, permission_id=delete_user_workouts.id)
    # create permissions allow clients to manage user_workout
    client_get_user_workouts.insert()
    client_post_user_workouts.insert()
    client_patch_user_workouts.insert()
    client_delete_user_workouts.insert()

    # define permissions allow clients to manage user_exercise
    client_get_user_exercises = Role_Permission(role_id=trainer_role.id, permission_id=get_user_exercises.id)
    client_post_user_exercises = Role_Permission(role_id=trainer_role.id, permission_id=post_user_exercises.id)
    client_patch_user_exercises = Role_Permission(role_id=trainer_role.id, permission_id=patch_user_exercises.id)
    client_delete_user_exercises = Role_Permission(role_id=trainer_role.id, permission_id=delete_user_exercises.id)
    # create permissions allow clients to manage user_exercise
    client_get_user_exercises.insert()
    client_post_user_exercises.insert()
    client_patch_user_exercises.insert()
    client_delete_user_exercises.insert()

    # define permissions allow clients to manage exercise_sets
    client_get_exercise_sets = Role_Permission(role_id=trainer_role.id, permission_id=get_exercise_sets.id)
    client_post_exercise_sets = Role_Permission(role_id=trainer_role.id, permission_id=post_exercise_sets.id)
    client_patch_exercise_sets = Role_Permission(role_id=trainer_role.id, permission_id=patch_exercise_sets.id)
    client_delete_exercise_sets = Role_Permission(role_id=trainer_role.id, permission_id=delete_exercise_sets.id)
    # create permissions allow clients to manage exercise_sets
    client_get_exercise_sets.insert()
    client_post_exercise_sets.insert()
    client_patch_exercise_sets.insert()
    client_delete_exercise_sets.insert()

    # define permissions allow clients to get clients (limited)
    client_get_clients = Role_Permission(role_id=trainer_role.id, permission_id=get_clients.id)
    # create permissions allow clients to get clients (limited)
    client_get_clients.insert()

    # define permissions allow clients to get trainers (limited)
    client_get_trainers = Role_Permission(role_id=trainer_role.id, permission_id=get_clients.id)
    # create permissions allow clients to get trainers (limited)
    client_get_trainers.insert()

    '''
    CREATE TEST ADMIN USER
    '''

    test_admin = User(email="test@admin", name="test admin", password="admin")
    test_admin.insert()
    test_admin_role = User_Role(test_admin.id, admin_role.id)
    test_admin_role.insert()

    '''
    CREATE TEST TRAINER USER
    '''

    test_trainer = User(email="test@trainer", name="test trainer", password="trainer")
    test_trainer.insert()
    test_trainer_role = User_Role(test_trainer.id, trainer_role.id)
    test_trainer_role.insert()

    '''
    CREATE TWO TEST CLIENT USERs
    '''

    test_client_one = User(email="test@trainee_one", name="test client one", password="password1")
    test_client_one.insert()
    test_client_one_role = User_Role(test_client_one.id, client_role.id)
    test_client_one_role.insert()

    test_client_two = User(email="test@trainee_two", name="test client two", password="password2")
    test_client_two.insert()
    test_client_two_role = User_Role(test_client_two.id, client_role.id)
    test_client_two_role.insert()

    return True

'''
PERMISSION MODEL
    This model defines a user permission.
'''

class Permission(db.Model):
    __tablename__ = 'Permission'

    '''Model Definition'''

    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)

    '''Init Method'''

    def __init__(self, name, description):
        self.name = name
        self.description = description

    '''
    Insert Method
        Inserts a new exercise model into the database.
        EXAMPLE:
            exercise = Exercise(name=req_name, description=req_description)
            exercise.insert()

    '''

    def insert(self):
        db.session.add(self)
        db.session.commit()

    '''
    Update Method
        Updates a new model into a database.
        The model must exist in the database.
        EXAMPLE:
            exercise = Exercise.query.filter(Exercise.id == id).one_or_none()
            exercise.name = 'New Name'
            exercise.update()
    '''

    def update(self):
        db.session.commit()

    '''
    Delete Method
        Deletes a new model into a database.
        The model must exist in the database.
        EXAMPLE:
            exercise = Exercise.query.filter(Exercise.id == id).one_or_none()
            exercise.delete()
    '''

    def delete(self):
        db.session.delete(self)
        db.session.commit()


'''
ROLE MODEL
'''

class Role(db.Model):

    __tablename__ = 'Role'

    '''Model Definition'''

    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    permissions = db.relationship('Role_Permission', backref='Role')

    '''Init Method'''

    def __init__(self, name, description):
        self.name = name
        self.description = description

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()


'''
ROLE PERMISSION MODEL
     This model maps predefined permission to a role.
'''


class Role_Permission(db.Model):

    __tablename__ = 'Role_Permission'

    '''Model Definition'''

    id = Column(Integer, primary_key=True)
    role_id = Column(Integer, ForeignKey('Role.id'))
    permission_id = Column(Integer, ForeignKey('Permission.id'))
    permission_definition = db.relationship("Permission", backref=db.backref("Role_Permission", uselist=False))

    '''Init Method'''

    def __init__(self, role_id, permission_id):
        self.role_id = role_id
        self.permission_id = permission_id

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()


'''
USER MODEL
'''


class User(db.Model):

    __tablename__ = 'User'

    '''Model Definition'''

    id = Column(Integer, primary_key=True)
    email = Column(String)
    name = Column(String)
    password = Column(String)
    roles = db.relationship('User_Role', backref='User')
    #workouts = db.relationship('User_Workout', backref='User')

    '''Init Method'''

    def __init__(self, email, name, password):
        self.email = email
        self.name = name
        self.password = password
        # self.roles = roles
        # self.workouts = workouts

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()


'''
USER ROLE MODEL
'''

class User_Role(db.Model):

    __tablename__ = 'User_Role'

    '''Model Definition'''

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('User.id'))
    role_id = Column(Integer, ForeignKey('Role.id'))
    role_definition = db.relationship("Role", backref=db.backref("User_Role", uselist=False))

    '''Init Method'''

    def __init__(self, user_id, role_id):
        self.user_id = user_id
        self.role_id = role_id

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()


# '''
# WORKOUT MODEL
# '''


# class Workout(db.Model):

#     __tablename__ = 'workout'

#     '''Model Definition'''

#     id = Column(Integer, primary_key=True)
#     name = Column(String)
#     description = Column(String)
#     exercises = db.relationship('workout_exercise', backref='workout')

#     '''Init Method'''

#     def __init__(self, name, description, exercises):
#         self.name = name
#         self.description = description
#         self.exercises = exercises

#     def insert(self):
#         db.session.add(self)
#         db.session.commit()

#     def update(self):
#         db.session.commit()

#     def delete(self):
#         db.session.delete(self)
#         db.session.commit()


# '''
# USER WORKOUT MODEL
# '''


# class User_Workout(db.Model):

#     __tablename__ = 'user_workout'

#     '''Model Definition'''

#     id = Column(Integer, primary_key=True)
#     date = Column(DateTime(timezone=False), nullable=False)
#     user_exercises = db.relationship('user_exercise', backref='user')
#     user_id = Column(Integer, ForeignKey('user.id'))
#     workout_id = Column(Integer, ForeignKey('workout.id'))

#     '''Init Method'''

#     def __init__(self, date, user_exercises, user_id, workout_id):
#         self.date = date
#         self.user_exercises = user_exercises
#         self.user_id = user_id
#         self.workout_id = workout_id

#     def insert(self):
#         db.session.add(self)
#         db.session.commit()

#     def update(self):
#         db.session.commit()

#     def delete(self):
#         db.session.delete(self)
#         db.session.commit()


# '''
# EXERCISE MODEL
# '''


# class Exercise(db.Model):

#     __tablename__ = 'exercise'

#     '''Model Definition'''

#     id = Column(Integer, primary_key=True)
#     name = Column(String)
#     description = Column(String)

#     '''Init Method'''

#     def __init__(self, name, description):
#         self.name = name
#         self.description = description

#     def insert(self):
#         db.session.add(self)
#         db.session.commit()

#     def update(self):
#         db.session.commit()

#     def delete(self):
#         db.session.delete(self)
#         db.session.commit()


# '''
# WORKOUT EXERCISE MODEL
# '''


# class Workout_Exercise(db.Model):

#     __tablename__ = 'workout_exercise'

#     '''Model Definition'''

#     id = Column(Integer, primary_key=True)
#     recommended_sets = Column(Integer)
#     exercise_id = Column(Integer, ForeignKey('exercise.id'))
#     workout_id = Column(Integer, ForeignKey('workout.id'))

#     '''Init Method'''

#     def __init__(self, recommended_sets, exercise_id, workout_id):
#         self.recommended_sets = recommended_sets
#         self.exercise_id = exercise_id
#         self.workout_id = workout_id

#     def insert(self):
#         db.session.add(self)
#         db.session.commit()

#     def update(self):
#         db.session.commit()

#     def delete(self):
#         db.session.delete(self)
#         db.session.commit()


# '''
# USER EXERCISE MODEL
#     This model is used to map user work outs to predefined exercises
#     these work out instances are also mapped to a recorded number of sets
#     in a one to many relationship
#     (one UserExercise maps to many Sets)
# '''


# class User_Exercise(db.Model):

#     __tablename__ = 'user_exercise'

#     '''Model Definition'''

#     id = Column(Integer, primary_key=True)
#     exercise_id = Column(Integer, ForeignKey('exercise.id'))
#     user_workout_id = Column(Integer, ForeignKey('user_workout.id'))
#     exercise_sets = db.relationship('exercise_set', backref='user_exercise')

#     '''Init Method'''

#     def __init__(self, sets, exercise_id, user_workout_id):
#         self.exercise_sets = exercise_sets
#         self.exercise_id = exercise_id
#         self.user_workout_id = user_workout_id

#     def insert(self):
#         db.session.add(self)
#         db.session.commit()

#     def update(self):
#         db.session.commit()

#     def delete(self):
#         db.session.delete(self)
#         db.session.commit()


# '''
# SET MODEL
#     This model is for an exercise set and is designed to
#     track weight, repetitions, rest, etc.
#     This model has a many to one relationship with the UserExercise Model
#     (Many Sets map to One User Exercise)
# '''

# CHANGE TO EXERCISE_SET
# class Exercise_Set(db.Model):

#     __tablename__ = 'exercise_set'

#     '''Model Definition'''

#     id = Column(Integer, primary_key=True)
#     weight = Column(Integer)
#     repetitions = Column(Integer)
#     rest = Column(Integer)
#     user_exercise_id = Column(Integer, ForeignKey('user_exercise.id'))

#     '''Init Method'''

#     def __init__(self, weight, repetitions, rest, user_exercise_id,):
#         self.weight = weight
#         self.repetitions = repetitions
#         self.rest = rest
#         self.user_exercise_id = user_exercise_id

#     def insert(self):
#         db.session.add(self)
#         db.session.commit()

#     def update(self):
#         db.session.commit()

#     def delete(self):
#         db.session.delete(self)
#         db.session.commit()
