# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['GroupMemberArgs', 'GroupMember']

@pulumi.input_type
class GroupMemberArgs:
    def __init__(__self__, *,
                 email: pulumi.Input[str],
                 group_id: pulumi.Input[str],
                 delivery_settings: Optional[pulumi.Input[str]] = None,
                 role: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a GroupMember resource.
        :param pulumi.Input[str] email: The member's email address. A member can be a user or another group. This property is required when adding a member to a
               group. The email must be unique and cannot be an alias of another group. If the email address is changed, the API
               automatically reflects the email address changes.
        :param pulumi.Input[str] group_id: Identifies the group in the API request. The value can be the group's email address, group alias, or the unique group
               ID.
        :param pulumi.Input[str] delivery_settings: Defines mail delivery preferences of member. Acceptable values are: - `ALL_MAIL`: All messages, delivered as soon as
               they arrive. - `DAILY`: No more than one message a day. - `DIGEST`: Up to 25 messages bundled into a single message. -
               `DISABLED`: Remove subscription. - `NONE`: No messages.
        :param pulumi.Input[str] role: The member's role in a group. The API returns an error for cycles in group memberships. For example, if group1 is a
               member of group2, group2 cannot be a member of group1. Acceptable values are: - `MANAGER`: This role is only available
               if the Google Groups for Business is enabled using the Admin Console. A `MANAGER` role can do everything done by an
               `OWNER` role except make a member an `OWNER` or delete the group. A group can have multiple `MANAGER` members. -
               `MEMBER`: This role can subscribe to a group, view discussion archives, and view the group's membership list. - `OWNER`:
               This role can send messages to the group, add or remove members, change member roles, change group's settings, and
               delete the group. An OWNER must be a member of the group. A group can have more than one OWNER.
        :param pulumi.Input[str] type: The type of group member. Acceptable values are: - `CUSTOMER`: The member represents all users in a domain. An email
               address is not returned and the ID returned is the customer ID. - `GROUP`: The member is another group. - `USER`: The
               member is a user.
        """
        pulumi.set(__self__, "email", email)
        pulumi.set(__self__, "group_id", group_id)
        if delivery_settings is not None:
            pulumi.set(__self__, "delivery_settings", delivery_settings)
        if role is not None:
            pulumi.set(__self__, "role", role)
        if type is not None:
            pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def email(self) -> pulumi.Input[str]:
        """
        The member's email address. A member can be a user or another group. This property is required when adding a member to a
        group. The email must be unique and cannot be an alias of another group. If the email address is changed, the API
        automatically reflects the email address changes.
        """
        return pulumi.get(self, "email")

    @email.setter
    def email(self, value: pulumi.Input[str]):
        pulumi.set(self, "email", value)

    @property
    @pulumi.getter(name="groupId")
    def group_id(self) -> pulumi.Input[str]:
        """
        Identifies the group in the API request. The value can be the group's email address, group alias, or the unique group
        ID.
        """
        return pulumi.get(self, "group_id")

    @group_id.setter
    def group_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "group_id", value)

    @property
    @pulumi.getter(name="deliverySettings")
    def delivery_settings(self) -> Optional[pulumi.Input[str]]:
        """
        Defines mail delivery preferences of member. Acceptable values are: - `ALL_MAIL`: All messages, delivered as soon as
        they arrive. - `DAILY`: No more than one message a day. - `DIGEST`: Up to 25 messages bundled into a single message. -
        `DISABLED`: Remove subscription. - `NONE`: No messages.
        """
        return pulumi.get(self, "delivery_settings")

    @delivery_settings.setter
    def delivery_settings(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "delivery_settings", value)

    @property
    @pulumi.getter
    def role(self) -> Optional[pulumi.Input[str]]:
        """
        The member's role in a group. The API returns an error for cycles in group memberships. For example, if group1 is a
        member of group2, group2 cannot be a member of group1. Acceptable values are: - `MANAGER`: This role is only available
        if the Google Groups for Business is enabled using the Admin Console. A `MANAGER` role can do everything done by an
        `OWNER` role except make a member an `OWNER` or delete the group. A group can have multiple `MANAGER` members. -
        `MEMBER`: This role can subscribe to a group, view discussion archives, and view the group's membership list. - `OWNER`:
        This role can send messages to the group, add or remove members, change member roles, change group's settings, and
        delete the group. An OWNER must be a member of the group. A group can have more than one OWNER.
        """
        return pulumi.get(self, "role")

    @role.setter
    def role(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "role", value)

    @property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[str]]:
        """
        The type of group member. Acceptable values are: - `CUSTOMER`: The member represents all users in a domain. An email
        address is not returned and the ID returned is the customer ID. - `GROUP`: The member is another group. - `USER`: The
        member is a user.
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "type", value)


