import argparse
from models.account import Account, Tenant, TenantAccountJoin, TenantAccountRole

import os
from dotenv import load_dotenv
load_dotenv()

parser = argparse.ArgumentParser(description="Add tenant to an existing account")

parser.add_argument("account_id", help="ID of the account")
parser.add_argument("--tenant_id", help="ID of the tenant (if exists)")
parser.add_argument("--tenant_name", help="Name of the new tenant (if creating)")
parser.add_argument("role", choices=[role.value for role in TenantAccountRole], help="Role of the account in the tenant")
parser.add_argument("--db_url", help="Database connection URL", default="postgresql://postgres:difyai123456@docker-db-1/dify")
parser.add_argument('--display', action='store_true', help='Include subfolders in processing')
parser.add_argument('--add-tenant', action='store_true', help='Include subfolders in processing')
parser.add_argument('--add-user', action='store_true', help='Include subfolders in processing')

args = parser.parse_args()

from app import app, db  # Import your Flask app
from models.account import Tenant
from services.account_service import TenantService, AccountService


def print_attributes(obj):
    """Prints the attributes and their values of any object."""
    for attribute in dir(obj):
        # Skip built-in attributes
        if not attribute.startswith('__'):
            value = getattr(obj, attribute)
            print(f"{attribute}: {value}")
            
with app.app_context():
    
    if args.display:
        # Start a new session
        session = db.session

        # Query for the tenant you are interested in
        tenants = session.query(Tenant).all()
        print("\nWorkspaces: \n")
        for tenant in tenants:
            print_attributes(tenant)
            print("\n")

        tenant = session.query(Tenant).first()
        
        session.commit()
        
    else:
        # Authenticate the main user
        try:
            account = AccountService.authenticate(email=os.getenv('USER_EMAIL'), password=os.getenv('USER_PASSWORD'))
        except Exception as e:
            print(f"Authentication failed: {e}")
            exit(1)
        
        if args.add_tenant:
            # Create a new tenant
            try:
                tenant_name = f"{account.name}'s Workspace"
                tenant = TenantService.create_tenant(name=tenant_name)
                print(f"Tenant '{tenant_name}' created successfully.")
            except Exception as e:
                print(f"Failed to create tenant: {e}")
                exit(1)
        
            # Add the authenticated user to the newly created tenant as an owner
            try:
                TenantService.create_tenant_member(tenant=tenant, account=account, role='owner')
                account.current_tenant = tenant
                db.session.commit()
                print(f"User '{account.email}' added to tenant '{tenant_name}' as an owner.")
            except Exception as e:
                print(f"Failed to add user to tenant: {e}")