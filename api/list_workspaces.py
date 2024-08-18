import argparse
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models.account import Account, Tenant, TenantAccountJoin
from services.account_service import TenantService
from app import app  # Import your Flask app

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
    print("Workspaces: ")
    for tenant in tenants:
        print_attributes(tenant)
        print("\n")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="List account names, IDs, emails, and associated workspaces with IDs and roles")
    parser.add_argument("--db_url", help="Database connection URL", default="postgresql://postgres:difyai123456@docker-db-1/dify")
    # postgresql://postgres:difyai123456@localhost:5432/dify
    args = parser.parse_args()

    # Use the application context
    with app.app_context():
        TenantService.create_owner_tenant_if_not_exist(account)
        TenantService.create_tenant_member(tenant, account, 'admin')
        TenantService.get_tenant_count()
        
        tenant = TenantService.create_tenant("Test")
        
        
        
        TenantService.create_owner_tenant_if_not_exist(account)
        
        account = AccountService.authenticate("arnaud.gardille@vigie.ai", "Dechiktorren92")
        
        tenant = TenantService.create_tenant("Test")
        list_accounts(args.db_url)