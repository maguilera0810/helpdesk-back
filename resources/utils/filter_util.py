# .\resources\utils\filter_util.py
class FilterUtil:
    @staticmethod
    def get_list_filters(data: dict[str, str]) -> dict[dict]:
        if not data:
            return {}
        incl_prefix = "incl_"
        excl_prefix = "excl_"
        list_sufix = "__in"
        incl_filters = {}
        excl_filters = {}
        for k, v in data.items():
            is_list = k.endswith(list_sufix)
            if k.startswith(excl_prefix):
                key = k.split(excl_prefix)[-1]
                excl_filters[key] = v.split(",") if is_list else v
            elif k.startswith(incl_prefix):
                key = k.split(incl_prefix)[-1]
                incl_filters[key] = v.split(",") if is_list else v
            else:
                key = k
                incl_filters[key] = v.split(",") if is_list else v
        return {"incl_filters": incl_filters, "excl_filters": excl_filters}
