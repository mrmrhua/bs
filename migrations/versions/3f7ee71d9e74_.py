"""empty message

Revision ID: 3f7ee71d9e74
Revises: 9f328e0f6013
Create Date: 2016-05-31 16:56:36.058285

"""

# revision identifiers, used by Alembic.
revision = '3f7ee71d9e74'
down_revision = '9f328e0f6013'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Relationship', sa.Column('friend_b', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'Relationship', 'User', ['friend_b'], ['id'])
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'Relationship', type_='foreignkey')
    op.drop_column('Relationship', 'friend_b')
    ### end Alembic commands ###