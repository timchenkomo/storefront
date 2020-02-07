"""create purchases table

Revision ID: e365a7ec9717
Revises: d4e897cc4f57
Create Date: 2020-02-07 18:17:28.362451

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e365a7ec9717'
down_revision = 'd4e897cc4f57'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "purchases",
        sa.Column("id", sa.Integer, primary_key=True, index=True),
        sa.Column("invoice_id", sa.Integer, nullable=False, index=True),
        sa.Column("user_id", sa.Integer, sa.ForeignKey("users.id"), index=True),
        sa.Column("product_id", sa.Integer, sa.ForeignKey("products.id"), index=True),
        sa.Column("price", sa.Integer),
        sa.Column("date", sa.DateTime, nullable=False),
        sa.Column("paid", sa.Boolean, nullable=False, default=False)
    )


def downgrade():
    op.drop_table("purchases")
