from .views import news, grub, grubs


def setup_routes(application):
    application.router.add_get('/news', news)
    application.router.add_get('/grub', grub)