@pulumi.input_type
class _GroupMemberState:
    def __init__(__self__, *,
                 delivery_settings: Optional[pulumi.Input[str]] = None,
                 email: Optional[pulumi.Input[str]] = None,
                 etag: Optional[pulumi.Input[str]] = None,
                 group_id: Optional[pulumi.Input[str]] = None,
                 member_id: Optional[pulumi.Input[str]] = None,
                 role: Optional[pulumi.Input[str]] = None,
                 status: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering GroupMember resources.
        :param pulumi.Input[str] delivery_settings: Defines mail delivery preferences of member. Acceptable values are: - `ALL_MAIL`: All messages, delivered as soon as
               they arrive. - `DAILY`: No more than one message a day. - `DIGEST`: Up to 25 messages bundled into a single message. -
               `DISABLED`: Remove subscription. - `NONE`: No messages.
        :param pulumi.Input[str] email: The member's email address. A member can be a user or another group. This property is required when adding a member to a
               group. The email must be unique and cannot be an alias of another group. If the email address is changed, the API
               automatically reflects the email address changes.
        :param pulumi.Input[str] etag: ETag of the resource.
        :param pulumi.Input[str] group_id: Identifies the group in the API request. The value can be the group's email address, group alias, or the unique group
               ID.
        :param pulumi.Input[str] member_id: The unique ID of the group member. A member id can be used as a member request URI's memberKey.
        :param pulumi.Input[str] role: The member's role in a group. The API returns an error for cycles in group memberships. For example, if group1 is a
               member of group2, group2 cannot be a member of group1. Acceptable values are: - `MANAGER`: This role is only available
               if the Google Groups for Business is enabled using the Admin Console. A `MANAGER` role can do everything done by an
               `OWNER` role except make a member an `OWNER` or delete the group. A group can have multiple `MANAGER` members. -
               `MEMBER`: This role can subscribe to a group, view discussion archives, and view the group's membership list. - `OWNER`:
               This role can send messages to the group, add or remove members, change member roles, change group's settings, and
               delete the group. An OWNER must be a member of the group. A group can have more than one OWNER.
        :param pulumi.Input[str] status: Status of member.
        :param pulumi.Input[str] type: The type of group member. Acceptable values are: - `CUSTOMER`: The member represents all users in a domain. An email
               address is not returned and the ID returned is the customer ID. - `GROUP`: The member is another group. - `USER`: The
               member is a user.
        """
        if delivery_settings is not None:
            pulumi.set(__self__, "delivery_settings", delivery_settings)
        if email is not None:
            pulumi.set(__self__, "email", email)
        if etag is not None:
            pulumi.set(__self__, "etag", etag)
        if group_id is not None:
            pulumi.set(__self__, "group_id", group_id)
        if member_id is not None:
            pulumi.set(__self__, "member_id", member_id)
        if role is not None:
            pulumi.set(__self__, "role", role)
        if status is not None:
            pulumi.set(__self__, "status", status)
        if type is not None:
            pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="deliverySettings")
    def delivery_settings(self) -> Optional[pulumi.Input[str]]:
        """
        Defines mail delivery preferences of member. Acceptable values are: - `ALL_MAIL`: All messages, delivered as soon as
        they arrive. - `DAILY`: No more than one message a day. - `DIGEST`: Up to 25 messages bundled into a single message. -
        `DISABLED`: Remove subscription. - `NONE`: No messages.
        """
        return pulumi.get(self, "delivery_settings")

    @delivery_settings.setter
    def delivery_settings(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "delivery_settings", value)

    @property
    @pulumi.getter
    def email(self) -> Optional[pulumi.Input[str]]:
        """
        The member's email address. A member can be a user or another group. This property is required when adding a member to a
        group. The email must be unique and cannot be an alias of another group. If the email address is changed, the API
        automatically reflects the email address changes.
        """
        return pulumi.get(self, "email")

    @email.setter
    def email(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "email", value)

    @property
    @pulumi.getter
    def etag(self) -> Optional[pulumi.Input[str]]:
        """
        ETag of the resource.
        """
        return pulumi.get(self, "etag")

    @etag.setter
    def etag(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "etag", value)

    @property
    @pulumi.getter(name="groupId")
    def group_id(self) -> Optional[pulumi.Input[str]]:
        """
        Identifies the group in the API request. The value can be the group's email address, group alias, or the unique group
        ID.
        """
        return pulumi.get(self, "group_id")

    @group_id.setter
    def group_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "group_id", value)

    @property
    @pulumi.getter(name="memberId")
    def member_id(self) -> Optional[pulumi.Input[str]]:
        """
        The unique ID of the group member. A member id can be used as a member request URI's memberKey.
        """
        return pulumi.get(self, "member_id")

    @member_id.setter
    def member_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "member_id", value)

    @property
    @pulumi.getter
    def role(self) -> Optional[pulumi.Input[str]]:
        """
        The member's role in a group. The API returns an error for cycles in group memberships. For example, if group1 is a
        member of group2, group2 cannot be a member of group1. Acceptable values are: - `MANAGER`: This role is only available
        if the Google Groups for Business is enabled using the Admin Console. A `MANAGER` role can do everything done by an
        `OWNER` role except make a member an `OWNER` or delete the group. A group can have multiple `MANAGER` members. -
        `MEMBER`: This role can subscribe to a group, view discussion archives, and view the group's membership list. - `OWNER`:
        This role can send messages to the group, add or remove members, change member roles, change group's settings, and
        delete the group. An OWNER must be a member of the group. A group can have more than one OWNER.
        """
        return pulumi.get(self, "role")

    @role.setter
    def role(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "role", value)

    @property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[str]]:
        """
        Status of member.
        """
        return pulumi.get(self, "status")

    @status.setter
    def status(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "status", value)

    @property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[str]]:
        """
        The type of group member. Acceptable values are: - `CUSTOMER`: The member represents all users in a domain. An email
        address is not returned and the ID returned is the customer ID. - `GROUP`: The member is another group. - `USER`: The
        member is a user.
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "type", value)


