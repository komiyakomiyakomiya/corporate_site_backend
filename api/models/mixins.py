from sqlalchemy import Column, Integer, text
from sqlalchemy.dialects.mysql import TIMESTAMP as Timestamp
from sqlalchemy.dialects.mysql import DATETIME
# from sqlalchemy_utils import UUIDType
# from uuid import uuid4


class Mixin(object):
    # uuid = Column(UUIDType(binary=False), primary_key=True, default=uuid4)
    # created_at = Column(Timestamp,
    #                     server_default=text('current_timestamp'),
    #                     nullable=False)
    # updated_at = Column(Timestamp,
    #                     server_default=text('current_timestamp on update current_timestamp'),
    #                     nullable=False)

    id = Column(Integer,
                primary_key=True,
                autoincrement=True,
                index=True)
    created_at = Column(DATETIME,
                        server_default=text('CURRENT_TIMESTAMP'),
                        nullable=False)
    updated_at = Column(DATETIME,
                        server_default=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'),
                        nullable=False)
    del_flg = Column(Integer,
                     default=0,
                     nullable=False)
