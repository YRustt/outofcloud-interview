from .views import news, grub, grubs, register


def setup_routes(application):
    application.router.add_get('/api/news', news)
    application.router.add_get('/api/grub', grub)
    application.router.add_post('/api/grubs', grubs)
    application.router.add_post('/api/register', register)
