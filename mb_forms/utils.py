from datetime import datetime
from codecs import encode

def form_store_session(request, form, prefix=None):
    s = request.session
    for k in form.cleaned_data:
        data = form.cleaned_data[k]
        if type(data) is not datetime.time:
            data = str(data)

        data = encode(data, 'utf8')    
        if prefix is not None:
            s['%s_%s' % (prefix, k)] = str(data)
        else:
            s[k] = str(data)
    s.save()




