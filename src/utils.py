from flask import Blueprint


class NestableBlueprint(Blueprint):
    """
    Hacking in support for nesting blueprints,
    until hopefully https://github.com/mitsuhiko/flask/issues/593 will be resolved
    """

    def register_blueprint(self, blueprint, **options):
        def deferred(state):
            url_prefix = (state.url_prefix or '') + (options.get('url_prefix', blueprint.url_prefix) or '')
            if 'url_prefix' in options:
                del options['url_prefix']

            state.app.register_blueprint(blueprint, url_prefix=url_prefix, **options)

        self.record(deferred)

    def register_view(self, view, url, pk='id', pk_type='int'):
        self.add_url_rule(url, defaults={pk: None}, view_func=view, methods=['GET', ])
        self.add_url_rule(url, view_func=view, methods=['POST', ])
        self.add_url_rule('%s<%s:%s>/' % (url, pk_type, pk), view_func=view, methods=['GET', 'PUT', 'DELETE'])
