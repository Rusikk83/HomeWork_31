from rest_framework import routers



from ads.views.views_selection import SelectionViewSet

router_selection = routers.SimpleRouter()
router_selection.register('selection', SelectionViewSet)
