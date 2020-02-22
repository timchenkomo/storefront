"""add fields signup_date, last_signin_date to the User table

Revision ID: 24402a686d71
Revises: fa941231b167
Create Date: 2020-02-22 14:00:57.806893

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '24402a686d71'
down_revision = 'fa941231b167'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('users', sa.Column('signup_date', sa.DateTime(), nullable=True))
    op.add_column('users', sa.Column('last_signin_date', sa.DateTime(), nullable=True))


def downgrade():
    op.drop_column('signup_date', 'last_signin_date')

