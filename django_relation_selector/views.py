from django.db.models.loading import cache as APPCACHE
from django.utils import simplejson
from django.http import HttpResponse

def relation_select(request):

	app_name = request.GET.get('app_name','')
	model_name = request.GET.get('model','')
	model = APPCACHE.get_model(app_name, model_name)
	if model:
		non_relation_fields = [(f.name, f.model._meta.object_name, f.model._meta.app_label) for f in model._meta.fields if not hasattr(f.rel, "to")]
		forward_relations = [(f.name, f.rel.to._meta.object_name, f.rel.to._meta.app_label) for f in model._meta.fields if hasattr(f.rel, "to")]
		backward_relations = [(r.field.related_query_name(), r.model._meta.object_name, r.model._meta.app_label) for r in model._meta.get_all_related_objects()]

		return HttpResponse(simplejson.dumps({'fields': non_relation_fields, 'relations': forward_relations + backward_relations}), mimetype='application/json')

	return HttpResponse(simplejson.dumps({}), mimetype='application/json')
