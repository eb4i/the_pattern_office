class DataTierPattern(Pattern):
    def __init__(self, metadata, definition):
        super().__init__(metadata['name'])
        self._metadata = metadata
        self._definition = definition

    def get_metadata(self):
        return self._metadata

    def get_definition(self):
        return self._definition

    def __str__(self):
        return f"{self._metadata['display_name']} ({self._metadata['version']})"
