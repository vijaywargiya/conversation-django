"""cartloop URL Configuration

The `urlpatterns` list routes URLs to 1_views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function 1_views
    1. Add an import:  from my_app import 1_views
    2. Add a URL to urlpatterns:  path('', 1_views.home, name='home')
Class-based 1_views
    1. Add an import:  from other_app.1_views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from rest_framework.routers import SimpleRouter

from cartloop.views import ConversationViewSet, ChatViewSet, UserViewSet, ClientViewSet, OperatorViewSet, \
    DiscountCodeViewSet, StoreViewSet

router = SimpleRouter(trailing_slash=False)
router.register('conversation', ConversationViewSet, basename='conversation')
router.register('chat', ChatViewSet)
router.register('user', UserViewSet)
router.register('discount_code', DiscountCodeViewSet)
router.register('store', StoreViewSet)
router.register('client', ClientViewSet)
router.register('operator', OperatorViewSet)

urlpatterns = router.urls + [
    path('admin/', admin.site.urls),
]
