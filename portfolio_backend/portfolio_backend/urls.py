"""portfolio_backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import include, path
from rest_framework_swagger.views import get_swagger_view

from person.urls import PERSON_ROUTER
from social.urls import SOCIAL_ROUTER
from project.urls import PROJECT_ROUTER, PROJECT_DESCRIPTION_ROUTER
from skill.urls import SKILL_ROUTER, SKILL_CATEGORY_ROUTER
from experience.urls import EXPERIENCE_ROUTER, EXPERIENCE_DESCRIPTION_ROUTER
from utils.routers import ExtendedDefaultRouter

ROUTER = ExtendedDefaultRouter()
ROUTER.register_routers(
    SOCIAL_ROUTER,
    PERSON_ROUTER,
    PROJECT_ROUTER,
    PROJECT_DESCRIPTION_ROUTER,
    SKILL_ROUTER,
    SKILL_CATEGORY_ROUTER,
    EXPERIENCE_ROUTER,
    EXPERIENCE_DESCRIPTION_ROUTER,
)

SCHEMA_VIEW = get_swagger_view(title='Portfolio API')

urlpatterns = [
    url(r'^swagger$', SCHEMA_VIEW),
    path('', include(ROUTER.urls)),
    path('admin/', admin.site.urls),
]
