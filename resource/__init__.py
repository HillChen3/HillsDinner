from flask_restplus import Api

from resource.CommGroup import api as group
from resource.GroupNews import api as news
from resource.GroupUserVerify import api as user_verify
from resource.Operation import api as operation
from resource.Session import api as session
from resource.SMS import api as SMS
from resource.User import api as user

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