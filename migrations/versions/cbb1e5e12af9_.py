"""empty message

Revision ID: cbb1e5e12af9
Revises: bff17ff82ef3
Create Date: 2018-03-24 14:38:37.893606

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cbb1e5e12af9'
down_revision = 'bff17ff82ef3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('system_resource_used',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('cpu_count', sa.Integer(), nullable=True),
    sa.Column('cpu_used_percent', sa.Text, nullable=True),
    sa.Column('mem_total', sa.BigInteger(), nullable=True),
    sa.Column('mem_user_percent', sa.Float(precision=2), nullable=True),
    sa.Column('net_send_total', sa.BigInteger(), nullable=True),
    sa.Column('net_recv_total', sa.BigInteger(), nullable=True),
    sa.Column('net_upstream', sa.Integer(), nullable=True),
    sa.Column('net_downstream', sa.Integer(), nullable=True),
    sa.Column('timestamp', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('system_resource_used')
    # ### end Alembic commands ###