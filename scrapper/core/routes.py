from .views import news, grub, grubs, register


def setup_routes(application):
    application.router.add_get('/news', news)
    application.router.add_get('/grub', grub)
    application.router.add_post('/grubs', grubs)
    application.router.add_post('/register', register)