class GroupMember(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 delivery_settings: Optional[pulumi.Input[str]] = None,
                 email: Optional[pulumi.Input[str]] = None,
                 group_id: Optional[pulumi.Input[str]] = None,
                 role: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Group Member resource manages Google Workspace Groups Members. Group Member resides under the `https://www.googleapis.com/auth/admin.directory.group` client scope.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_googleworkspace as googleworkspace

        sales = googleworkspace.Group("sales", email="sales@example.com")
        michael = googleworkspace.User("michael",
            primary_email="michael.scott@example.com",
            password="34819d7beeabb9260a5c854bc85b3e44",
            hash_function="MD5",
            name=googleworkspace.UserNameArgs(
                family_name="Scott",
                given_name="Michael",
            ))
        manager = googleworkspace.GroupMember("manager",
            group_id=sales.id,
            email=michael.primary_email,
            role="MANAGER")
        ```

        ## Import

        ```sh
         $ pulumi import googleworkspace:index/groupMember:GroupMember manager groups/01abcde23fg4h5i/members/123456789012345678901
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] delivery_settings: Defines mail delivery preferences of member. Acceptable values are: - `ALL_MAIL`: All messages, delivered as soon as
               they arrive. - `DAILY`: No more than one message a day. - `DIGEST`: Up to 25 messages bundled into a single message. -
               `DISABLED`: Remove subscription. - `NONE`: No messages.
        :param pulumi.Input[str] email: The member's email address. A member can be a user or another group. This property is required when adding a member to a
               group. The email must be unique and cannot be an alias of another group. If the email address is changed, the API
               automatically reflects the email address changes.
        :param pulumi.Input[str] group_id: Identifies the group in the API request. The value can be the group's email address, group alias, or the unique group
               ID.
        :param pulumi.Input[str] role: The member's role in a group. The API returns an error for cycles in group memberships. For example, if group1 is a
               member of group2, group2 cannot be a member of group1. Acceptable values are: - `MANAGER`: This role is only available
               if the Google Groups for Business is enabled using the Admin Console. A `MANAGER` role can do everything done by an
               `OWNER` role except make a member an `OWNER` or delete the group. A group can have multiple `MANAGER` members. -
               `MEMBER`: This role can subscribe to a group, view discussion archives, and view the group's membership list. - `OWNER`:
               This role can send messages to the group, add or remove members, change member roles, change group's settings, and
               delete the group. An OWNER must be a member of the group. A group can have more than one OWNER.
        :param pulumi.Input[str] type: The type of group member. Acceptable values are: - `CUSTOMER`: The member represents all users in a domain. An email
               address is not returned and the ID returned is the customer ID. - `GROUP`: The member is another group. - `USER`: The
               member is a user.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: GroupMemberArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Group Member resource manages Google Workspace Groups Members. Group Member resides under the `https://www.googleapis.com/auth/admin.directory.group` client scope.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_googleworkspace as googleworkspace

        sales = googleworkspace.Group("sales", email="sales@example.com")
        michael = googleworkspace.User("michael",
            primary_email="michael.scott@example.com",
            password="34819d7beeabb9260a5c854bc85b3e44",
            hash_function="MD5",
            name=googleworkspace.UserNameArgs(
                family_name="Scott",
                given_name="Michael",
            ))
        manager = googleworkspace.GroupMember("manager",
            group_id=sales.id,
            email=michael.primary_email,
            role="MANAGER")
        ```

        ## Import

        ```sh
         $ pulumi import googleworkspace:index/groupMember:GroupMember manager groups/01abcde23fg4h5i/members/123456789012345678901
        ```

        :param str resource_name: The name of the resource.
        :param GroupMemberArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(GroupMemberArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 delivery_settings: Optional[pulumi.Input[str]] = None,
                 email: Optional[pulumi.Input[str]] = None,
                 group_id: Optional[pulumi.Input[str]] = None,
                 role: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = GroupMemberArgs.__new__(GroupMemberArgs)

            __props__.__dict__["delivery_settings"] = delivery_settings
            if email is None and not opts.urn:
                raise TypeError("Missing required property 'email'")
            __props__.__dict__["email"] = email
            if group_id is None and not opts.urn:
                raise TypeError("Missing required property 'group_id'")
            __props__.__dict__["group_id"] = group_id
            __props__.__dict__["role"] = role
            __props__.__dict__["type"] = type
            __props__.__dict__["etag"] = None
            __props__.__dict__["member_id"] = None
            __props__.__dict__["status"] = None
        super(GroupMember, __self__).__init__(
            'googleworkspace:index/groupMember:GroupMember',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            delivery_settings: Optional[pulumi.Input[str]] = None,
            email: Optional[pulumi.Input[str]] = None,
            etag: Optional[pulumi.Input[str]] = None,
            group_id: Optional[pulumi.Input[str]] = None,
            member_id: Optional[pulumi.Input[str]] = None,
            role: Optional[pulumi.Input[str]] = None,
            status: Optional[pulumi.Input[str]] = None,
            type: Optional[pulumi.Input[str]] = None) -> 'GroupMember':
        """
        Get an existing GroupMember resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] delivery_settings: Defines mail delivery preferences of member. Acceptable values are: - `ALL_MAIL`: All messages, delivered as soon as
               they arrive. - `DAILY`: No more than one message a day. - `DIGEST`: Up to 25 messages bundled into a single message. -
               `DISABLED`: Remove subscription. - `NONE`: No messages.
        :param pulumi.Input[str] email: The member's email address. A member can be a user or another group. This property is required when adding a member to a
               group. The email must be unique and cannot be an alias of another group. If the email address is changed, the API
               automatically reflects the email address changes.
        :param pulumi.Input[str] etag: ETag of the resource.
        :param pulumi.Input[str] group_id: Identifies the group in the API request. The value can be the group's email address, group alias, or the unique group
               ID.
        :param pulumi.Input[str] member_id: The unique ID of the group member. A member id can be used as a member request URI's memberKey.
        :param pulumi.Input[str] role: The member's role in a group. The API returns an error for cycles in group memberships. For example, if group1 is a
               member of group2, group2 cannot be a member of group1. Acceptable values are: - `MANAGER`: This role is only available
               if the Google Groups for Business is enabled using the Admin Console. A `MANAGER` role can do everything done by an
               `OWNER` role except make a member an `OWNER` or delete the group. A group can have multiple `MANAGER` members. -
               `MEMBER`: This role can subscribe to a group, view discussion archives, and view the group's membership list. - `OWNER`:
               This role can send messages to the group, add or remove members, change member roles, change group's settings, and
               delete the group. An OWNER must be a member of the group. A group can have more than one OWNER.
        :param pulumi.Input[str] status: Status of member.
        :param pulumi.Input[str] type: The type of group member. Acceptable values are: - `CUSTOMER`: The member represents all users in a domain. An email
               address is not returned and the ID returned is the customer ID. - `GROUP`: The member is another group. - `USER`: The
               member is a user.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _GroupMemberState.__new__(_GroupMemberState)

        __props__.__dict__["delivery_settings"] = delivery_settings
        __props__.__dict__["email"] = email
        __props__.__dict__["etag"] = etag
        __props__.__dict__["group_id"] = group_id
        __props__.__dict__["member_id"] = member_id
        __props__.__dict__["role"] = role
        __props__.__dict__["status"] = status
        __props__.__dict__["type"] = type
        return GroupMember(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="deliverySettings")
    def delivery_settings(self) -> pulumi.Output[Optional[str]]:
        """
        Defines mail delivery preferences of member. Acceptable values are: - `ALL_MAIL`: All messages, delivered as soon as
        they arrive. - `DAILY`: No more than one message a day. - `DIGEST`: Up to 25 messages bundled into a single message. -
        `DISABLED`: Remove subscription. - `NONE`: No messages.
        """
        return pulumi.get(self, "delivery_settings")

    @property
    @pulumi.getter
    def email(self) -> pulumi.Output[str]:
        """
        The member's email address. A member can be a user or another group. This property is required when adding a member to a
        group. The email must be unique and cannot be an alias of another group. If the email address is changed, the API
        automatically reflects the email address changes.
        """
        return pulumi.get(self, "email")

    @property
    @pulumi.getter
    def etag(self) -> pulumi.Output[str]:
        """
        ETag of the resource.
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter(name="groupId")
    def group_id(self) -> pulumi.Output[str]:
        """
        Identifies the group in the API request. The value can be the group's email address, group alias, or the unique group
        ID.
        """
        return pulumi.get(self, "group_id")

    @property
    @pulumi.getter(name="memberId")
    def member_id(self) -> pulumi.Output[str]:
        """
        The unique ID of the group member. A member id can be used as a member request URI's memberKey.
        """
        return pulumi.get(self, "member_id")

    @property
    @pulumi.getter
    def role(self) -> pulumi.Output[Optional[str]]:
        """
        The member's role in a group. The API returns an error for cycles in group memberships. For example, if group1 is a
        member of group2, group2 cannot be a member of group1. Acceptable values are: - `MANAGER`: This role is only available
        if the Google Groups for Business is enabled using the Admin Console. A `MANAGER` role can do everything done by an
        `OWNER` role except make a member an `OWNER` or delete the group. A group can have multiple `MANAGER` members. -
        `MEMBER`: This role can subscribe to a group, view discussion archives, and view the group's membership list. - `OWNER`:
        This role can send messages to the group, add or remove members, change member roles, change group's settings, and
        delete the group. An OWNER must be a member of the group. A group can have more than one OWNER.
        """
        return pulumi.get(self, "role")

    @property
    @pulumi.getter
    def status(self) -> pulumi.Output[str]:
        """
        Status of member.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[Optional[str]]:
        """
        The type of group member. Acceptable values are: - `CUSTOMER`: The member represents all users in a domain. An email
        address is not returned and the ID returned is the customer ID. - `GROUP`: The member is another group. - `USER`: The
        member is a user.
        """
        return pulumi.get(self, "type")

