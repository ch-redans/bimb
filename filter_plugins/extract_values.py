class FilterModule(object):
    def filters(self):
        return {
            'extract_values': self.extract_values
        }

    def extract_values(self, items, mappings):
        results = []
        for item in items:
            if not isinstance(item, dict):
                raise ValueError(f"Expected dictionary, got {type(item)}: {item}")

            result = {}
            for key, path in mappings.items():
                # Navigate nested dictionaries
                value = item
                for part in path.split('/'):
                    if isinstance(value, dict):
                        value = value.get(part, None)
                    else:
                        value = None
                result[key] = value if value is not None else ""
            results.append(result)
        return results

