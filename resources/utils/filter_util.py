# .\resources\utils\filter_util.py
from resources.utils.crypto_util import CryptoUtil


class FilterUtil:

    @classmethod
    def get_list_filters(cls, data: dict[str, str], n: int = 2) -> dict[str, dict]:

        data = cls.parser_queryparams(data, n)

        incl_prefix, excl_prefix, order_key, list_suffix = "incl_", "excl_", "order_by", "__in"
        incl_filters, excl_filters, order = {}, {}, []

        if v := data.get(order_key):
            order = v.split(",") if "," in v else [v]
            del data[order_key]

        for key, v in data.items():
            values = v.split(",") if key.endswith(
                list_suffix) or "," in v else v

            if key.startswith(excl_prefix):
                excl_filters[key.removeprefix(excl_prefix)] = values
            elif key.startswith(incl_prefix):
                incl_filters[key.removeprefix(incl_prefix)] = values
            else:
                incl_filters[key] = values
        return {
            "incl_filters": incl_filters,
            "excl_filters": excl_filters,
            "order": order,
        }

    @classmethod
    def parser_queryparams(cls, data: dict[str, str], n: int = 2) -> dict[str, dict]:
        if not data:
            return {}
        if q := data.get("q"):
            data = CryptoUtil.decode_base64(q, n)
        return data
