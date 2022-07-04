import os
from logging.config import fileConfig
from sqlalchemy import engine_from_config
from sqlalchemy import pool
import sqlalchemy_utils
from alembic import context
import database
# modesls.* はコードないで使わないが、importしないとdatabase.Baseのmetadataにモデルが登録されず、
# alembicでmigrationファイルを作成した際に認識されないので注意
import models.department
import models.employee
import models.tag
import models.work
import models.work_tag

# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config

# connect to database
DB_USER = os.environ.get('MYSQL_USER')
DB_PASSWORD = os.environ.get('MYSQL_PASSWORD')
DB_ROOT_PASSWORD = os.environ.get('MYSQL_ROOT_PASSWORD')
DB_HOST = os.environ.get('MYSQL_HOST')
DB_NAME = os.environ.get('MYSQL_DATABASE')

DATABASE = 'mysql://%s:%s@%s/%s?charset=utf8' % (
    DB_USER,
    DB_PASSWORD,
    DB_HOST,
    DB_NAME,
)
config.set_main_option('sqlalchemy.url', DATABASE)

# Interpret the config file for Python logging.
# This line sets up loggers basically.
fileConfig(config.config_file_name)

# add your model's MetaData object here
# for 'autogenerate' support
# from myapp import mymodel
# target_metadata = mymodel.Base.metadata
target_metadata = database.Base.metadata
# target_metadata = None

# other values from the config, defined by the needs of env.py,
# can be acquired:
# my_important_option = config.get_main_option("my_important_option")
# ... etc.


# UUIDを使う場合に必要
# def render_item(type_, obj, autogen_context):
#     """Apply custom rendering for selected items."""

#     if type_ == 'type' and isinstance(
#             obj, sqlalchemy_utils.types.uuid.UUIDType):
#         # add import for this type
#         autogen_context.imports.add("import sqlalchemy_utils")
#         autogen_context.imports.add("import uuid")
#         return "sqlalchemy_utils.types.uuid.UUIDType(binary=False), default=uuid.uuid4"

#     # default rendering for other objects
#     return False


def run_migrations_offline():
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.

    """
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online():
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.

    """
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            # UUIDを使う場合に必要
            # render_item=render_item
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()

