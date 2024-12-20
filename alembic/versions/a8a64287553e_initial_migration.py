"""Initial migration

Revision ID: a8a64287553e
Revises: 8e47143a8b0d
Create Date: 2024-12-01 17:16:20.617411

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a8a64287553e'
down_revision: Union[str, None] = '8e47143a8b0d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('products', 'price',
               existing_type=sa.INTEGER(),
               type_=sa.Float(),
               existing_nullable=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('products', 'price',
               existing_type=sa.Float(),
               type_=sa.INTEGER(),
               existing_nullable=False)
    # ### end Alembic commands ###
