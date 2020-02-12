"""create products table

Revision ID: d4e897cc4f57
Revises: e278c1e86cf0
Create Date: 2020-02-07 17:45:17.597080

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd4e897cc4f57'
down_revision = 'e278c1e86cf0'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "products",
        sa.Column("id", sa.Integer, primary_key=True, index=True),
        sa.Column("group_id", sa.Integer, sa.ForeignKey("groups.id"), index=True),
        sa.Column("series_id", sa.Integer, sa.ForeignKey("series.id"), index=True),
        sa.Column("slug", sa.String(32), nullable=False, index=True, unique=True),
        sa.Column("type", sa.Enum("digital", "audio", "printed", name="producttype"), nullable=False),
        sa.Column("price", sa.Integer),
        sa.Column("urls", sa.String(1024)),
        sa.Column("publisher", sa.String(256)),
        sa.Column("year_published", sa.Integer)
    )


def downgrade():
    op.drop_table("products")
