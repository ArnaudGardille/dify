import argparse
import os
from dotenv import load_dotenv

from app import app, db  # Import your Flask app
from models.account import Account, Tenant, TenantAccountJoin, TenantAccountRole
from services.account_service import TenantService, AccountService, RegisterService

load_dotenv()

parser = argparse.ArgumentParser(description="Database management script")

# Account-related arguments
parser.add_argument("--create-account", action="store_true", help="Create a new account")
parser.add_argument("--update-account", action="store_true", help="Update an existing account")
parser.add_argument("--close-account", action="store_true", help="Close an existing account")
parser.add_argument("--email", help="Email of the account")
parser.add_argument("--name", help="Name of the account")
parser.add_argument("--password", help="Password of the account")
parser.add_argument("--new-password", help="New password for the account")
parser.add_argument("--interface-language", help="Interface language of the account", default="en")
parser.add_argument("--interface-theme", help="Interface theme of the account", default="light")

# Tenant-related arguments
parser.add_argument("--create-tenant", action="store_true", help="Create a new tenant")
parser.add_argument("--add-tenant-member", action="store_true", help="Add a member to a tenant")
parser.add_argument("--remove-tenant-member", action="store_true", help="Remove a member from a tenant")
parser.add_argument("--update-tenant-member-role", action="store_true", help="Update a tenant member's role")
parser.add_argument("--tenant-id", help="ID of the tenant")
parser.add_argument("--tenant-name", help="Name of the tenant")
parser.add_argument("--role", choices=[role.value for role in TenantAccountRole], help="Role of the account in the tenant", default="owner")

# Operator-related arguments
parser.add_argument("--operator-email", help="Email of the operator account")
parser.add_argument("--operator-password", help="Password of the operator account")

# Display arguments
parser.add_argument('--display', action='store_true', help='Display tenants and their details')

args = parser.parse_args()

def print_attributes(obj):
    """Prints the attributes and their values of any object."""
    for attribute in dir(obj):
        if not attribute.startswith('__'):
            value = getattr(obj, attribute)
            print(f"{attribute}: {value}")

with app.app_context():
    if args.display:
        session = db.session
        tenants = session.query(Tenant).all()
        print("\nWorkspaces: \n")
        for tenant in tenants:
            print_attributes(tenant)
            print("\n")
        session.commit()

    elif args.create_account:
        try:
            account = AccountService.create_account(
                email=args.email,
                name=args.name,
                interface_language=args.interface_language,
                password=args.password,
                interface_theme=args.interface_theme
            )
            print(f"Account '{args.email}' created successfully.")
        except Exception as e:
            print(f"Failed to create account: {e}")

    elif args.update_account:
        try:
            account = Account.query.filter_by(email=args.email).first()
            if not account:
                raise Exception("Account not found.")
            
            update_data = {}
            if args.name:
                update_data['name'] = args.name
            if args.new_password:
                update_data['password'] = args.new_password
            if args.interface_language:
                update_data['interface_language'] = args.interface_language
            if args.interface_theme:
                update_data['interface_theme'] = args.interface_theme
            
            AccountService.update_account(account, **update_data)
            print(f"Account '{args.email}' updated successfully.")
        except Exception as e:
            print(f"Failed to update account: {e}")

    elif args.close_account:
        try:
            account = Account.query.filter_by(email=args.email).first()
            if not account:
                raise Exception("Account not found.")
            
            AccountService.close_account(account)
            print(f"Account '{args.email}' closed successfully.")
        except Exception as e:
            print(f"Failed to close account: {e}")

    elif args.create_tenant:
        try:
            tenant_name = args.tenant_name or f"{args.email}'s Workspace"
            tenant = TenantService.create_tenant(name=tenant_name)
            print(f"Tenant '{tenant_name}' created successfully.")
        except Exception as e:
            print(f"Failed to create tenant: {e}")

    elif args.add_tenant_member:
        try:
            tenant = Tenant.query.filter_by(id=args.tenant_id).first()
            if not tenant:
                raise Exception("Tenant not found.")

            account = Account.query.filter_by(email=args.email).first()
            if not account:
                raise Exception("Account not found.")

            TenantService.create_tenant_member(tenant=tenant, account=account, role=args.role)
            print(f"Account '{args.email}' added to tenant '{tenant.name}' as '{args.role}'.")
        except Exception as e:
            print(f"Failed to add tenant member: {e}")

    elif args.remove_tenant_member:
        try:
            tenant = Tenant.query.filter_by(id=args.tenant_id).first()
            if not tenant:
                raise Exception("Tenant not found.")

            account = Account.query.filter_by(email=args.email).first()
            if not account:
                raise Exception("Account not found.")

            operator_email = os.getenv('USER_EMAIL')
            operator_password = os.getenv('USER_PASSWORD')
            operator = AccountService.authenticate(email=operator_email, password=operator_password)

            TenantService.remove_member_from_tenant(tenant=tenant, account=account, operator=operator)
            print(f"Account '{args.email}' removed from tenant '{tenant.name}'.")
        except Exception as e:
            print(f"Failed to remove tenant member: {e}")

    elif args.update_tenant_member_role:
        try:
            tenant = Tenant.query.filter_by(id=args.tenant_id).first()
            if not tenant:
                raise Exception("Tenant not found.")

            account = Account.query.filter_by(email=args.email).first()
            if not account:
                raise Exception("Account not found.")

            operator_email = os.getenv('USER_EMAIL')
            operator_password = os.getenv('USER_PASSWORD')
            operator = AccountService.authenticate(email=operator_email, password=operator_password)

            TenantService.update_member_role(tenant=tenant, member=account, new_role=args.role, operator=operator)
            print(f"Updated role of account '{args.email}' in tenant '{tenant.name}' to '{args.role}'.")
        except Exception as e:
            print(f"Failed to update tenant member role: {e}")