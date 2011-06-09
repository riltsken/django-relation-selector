from django.db.models.loading import cache as APPCACHE
from django.utils import simplejson
from django.http import HttpResponse

class relation_select(object):

	def __new__(cls, request, *args, **kwargs):
		obj = super(relation_select,cls).__new__(cls)
		return obj(request, *args, **kwargs)

	def __call__(cls, request):
		app_name = request.GET.get('app_name','')
		model_name = request.GET.get('model','')
		model = APPCACHE.get_model(app_name, model_name)
		if model:
			return HttpResponse(simplejson.dumps(cls.get_context(model)), mimetype='application/json')

		return HttpResponse(simplejson.dumps({}), mimetype='application/json')

	def get_non_relation_fields(self, model):
		return [(f.name, f.model._meta.object_name, f.model._meta.app_label) for f in model._meta.fields if not hasattr(f.rel, "to")]

	def get_forward_relations(self, model):
		return [(f.name, f.rel.to._meta.object_name, f.rel.to._meta.app_label) for f in model._meta.fields if hasattr(f.rel, "to")]

	def get_backward_relations(self, model):
		return [(r.field.related_query_name(), r.model._meta.object_name, r.model._meta.app_label) for r in model._meta.get_all_related_objects()]

	def get_context(self, model):
		return {'fields': self.get_non_relation_fields(model), 'relations': self.get_forward_relations(model) + self.get_backward_relations(model)}
