# tpo/pattern_factory.py
class PatternFactory:
    def __init__(self):
        self.patterns = {}

    def register_pattern(self, name, pattern):
        self.patterns[name] = pattern

    def create_pattern(self, name, *args, **kwargs):
        if name not in self.patterns:
            raise ValueError(f"Pattern {name} not registered")

        pattern_class = self.patterns[name]
        return pattern_class(*args, **kwargs)

    @staticmethod
    def create_pattern_from_yaml(yaml_str):
        pattern_data = yaml.safe_load(yaml_str)

        if pattern_data['metadata']['name'] == 'datatier':
            return DataTierPattern(pattern_data['metadata'], pattern_data['definition'])
        else:
            raise ValueError(f"Unknown pattern: {pattern_data['metadata']['name']}")
