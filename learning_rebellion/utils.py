from learning_rebellion.models import Page


def get_page(slug):
    try:
        page = Page.objects.get(slug=slug,active=True)
    except Page.DoesNotExist:
        return None
    return page