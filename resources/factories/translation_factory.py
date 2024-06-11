from django.conf import settings

from resources.gateways.translation import BaseTranslationGateway, WeblateGateway

MAIN_PROVIDER = settings.MAIN_TRANSLATION_PROVIDER


class TranslationFactory:
    @staticmethod
    def get_provider(provider: str = MAIN_PROVIDER) -> BaseTranslationGateway:
        if provider == "weblate":
            return WeblateGateway()
        else:
            raise ValueError(f"Unsupported translation service: {provider}")
