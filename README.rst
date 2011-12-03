Flask REST
##########

This library is a tiny REST toolkit intending to simplify your life when you
want to create a REST API for your flask apps.

Install it
==========

Well, that's really simple, it's packaged and on PyPI, so::

    $ pip install flask-rest

Use it
======

Handlers
--------

Create your classes with specific methods (namely add, get, delete and update),
register it with an url, and you're good.


Here is a simple example on how to use it::

    from flask import Blueprint
    from flask_rest import RESTResource, need_auth

    # Subclass a RestResource and configure it

    api = Blueprint("api", __name__, url_prefix="/api")

    # You can define a authenfier if you want to.

    class ProjectHandler(object):

        def add(self): #This maps on "post /"
            form = ProjectForm(csrf_enabled=False) # just for the example
            if form.validate():
                project = form.save()
                db.session.add(project)
                db.session.commit()
                return 201, project.id
            return 400, form.errors # returns a status code and the data

        def get(self, project_id): # maps on GET /<id>
            # do your stuff here
            return 200, project

        # you can use the "need_auth" decorator to do things for you
        @need_auth(authentifier_callable, "project") # injects the "project" argument if authorised 
        def delete(self, project):
            # do your stuff
            return 200, "DELETED"


Once your handlers defined, you just have to register them with the app or the
blueprint::

    project_resource = RESTResource(
        name="project", # name of the var to inject to the methods
        route="/projects",  # will be availble at /api/projects/*
        app=api, # the app which should handle this
        actions=["add", "update", "delete", "get"], #authorised actions
        handler=ProjectHandler()) # the handler of the request

If everything should be protected, you can use the `authentifier` argument::

    authentifier=check_project

Where `check_project` is a callable that returns either the project or False if
the acces is not authorized.

Serialisation / Deserialisation
-------------------------------

When you are returning python objects, they can be serialized, which could be
useful in most of the cases. The only serialisation format supported so far is
JSON. 

To serialise *normal* python objects, they should have a `_to_serialize`
attribute, containing all the names of the attributes to serialize. Here is an
example::


    class Member():

        _to_serialize = ("id", "name", "email")

        def __init__(self, **kwargs):
            for name, value in kwargs.items():
                setattr(self, name, value)

If you want to have a look at a real use for this, please head to
https://github.com/spiral-project/ihatemoney/blob/master/budget/api.py
