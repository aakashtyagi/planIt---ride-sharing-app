from mb_api.decorators import api_view
from mb_api.response import Response
from datetime import datetime

@api_view()
def test_view(request, format=None):
    return Response({"CurrentTime": datetime.now()})
test_api = test_view