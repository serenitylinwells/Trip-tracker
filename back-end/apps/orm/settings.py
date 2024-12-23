TORTOISE_ORM = {
    "connections": {"default": "sqlite://apps/orm/sqlite.db"},
    "apps": {
        "models": {
            "models": ["apps.orm.models"],
            "default_connection": "default",
        },
    },
}
