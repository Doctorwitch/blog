from django.conf.urls import url
from user.views import Register, Index, About, Login, Active

urlpatterns = [
    url(r'^register$', Register.as_view(), name='register'),
    url(r'^active/(?P<token>.*)$', Active.as_view(), name='用户激活'),
    url(r'^login$', Login.as_view(), name='login'),
    url(r'^about$', About.as_view(), name='about'),
    url(r'^index$', Index.as_view(), name='index'),
    url(r'^$', Index.as_view(), name='index'),
]
