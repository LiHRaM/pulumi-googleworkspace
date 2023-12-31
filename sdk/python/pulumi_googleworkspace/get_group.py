# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = [
    'GetGroupResult',
    'AwaitableGetGroupResult',
    'get_group',
    'get_group_output',
]

@pulumi.output_type
class GetGroupResult:
    """
    A collection of values returned by getGroup.
    """
    def __init__(__self__, admin_created=None, aliases=None, description=None, direct_members_count=None, email=None, etag=None, id=None, name=None, non_editable_aliases=None):
        if admin_created and not isinstance(admin_created, bool):
            raise TypeError("Expected argument 'admin_created' to be a bool")
        pulumi.set(__self__, "admin_created", admin_created)
        if aliases and not isinstance(aliases, list):
            raise TypeError("Expected argument 'aliases' to be a list")
        pulumi.set(__self__, "aliases", aliases)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if direct_members_count and not isinstance(direct_members_count, int):
            raise TypeError("Expected argument 'direct_members_count' to be a int")
        pulumi.set(__self__, "direct_members_count", direct_members_count)
        if email and not isinstance(email, str):
            raise TypeError("Expected argument 'email' to be a str")
        pulumi.set(__self__, "email", email)
        if etag and not isinstance(etag, str):
            raise TypeError("Expected argument 'etag' to be a str")
        pulumi.set(__self__, "etag", etag)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if non_editable_aliases and not isinstance(non_editable_aliases, list):
            raise TypeError("Expected argument 'non_editable_aliases' to be a list")
        pulumi.set(__self__, "non_editable_aliases", non_editable_aliases)

    @property
    @pulumi.getter(name="adminCreated")
    def admin_created(self) -> bool:
        """
        Value is true if this group was created by an administrator rather than a user.
        """
        return pulumi.get(self, "admin_created")

    @property
    @pulumi.getter
    def aliases(self) -> Sequence[str]:
        """
        asps.list of group's email addresses.
        """
        return pulumi.get(self, "aliases")

    @property
    @pulumi.getter
    def description(self) -> str:
        """
        An extended description to help users determine the purpose of a group.For example, you can include information about who should join the group,the types of messages to send to the group, links to FAQs about the group, or related groups.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="directMembersCount")
    def direct_members_count(self) -> int:
        """
        The number of users that are direct members of the group.If a group is a member (child) of this group (the parent),members of the child group are not counted in the directMembersCount property of the parent group.
        """
        return pulumi.get(self, "direct_members_count")

    @property
    @pulumi.getter
    def email(self) -> str:
        """
        The group's email address. If your account has multiple domains,select the appropriate domain for the email address. The email must be unique.
        """
        return pulumi.get(self, "email")

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
        The unique ID of a group. A group id can be used as a group request URI's groupKey.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The group's display name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="nonEditableAliases")
    def non_editable_aliases(self) -> Sequence[str]:
        """
        asps.list of the group's non-editable alias email addresses that are outside of the account's primary domain or subdomains. These are functioning email addresses used by the group.
        """
        return pulumi.get(self, "non_editable_aliases")


class AwaitableGetGroupResult(GetGroupResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetGroupResult(
            admin_created=self.admin_created,
            aliases=self.aliases,
            description=self.description,
            direct_members_count=self.direct_members_count,
            email=self.email,
            etag=self.etag,
            id=self.id,
            name=self.name,
            non_editable_aliases=self.non_editable_aliases)


def get_group(email: Optional[str] = None,
              id: Optional[str] = None,
              opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetGroupResult:
    """
    ## Example Usage

    ```python
    import pulumi
    import pulumi_googleworkspace as googleworkspace

    sales = googleworkspace.get_group(email="sales@example.com")
    pulumi.export("groupName", sales.name)
    ```


    :param str email: The group's email address. If your account has multiple domains,select the appropriate domain for the email address. The email must be unique.
    :param str id: The unique ID of a group. A group id can be used as a group request URI's groupKey.
    """
    __args__ = dict()
    __args__['email'] = email
    __args__['id'] = id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('googleworkspace:index/getGroup:getGroup', __args__, opts=opts, typ=GetGroupResult).value

    return AwaitableGetGroupResult(
        admin_created=__ret__.admin_created,
        aliases=__ret__.aliases,
        description=__ret__.description,
        direct_members_count=__ret__.direct_members_count,
        email=__ret__.email,
        etag=__ret__.etag,
        id=__ret__.id,
        name=__ret__.name,
        non_editable_aliases=__ret__.non_editable_aliases)


@_utilities.lift_output_func(get_group)
def get_group_output(email: Optional[pulumi.Input[Optional[str]]] = None,
                     id: Optional[pulumi.Input[Optional[str]]] = None,
                     opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetGroupResult]:
    """
    ## Example Usage

    ```python
    import pulumi
    import pulumi_googleworkspace as googleworkspace

    sales = googleworkspace.get_group(email="sales@example.com")
    pulumi.export("groupName", sales.name)
    ```


    :param str email: The group's email address. If your account has multiple domains,select the appropriate domain for the email address. The email must be unique.
    :param str id: The unique ID of a group. A group id can be used as a group request URI's groupKey.
    """
    ...
