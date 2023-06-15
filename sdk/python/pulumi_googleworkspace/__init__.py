# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from . import _utilities
import typing
# Export this package's modules as members:
from .chrome_policy import *
from .domain import *
from .domain_alias import *
from .get_chrome_policy_schema import *
from .get_domain import *
from .get_domain_alias import *
from .get_group import *
from .get_group_member import *
from .get_group_members import *
from .get_group_settings import *
from .get_groups import *
from .get_org_unit import *
from .get_privileges import *
from .get_role import *
from .get_schema import *
from .get_user import *
from .get_users import *
from .gmail_send_as_alias import *
from .group import *
from .group_member import *
from .group_members import *
from .group_settings import *
from .org_unit import *
from .provider import *
from .role import *
from .role_assignment import *
from .schema import *
from .user import *
from ._inputs import *
from . import outputs

# Make subpackages available:
if typing.TYPE_CHECKING:
    import pulumi_googleworkspace.config as __config
    config = __config
else:
    config = _utilities.lazy_import('pulumi_googleworkspace.config')

_utilities.register(
    resource_modules="""
[
 {
  "pkg": "googleworkspace",
  "mod": "index/chromePolicy",
  "fqn": "pulumi_googleworkspace",
  "classes": {
   "googleworkspace:index/chromePolicy:ChromePolicy": "ChromePolicy"
  }
 },
 {
  "pkg": "googleworkspace",
  "mod": "index/domain",
  "fqn": "pulumi_googleworkspace",
  "classes": {
   "googleworkspace:index/domain:Domain": "Domain"
  }
 },
 {
  "pkg": "googleworkspace",
  "mod": "index/domainAlias",
  "fqn": "pulumi_googleworkspace",
  "classes": {
   "googleworkspace:index/domainAlias:DomainAlias": "DomainAlias"
  }
 },
 {
  "pkg": "googleworkspace",
  "mod": "index/gmailSendAsAlias",
  "fqn": "pulumi_googleworkspace",
  "classes": {
   "googleworkspace:index/gmailSendAsAlias:GmailSendAsAlias": "GmailSendAsAlias"
  }
 },
 {
  "pkg": "googleworkspace",
  "mod": "index/group",
  "fqn": "pulumi_googleworkspace",
  "classes": {
   "googleworkspace:index/group:Group": "Group"
  }
 },
 {
  "pkg": "googleworkspace",
  "mod": "index/groupMember",
  "fqn": "pulumi_googleworkspace",
  "classes": {
   "googleworkspace:index/groupMember:GroupMember": "GroupMember"
  }
 },
 {
  "pkg": "googleworkspace",
  "mod": "index/groupMembers",
  "fqn": "pulumi_googleworkspace",
  "classes": {
   "googleworkspace:index/groupMembers:GroupMembers": "GroupMembers"
  }
 },
 {
  "pkg": "googleworkspace",
  "mod": "index/groupSettings",
  "fqn": "pulumi_googleworkspace",
  "classes": {
   "googleworkspace:index/groupSettings:GroupSettings": "GroupSettings"
  }
 },
 {
  "pkg": "googleworkspace",
  "mod": "index/orgUnit",
  "fqn": "pulumi_googleworkspace",
  "classes": {
   "googleworkspace:index/orgUnit:OrgUnit": "OrgUnit"
  }
 },
 {
  "pkg": "googleworkspace",
  "mod": "index/role",
  "fqn": "pulumi_googleworkspace",
  "classes": {
   "googleworkspace:index/role:Role": "Role"
  }
 },
 {
  "pkg": "googleworkspace",
  "mod": "index/roleAssignment",
  "fqn": "pulumi_googleworkspace",
  "classes": {
   "googleworkspace:index/roleAssignment:RoleAssignment": "RoleAssignment"
  }
 },
 {
  "pkg": "googleworkspace",
  "mod": "index/schema",
  "fqn": "pulumi_googleworkspace",
  "classes": {
   "googleworkspace:index/schema:Schema": "Schema"
  }
 },
 {
  "pkg": "googleworkspace",
  "mod": "index/user",
  "fqn": "pulumi_googleworkspace",
  "classes": {
   "googleworkspace:index/user:User": "User"
  }
 }
]
""",
    resource_packages="""
[
 {
  "pkg": "googleworkspace",
  "token": "pulumi:providers:googleworkspace",
  "fqn": "pulumi_googleworkspace",
  "class": "Provider"
 }
]
"""
)
