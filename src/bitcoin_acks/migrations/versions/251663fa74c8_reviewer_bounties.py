"""reviewer bounties

Revision ID: 251663fa74c8
Revises: e9766272137f
Create Date: 2020-09-28 14:29:48.019803

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '251663fa74c8'
down_revision = 'e9766272137f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('bounties_recipient_user_id_fkey', 'bounties', type_='foreignkey')
    op.drop_column('bounties', 'recipient_user_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('bounties', sa.Column('recipient_user_id', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.create_foreign_key('bounties_recipient_user_id_fkey', 'bounties', 'users', ['recipient_user_id'], ['id'])
    # ### end Alembic commands ###
