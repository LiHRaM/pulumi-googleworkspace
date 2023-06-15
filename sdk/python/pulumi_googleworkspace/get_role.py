# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities
from . import outputs

__all__ = [
    'GetRoleResult',
    'AwaitableGetRoleResult',
    'get_role',
    'get_role_output',
]

@pulumi.output_type
class GetRoleResult:
    """
    A collection of values returned by getRole.
    """
    def __init__(__self__, description=None, etag=None, id=None, is_super_admin_role=None, is_system_role=None, name=None, privileges=None):
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if etag and not isinstance(etag, str):
            raise TypeError("Expected argument 'etag' to be a str")
        pulumi.set(__self__, "etag", etag)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if is_super_admin_role and not isinstance(is_super_admin_role, bool):
            raise TypeError("Expected argument 'is_super_admin_role' to be a bool")
        pulumi.set(__self__, "is_super_admin_role", is_super_admin_role)
        if is_system_role and not isinstance(is_system_role, bool):
            raise TypeError("Expected argument 'is_system_role' to be a bool")
        pulumi.set(__self__, "is_system_role", is_system_role)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if privileges and not isinstance(privileges, list):
            raise TypeError("Expected argument 'privileges' to be a list")
        pulumi.set(__self__, "privileges", privileges)

    @property
    @pulumi.getter
    def description(self) -> str:
        """
        A short description of the role.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def etag(self) -> str:
        """
        ETag of the resource.
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        ID of the role.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="isSuperAdminRole")
    def is_super_admin_role(self) -> bool:
        """
        Returns true if the role is a super admin role.
        """
        return pulumi.get(self, "is_super_admin_role")

    @property
    @pulumi.getter(name="isSystemRole")
    def is_system_role(self) -> bool:
        """
        Returns true if this is a pre-defined system role.
        """
        return pulumi.get(self, "is_system_role")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Name of the role.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def privileges(self) -> Sequence['outputs.GetRolePrivilegeResult']:
        """
        The set of privileges that are granted to this role.
        """
        return pulumi.get(self, "privileges")


class AwaitableGetRoleResult(GetRoleResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetRoleResult(
            description=self.description,
            etag=self.etag,
            id=self.id,
            is_super_admin_role=self.is_super_admin_role,
            is_system_role=self.is_system_role,
            name=self.name,
            privileges=self.privileges)


def get_role(name: Optional[str] = None,
             opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetRoleResult:
    """
    ## Example Usage

    ```python
    import pulumi
    import pulumi_googleworkspace as googleworkspace

    group_admin = googleworkspace.get_role(name="_GROUPS_ADMIN_ROLE")
    pulumi.export("isSystemRole", group_admin.is_system_role)
    ```


    :param str name: Name of the role.
    """
    __args__ = dict()
    __args__['name'] = name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('googleworkspace:index/getRole:getRole', __args__, opts=opts, typ=GetRoleResult).value

    return AwaitableGetRoleResult(
        description=__ret__.description,
        etag=__ret__.etag,
        id=__ret__.id,
        is_super_admin_role=__ret__.is_super_admin_role,
        is_system_role=__ret__.is_system_role,
        name=__ret__.name,
        privileges=__ret__.privileges)


@_utilities.lift_output_func(get_role)
def get_role_output(name: Optional[pulumi.Input[str]] = None,
                    opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetRoleResult]:
    """
    ## Example Usage

    ```python
    import pulumi
    import pulumi_googleworkspace as googleworkspace

    group_admin = googleworkspace.get_role(name="_GROUPS_ADMIN_ROLE")
    pulumi.export("isSystemRole", group_admin.is_system_role)
    ```


    :param str name: Name of the role.
    """
    ...
