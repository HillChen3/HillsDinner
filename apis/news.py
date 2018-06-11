from flask_restplus import Resource, abort, reqparse, Namespace, fields
from models.models import group_model, operation_model, group_user_verify_model, user_model, group_news_model
from playhouse.shortcuts import model_to_dict, dict_to_model
from models.models import Group, User, GroupUserRelation, GroupNews

api = Namespace('GroupNews', description="event or new in group")
in_progress = "Interface is still in progress"
group_news_model = api.model('GroupNewsModel', group_news_model)
APIS = {
    'group-news': {'task': 'the event or message published by group'}
}
parser = reqparse.RequestParser()


def abort_if_todo_doesnt_exist(api_id):
    if api_id not in APIS:
        abort(404, message="API {} doesn't exist".format(api_id))

@api.route('/news/<news_id>')
class SingleGroupNews(Resource):
    @api.marshal_with(group_news_model)
    def get(self, news_id):
        group_news = GroupNews.get_or_none(GroupNews.id == news_id)
        if not group_news:
            return 'news not find', 204
        return group_news, 200

    @api.doc(body=group_news_model)
    def put(self, news_id):
        for key, value in group_news_model.items():
            parser.add_argument(key, type=str, required=True)
        args = parser.parse_args()
        if not args['create_time']:
            args.pop('create_time', None)
        group_news = dict_to_model(GroupNews, args)
        group_news.id = news_id
        group_news.save()
        return 'success', 200

    def delete(self, news_id):
        group_new = GroupNews.get_or_none(GroupNews.id == news_id)
        if not group_new:
            return 'group new not find', 204
        group_new.delete_instance()
        return 'success', 200