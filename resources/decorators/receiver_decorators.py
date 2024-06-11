from django.dispatch import receiver


def register_receivers(signal, models):
    def decorator(func):
        for model in models:
            receiver(signal, sender=model)(func)
        return func

    return decorator
