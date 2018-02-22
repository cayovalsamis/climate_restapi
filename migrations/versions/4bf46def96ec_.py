"""empty message

Revision ID: 4bf46def96ec
Revises: 
Create Date: 2018-02-21 15:31:37.140237

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4bf46def96ec'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('climate_data',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('date', sa.String(length=64), nullable=True),
    sa.Column('temperature', sa.String(length=120), nullable=True),
    sa.Column('rainfall', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('climate_data')
    # ### end Alembic commands ###
