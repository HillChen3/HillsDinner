from flask_restplus import Api

# from apis.group import api as group
# from apis.news import api as news
# from apis.userVerify import api as user_verify
# from apis.operation import api as operation
# from apis.session import api as session
# from apis.SMS import api as SMS
from apis.user import api as user

api = Api(
    title='ace-youth',
    version='0.11',
    description='restful apis for ace youth',
    # All API metadatas
)

# api.add_namespace(group)
# api.add_namespace(news)
# api.add_namespace(user_verify)
# api.add_namespace(operation)
# api.add_namespace(session)
# api.add_namespace(SMS)
api.add_namespace(user)
