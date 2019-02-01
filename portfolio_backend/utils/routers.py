from rest_framework.routers import DefaultRouter


class ExtendedDefaultRouter(DefaultRouter):
    def register_router(self, router):
        self.registry.extend(router.registry)

    def register_routers(self, *routers):
        for router in routers:
            self.register_router(router)
