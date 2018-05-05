from flask_restplus import Api

from apis.Group import api as group
from apis.News import api as news
from apis.UserVerify import api as user_verify
from apis.Operation import api as operation
from apis.Session import api as session
from apis.SMS import api as SMS
from apis.User import api as user

api = Api(
    title='ace-youth',
    version='0.11',
    description='restful apis for ace youth',
    # All API metadatas
)

api.add_namespace(group)
api.add_namespace(news)
api.add_namespace(user_verify)
api.add_namespace(operation)
api.add_namespace(session)
api.add_namespace(SMS)
api.add_namespace(user)
