# filter_plugins/expand_days.py
class FilterModule(object):
    def filters(self):
        return {
            'expand_days': self.expand_days
        }

    def expand_days(self, input_days):
        days_mapping = {
            'MO': 'Monday',
            'TU': 'Tuesday',
            'WE': 'Wednesday',
            'TH': 'Thursday',
            'FR': 'Friday',
            'SA': 'Saturday',
            'SU': 'Sunday',
        }

        result = []

        for day_set in input_days:
            start, _, end = day_set.partition('-')
            if end:
                result.extend([days_mapping[day] for day in days_mapping if start <= day <= end])
            else:
                result.append(days_mapping[start])

        return ','.join(result)

