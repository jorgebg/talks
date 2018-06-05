from rest_framework.routers import SimpleRouter

from user.views import UserViewSet

router = SimpleRouter()
router.register(r'users', UserViewSet, base_name='user')
urlpatterns = router.urls
