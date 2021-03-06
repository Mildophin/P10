from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import (ProjectsViewSet,
                    CommentsViewSet,
                    ContributorsViewSet,
                    IssuesViewSet, RegisterUsers,
                    )


router = routers.DefaultRouter()
router.register(r"", ProjectsViewSet, basename="projects")
router.register(r"^(?P<id>[^/.]+)/users", ContributorsViewSet, basename="users")
router.register(r"^(?P<id>[^/.]+)/issues", IssuesViewSet, basename="issues")
router.register(r"^(?P<id>[^/.]+)/issues/(?P<issue_id>[^/.]+)/comments", CommentsViewSet, basename="comments")


urlpatterns = [
    path('projects/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('signup/', RegisterUsers.as_view(), name='signup')

]
