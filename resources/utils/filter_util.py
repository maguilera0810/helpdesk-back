class FilterUtil:
    @staticmethod
    def get_list_filters(data: dict[str, str]) -> dict[dict]:
        if not data:
            return {}
        incl_prefix = "incl_"
        excl_prefix = "excl_"
        incl_filters = {}
        excl_filters = {}
        for k, v in data.items():
            if k.startswith(excl_prefix):
                key = k.split(excl_prefix)[-1]
                excl_filters[key] = v
            elif k.startswith(incl_prefix):
                key = k.split(incl_prefix)[-1]
                incl_filters[key] = v
            else:
                key = k
                incl_filters[key] = v
        return {"incl_filters": incl_filters, "excl_filters": excl_filters}
