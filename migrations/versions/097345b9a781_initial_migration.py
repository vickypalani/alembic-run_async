"""Initial migration

Revision ID: 097345b9a781
Revises: 
Create Date: 2024-06-29 22:39:34.244325

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from migrations.permissions import create_permissions, delete_permissions


# revision identifiers, used by Alembic.
revision: str = "097345b9a781"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "permissions",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(), nullable=False),
        sa.Column("display_name", sa.String(), nullable=False),
        sa.Column("description", sa.String(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("display_name"),
        sa.UniqueConstraint("name"),
    )
    op.create_table(
        "users",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.run_async(async_function=create_permissions, kw_args={"table": "users"})
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("users")
    op.run_async(async_function=delete_permissions, kw_args={"table": "users"})
    op.drop_table("permissions")
    # ### end Alembic commands ###