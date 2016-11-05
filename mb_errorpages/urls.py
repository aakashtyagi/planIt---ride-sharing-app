from django.conf.urls import handler500, handler400, handler403, handler404

handler500 = 'mb_errorpages.views.error_500'
handler400 = 'mb_errorpages.views.error_400'
handler403 = 'mb_errorpages.views.error_403'
handler404 = 'mb_errorpages.views.error_404'
