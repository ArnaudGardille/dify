import argparse
from app import app, db  # Import your Flask app

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models.account import Account, Tenant, TenantAccountJoin
def print_attributes(obj):
    """Prints the attributes and their values of any object."""
    for attribute in dir(obj):
        # Skip built-in attributes
        if not attribute.startswith('__'):
            value = getattr(obj, attribute)
            print(f"{attribute}: {value}")

def list_accounts(db_url):
    engine = create_engine(db_url)
    Session = sessionmaker(bind=engine)
    session = Session()

    tenants = session.query(Tenant).all()

    for tenant in tenants:
        print_attributes(tenant)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="List account names, IDs, emails, and associated workspaces with IDs and roles")
    parser.add_argument("--db_url", help="Database connection URL", default="postgresql://postgres:difyai123456@docker-db-1/dify")
    args = parser.parse_args()

    with app.app_context():
        list_accounts(args.db_url)
