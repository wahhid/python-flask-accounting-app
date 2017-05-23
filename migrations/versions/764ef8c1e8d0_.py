"""empty message

Revision ID: 764ef8c1e8d0
Revises: 9db5fdec9986
Create Date: 2017-05-22 08:06:05.870985

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '764ef8c1e8d0'
down_revision = '9db5fdec9986'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('account',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=24), nullable=False),
    sa.Column('type', sa.String(length=36), nullable=False),
    sa.Column('cost', sa.Integer(), nullable=False),
    sa.Column('time', sa.DateTime(), nullable=False),
    sa.Column('created_at', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('account')
    # ### end Alembic commands ###