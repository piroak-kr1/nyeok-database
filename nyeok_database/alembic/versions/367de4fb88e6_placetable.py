"""Placetable

Revision ID: 367de4fb88e6
Revises: 255d354c72cc
Create Date: 2024-08-21 14:26:42.353283

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '367de4fb88e6'
down_revision: Union[str, None] = '255d354c72cc'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('place',
    sa.Column('contentid', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(), nullable=False),
    sa.Column('firstimage2', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('contentid')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('place')
    # ### end Alembic commands ###
