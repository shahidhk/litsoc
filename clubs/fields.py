from django_select2 import *

class SelfMultiChoices(AutoSelect2MultipleField):
    big_data = []

    def validate_value(self, value):
        if value in [v for v in self.big_data]:
            return True
        else:
            return False

    def coerce_value(self, value):
        return value

    def get_val_txt(self, value):
        if not hasattr(self, '_big_data'):
            self._big_data = dict(self.big_data)
        return self._big_data.get(value, None)

    def get_results(self, request, term, page, context):
        if not hasattr(self, '_big_data'):
            self._big_data = dict(self.big_data)
        res = [(v, self._big_data[v]) for v in self._big_data]
        res.insert(0,(term, term,))
        res = res[:2]
        self._big_data[term] = term
        self.choices = res
        return (NO_ERR_RESP, False, res)
