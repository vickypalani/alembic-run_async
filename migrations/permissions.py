"""Will dynamically generate the permissions"""

from sqlalchemy import insert, delete
from main import Permission

CRUD_OPERATIONS = {
    "create": "To create",
    "read": "To view",
    "update": "To update",
    "delete": "To delete",
}


async def create_permissions(connnection, kw_args):
    """Create permissions based on the given table"""
    table = kw_args["table"]
    permissions = []
    for key in CRUD_OPERATIONS.keys():
        permission_detail = {
            "name": f"{table}.{key}",
            "display_name": f"{table.title()} {key.title()}",
            "description": f"{CRUD_OPERATIONS[key]} {table}",
        }
        permissions.append(permission_detail)
    return await connnection.execute(insert(Permission), permissions)


async def delete_permissions(connection, kw_args):
    """Delete permissions based on the given table"""
    table = kw_args["table"]
    return await connection.execute(
        delete(Permission).where(Permission.name.like(f"{table}.%"))
    )
