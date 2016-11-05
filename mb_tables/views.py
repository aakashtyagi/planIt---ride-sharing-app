from mb_api.response import Response
from django.core.paginator import Paginator
from mb_api.views import APIView

class TableApi(APIView):
    page_limit = 10
    page_number = 0
    sort_name = None
    sort_order = None
    search = None
    total = 1

    def parse_options(self, request):
        self.page_limit = int(request.GET.get('pageSize', 10))
        self.page_number = int(request.GET.get('pageNumber', 1))
        self.sort_name = request.GET.get('sortName', None)
        self.sort_order = request.GET.get('sortOrder', None)
        self.search = request.GET.get('searchPhrase', None)

    def get(self, request, format=None):
        self.parse_options(request)
        queryset = self.get_queryset(request)
        if queryset:
            queryset = self.apply_options(queryset)
            res = dict()
            res['rows'] = self.get_rows(queryset, request=request)
            res['total'] = self.total
            return Response(res)
        else:
            print "TableApi Query Returned None"
            return Response({'rows': [], 'total': 0})

    def get_rows(self, queryset, request=None):
        return list()

    def apply_options(self, queryset):
        if self.sort_name:
            if self.sort_order == 'desc':
                queryset = queryset.order_by('-%s' % self.sort_name )
            else:
                queryset = queryset.order_by(self.sort_name)
        p = Paginator(queryset, self.page_limit)
        self.total = p.count
        return p.page(self.page_number)


    def get_queryset(self, request):
        return None