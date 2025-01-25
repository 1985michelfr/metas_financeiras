"""add priority to goals

Revision ID: 2024_03_19_add_priority
Revises: previous_revision_id
Create Date: 2024-03-19 10:00:00.000000

"""
""" from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '2024_03_19_add_priority'
down_revision = 'previous_revision_id'  # coloque aqui o ID da última revisão
branch_labels = None
depends_on = None

def upgrade():
    op.add_column('goal', sa.Column('priority', sa.Integer(), nullable=True))
    # Define um valor padrão para as metas existentes
    op.execute('UPDATE goal SET priority = 0 WHERE priority IS NULL')
    
def downgrade():
    op.drop_column('goal', 'priority')  """