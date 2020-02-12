"""create series table

Revision ID: 710794468fbe
Revises: 88a855c2eda7
Create Date: 2020-02-07 17:22:28.314180

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '710794468fbe'
down_revision = '88a855c2eda7'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "series",
        sa.Column("id", sa.Integer, primary_key=True, index=True),
        sa.Column("title", sa.String(64), nullable=False)
    )


def downgrade():
    op.drop_table("series")
