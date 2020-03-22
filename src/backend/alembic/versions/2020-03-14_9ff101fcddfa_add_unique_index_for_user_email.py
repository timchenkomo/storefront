"""Add unique index for user.email

Revision ID: 9ff101fcddfa
Revises: 24402a686d71
Create Date: 2020-03-14 16:00:05.339230

"""
from alembic import op


# revision identifiers, used by Alembic.
revision = '9ff101fcddfa'
down_revision = '24402a686d71'
branch_labels = None
depends_on = None


def upgrade():
    op.create_unique_constraint("users_email_uindex", "users", ["email"])
    pass


def downgrade():
    op.drop_constraint("users_email_uindex", "users")
    pass
