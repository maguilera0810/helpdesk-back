# .\resources\utils\filter_util.py

class FilterUtil:

    @staticmethod
    def get_list_filters(data: dict[str, str]) -> dict[str, dict]:
        if not data:
            return {}

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
