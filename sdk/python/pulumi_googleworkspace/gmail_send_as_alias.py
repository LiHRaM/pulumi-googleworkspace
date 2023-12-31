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
from ._inputs import *

__all__ = ['GmailSendAsAliasArgs', 'GmailSendAsAlias']

@pulumi.input_type
class GmailSendAsAliasArgs:
    def __init__(__self__, *,
                 primary_email: pulumi.Input[str],
                 send_as_email: pulumi.Input[str],
                 display_name: Optional[pulumi.Input[str]] = None,
                 is_default: Optional[pulumi.Input[bool]] = None,
                 reply_to_address: Optional[pulumi.Input[str]] = None,
                 signature: Optional[pulumi.Input[str]] = None,
                 smtp_msa: Optional[pulumi.Input['GmailSendAsAliasSmtpMsaArgs']] = None,
                 treat_as_alias: Optional[pulumi.Input[bool]] = None):
        """
        The set of arguments for constructing a GmailSendAsAlias resource.
        :param pulumi.Input[str] primary_email: User's primary email address.
        :param pulumi.Input[str] send_as_email: The email address that appears in the 'From:' header for mail sent using this alias.
        :param pulumi.Input[str] display_name: A name that appears in the 'From:' header for mail sent using this alias. For custom 'from' addresses, when this is empty, Gmail will populate the 'From:' header with the name that is used for the primary address associated with the account. If the admin has disabled the ability for users to update their name format, requests to update this field for the primary login will silently fail.
        :param pulumi.Input[bool] is_default: Whether this address is selected as the default 'From:' address in situations such as composing a new message or sending
               a vacation auto-reply. Every Gmail account has exactly one default send-as address, so the only legal value that clients
               may write to this field is true. Changing this from false to true for an address will result in this field becoming
               false for the other previous default address. Toggling an existing alias' default to false is not possible, another
               alias must be added/imported and toggled to true to remove the default from an existing alias. To avoid drift with
               Terraform, please change the previous default's config to false AFTER a new default is applied and perform a refresh to
               synchronize with remote state.
        :param pulumi.Input[str] reply_to_address: An optional email address that is included in a 'Reply-To:' header for mail sent using this alias. If this is empty, Gmail will not generate a 'Reply-To:' header.
        :param pulumi.Input[str] signature: An optional HTML signature that is included in messages composed with this alias in the Gmail web UI. This signature is added to new emails only.
        :param pulumi.Input['GmailSendAsAliasSmtpMsaArgs'] smtp_msa: An optional SMTP service that will be used as an outbound relay for mail sent using this alias. If this is empty, outbound mail will be sent directly from Gmail's servers to the destination SMTP service. This setting only applies to custom 'from' aliases.
        :param pulumi.Input[bool] treat_as_alias: Defaults to `true`. Whether Gmail should treat this address as an alias for the user's primary email address. This setting only applies to custom 'from' aliases. See https://support.google.com/a/answer/1710338 for help on making this decision
        """
        pulumi.set(__self__, "primary_email", primary_email)
        pulumi.set(__self__, "send_as_email", send_as_email)
        if display_name is not None:
            pulumi.set(__self__, "display_name", display_name)
        if is_default is not None:
            pulumi.set(__self__, "is_default", is_default)
        if reply_to_address is not None:
            pulumi.set(__self__, "reply_to_address", reply_to_address)
        if signature is not None:
            pulumi.set(__self__, "signature", signature)
        if smtp_msa is not None:
            pulumi.set(__self__, "smtp_msa", smtp_msa)
        if treat_as_alias is not None:
            pulumi.set(__self__, "treat_as_alias", treat_as_alias)

    @property
    @pulumi.getter(name="primaryEmail")
    def primary_email(self) -> pulumi.Input[str]:
        """
        User's primary email address.
        """
        return pulumi.get(self, "primary_email")

    @primary_email.setter
    def primary_email(self, value: pulumi.Input[str]):
        pulumi.set(self, "primary_email", value)

    @property
    @pulumi.getter(name="sendAsEmail")
    def send_as_email(self) -> pulumi.Input[str]:
        """
        The email address that appears in the 'From:' header for mail sent using this alias.
        """
        return pulumi.get(self, "send_as_email")

    @send_as_email.setter
    def send_as_email(self, value: pulumi.Input[str]):
        pulumi.set(self, "send_as_email", value)

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[str]]:
        """
        A name that appears in the 'From:' header for mail sent using this alias. For custom 'from' addresses, when this is empty, Gmail will populate the 'From:' header with the name that is used for the primary address associated with the account. If the admin has disabled the ability for users to update their name format, requests to update this field for the primary login will silently fail.
        """
        return pulumi.get(self, "display_name")

    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "display_name", value)

    @property
    @pulumi.getter(name="isDefault")
    def is_default(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether this address is selected as the default 'From:' address in situations such as composing a new message or sending
        a vacation auto-reply. Every Gmail account has exactly one default send-as address, so the only legal value that clients
        may write to this field is true. Changing this from false to true for an address will result in this field becoming
        false for the other previous default address. Toggling an existing alias' default to false is not possible, another
        alias must be added/imported and toggled to true to remove the default from an existing alias. To avoid drift with
        Terraform, please change the previous default's config to false AFTER a new default is applied and perform a refresh to
        synchronize with remote state.
        """
        return pulumi.get(self, "is_default")

    @is_default.setter
    def is_default(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "is_default", value)

    @property
    @pulumi.getter(name="replyToAddress")
    def reply_to_address(self) -> Optional[pulumi.Input[str]]:
        """
        An optional email address that is included in a 'Reply-To:' header for mail sent using this alias. If this is empty, Gmail will not generate a 'Reply-To:' header.
        """
        return pulumi.get(self, "reply_to_address")

    @reply_to_address.setter
    def reply_to_address(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "reply_to_address", value)

    @property
    @pulumi.getter
    def signature(self) -> Optional[pulumi.Input[str]]:
        """
        An optional HTML signature that is included in messages composed with this alias in the Gmail web UI. This signature is added to new emails only.
        """
        return pulumi.get(self, "signature")

    @signature.setter
    def signature(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "signature", value)

    @property
    @pulumi.getter(name="smtpMsa")
    def smtp_msa(self) -> Optional[pulumi.Input['GmailSendAsAliasSmtpMsaArgs']]:
        """
        An optional SMTP service that will be used as an outbound relay for mail sent using this alias. If this is empty, outbound mail will be sent directly from Gmail's servers to the destination SMTP service. This setting only applies to custom 'from' aliases.
        """
        return pulumi.get(self, "smtp_msa")

    @smtp_msa.setter
    def smtp_msa(self, value: Optional[pulumi.Input['GmailSendAsAliasSmtpMsaArgs']]):
        pulumi.set(self, "smtp_msa", value)

    @property
    @pulumi.getter(name="treatAsAlias")
    def treat_as_alias(self) -> Optional[pulumi.Input[bool]]:
        """
        Defaults to `true`. Whether Gmail should treat this address as an alias for the user's primary email address. This setting only applies to custom 'from' aliases. See https://support.google.com/a/answer/1710338 for help on making this decision
        """
        return pulumi.get(self, "treat_as_alias")

    @treat_as_alias.setter
    def treat_as_alias(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "treat_as_alias", value)


@pulumi.input_type
class _GmailSendAsAliasState:
    def __init__(__self__, *,
                 display_name: Optional[pulumi.Input[str]] = None,
                 is_default: Optional[pulumi.Input[bool]] = None,
                 is_primary: Optional[pulumi.Input[bool]] = None,
                 primary_email: Optional[pulumi.Input[str]] = None,
                 reply_to_address: Optional[pulumi.Input[str]] = None,
                 send_as_email: Optional[pulumi.Input[str]] = None,
                 signature: Optional[pulumi.Input[str]] = None,
                 smtp_msa: Optional[pulumi.Input['GmailSendAsAliasSmtpMsaArgs']] = None,
                 treat_as_alias: Optional[pulumi.Input[bool]] = None,
                 verification_status: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering GmailSendAsAlias resources.
        :param pulumi.Input[str] display_name: A name that appears in the 'From:' header for mail sent using this alias. For custom 'from' addresses, when this is empty, Gmail will populate the 'From:' header with the name that is used for the primary address associated with the account. If the admin has disabled the ability for users to update their name format, requests to update this field for the primary login will silently fail.
        :param pulumi.Input[bool] is_default: Whether this address is selected as the default 'From:' address in situations such as composing a new message or sending
               a vacation auto-reply. Every Gmail account has exactly one default send-as address, so the only legal value that clients
               may write to this field is true. Changing this from false to true for an address will result in this field becoming
               false for the other previous default address. Toggling an existing alias' default to false is not possible, another
               alias must be added/imported and toggled to true to remove the default from an existing alias. To avoid drift with
               Terraform, please change the previous default's config to false AFTER a new default is applied and perform a refresh to
               synchronize with remote state.
        :param pulumi.Input[bool] is_primary: Whether this address is the primary address used to login to the account. Every Gmail account has exactly one primary address, and it cannot be deleted from the collection of send-as aliases.
        :param pulumi.Input[str] primary_email: User's primary email address.
        :param pulumi.Input[str] reply_to_address: An optional email address that is included in a 'Reply-To:' header for mail sent using this alias. If this is empty, Gmail will not generate a 'Reply-To:' header.
        :param pulumi.Input[str] send_as_email: The email address that appears in the 'From:' header for mail sent using this alias.
        :param pulumi.Input[str] signature: An optional HTML signature that is included in messages composed with this alias in the Gmail web UI. This signature is added to new emails only.
        :param pulumi.Input['GmailSendAsAliasSmtpMsaArgs'] smtp_msa: An optional SMTP service that will be used as an outbound relay for mail sent using this alias. If this is empty, outbound mail will be sent directly from Gmail's servers to the destination SMTP service. This setting only applies to custom 'from' aliases.
        :param pulumi.Input[bool] treat_as_alias: Defaults to `true`. Whether Gmail should treat this address as an alias for the user's primary email address. This setting only applies to custom 'from' aliases. See https://support.google.com/a/answer/1710338 for help on making this decision
        :param pulumi.Input[str] verification_status: Indicates whether this address has been verified for use as a send-as alias.
        """
        if display_name is not None:
            pulumi.set(__self__, "display_name", display_name)
        if is_default is not None:
            pulumi.set(__self__, "is_default", is_default)
        if is_primary is not None:
            pulumi.set(__self__, "is_primary", is_primary)
        if primary_email is not None:
            pulumi.set(__self__, "primary_email", primary_email)
        if reply_to_address is not None:
            pulumi.set(__self__, "reply_to_address", reply_to_address)
        if send_as_email is not None:
            pulumi.set(__self__, "send_as_email", send_as_email)
        if signature is not None:
            pulumi.set(__self__, "signature", signature)
        if smtp_msa is not None:
            pulumi.set(__self__, "smtp_msa", smtp_msa)
        if treat_as_alias is not None:
            pulumi.set(__self__, "treat_as_alias", treat_as_alias)
        if verification_status is not None:
            pulumi.set(__self__, "verification_status", verification_status)

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[str]]:
        """
        A name that appears in the 'From:' header for mail sent using this alias. For custom 'from' addresses, when this is empty, Gmail will populate the 'From:' header with the name that is used for the primary address associated with the account. If the admin has disabled the ability for users to update their name format, requests to update this field for the primary login will silently fail.
        """
        return pulumi.get(self, "display_name")

    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "display_name", value)

    @property
    @pulumi.getter(name="isDefault")
    def is_default(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether this address is selected as the default 'From:' address in situations such as composing a new message or sending
        a vacation auto-reply. Every Gmail account has exactly one default send-as address, so the only legal value that clients
        may write to this field is true. Changing this from false to true for an address will result in this field becoming
        false for the other previous default address. Toggling an existing alias' default to false is not possible, another
        alias must be added/imported and toggled to true to remove the default from an existing alias. To avoid drift with
        Terraform, please change the previous default's config to false AFTER a new default is applied and perform a refresh to
        synchronize with remote state.
        """
        return pulumi.get(self, "is_default")

    @is_default.setter
    def is_default(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "is_default", value)

    @property
    @pulumi.getter(name="isPrimary")
    def is_primary(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether this address is the primary address used to login to the account. Every Gmail account has exactly one primary address, and it cannot be deleted from the collection of send-as aliases.
        """
        return pulumi.get(self, "is_primary")

    @is_primary.setter
    def is_primary(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "is_primary", value)

    @property
    @pulumi.getter(name="primaryEmail")
    def primary_email(self) -> Optional[pulumi.Input[str]]:
        """
        User's primary email address.
        """
        return pulumi.get(self, "primary_email")

    @primary_email.setter
    def primary_email(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "primary_email", value)

    @property
    @pulumi.getter(name="replyToAddress")
    def reply_to_address(self) -> Optional[pulumi.Input[str]]:
        """
        An optional email address that is included in a 'Reply-To:' header for mail sent using this alias. If this is empty, Gmail will not generate a 'Reply-To:' header.
        """
        return pulumi.get(self, "reply_to_address")

    @reply_to_address.setter
    def reply_to_address(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "reply_to_address", value)

    @property
    @pulumi.getter(name="sendAsEmail")
    def send_as_email(self) -> Optional[pulumi.Input[str]]:
        """
        The email address that appears in the 'From:' header for mail sent using this alias.
        """
        return pulumi.get(self, "send_as_email")

    @send_as_email.setter
    def send_as_email(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "send_as_email", value)

    @property
    @pulumi.getter
    def signature(self) -> Optional[pulumi.Input[str]]:
        """
        An optional HTML signature that is included in messages composed with this alias in the Gmail web UI. This signature is added to new emails only.
        """
        return pulumi.get(self, "signature")

    @signature.setter
    def signature(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "signature", value)

    @property
    @pulumi.getter(name="smtpMsa")
    def smtp_msa(self) -> Optional[pulumi.Input['GmailSendAsAliasSmtpMsaArgs']]:
        """
        An optional SMTP service that will be used as an outbound relay for mail sent using this alias. If this is empty, outbound mail will be sent directly from Gmail's servers to the destination SMTP service. This setting only applies to custom 'from' aliases.
        """
        return pulumi.get(self, "smtp_msa")

    @smtp_msa.setter
    def smtp_msa(self, value: Optional[pulumi.Input['GmailSendAsAliasSmtpMsaArgs']]):
        pulumi.set(self, "smtp_msa", value)

    @property
    @pulumi.getter(name="treatAsAlias")
    def treat_as_alias(self) -> Optional[pulumi.Input[bool]]:
        """
        Defaults to `true`. Whether Gmail should treat this address as an alias for the user's primary email address. This setting only applies to custom 'from' aliases. See https://support.google.com/a/answer/1710338 for help on making this decision
        """
        return pulumi.get(self, "treat_as_alias")

    @treat_as_alias.setter
    def treat_as_alias(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "treat_as_alias", value)

    @property
    @pulumi.getter(name="verificationStatus")
    def verification_status(self) -> Optional[pulumi.Input[str]]:
        """
        Indicates whether this address has been verified for use as a send-as alias.
        """
        return pulumi.get(self, "verification_status")

    @verification_status.setter
    def verification_status(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "verification_status", value)


class GmailSendAsAlias(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 is_default: Optional[pulumi.Input[bool]] = None,
                 primary_email: Optional[pulumi.Input[str]] = None,
                 reply_to_address: Optional[pulumi.Input[str]] = None,
                 send_as_email: Optional[pulumi.Input[str]] = None,
                 signature: Optional[pulumi.Input[str]] = None,
                 smtp_msa: Optional[pulumi.Input[pulumi.InputType['GmailSendAsAliasSmtpMsaArgs']]] = None,
                 treat_as_alias: Optional[pulumi.Input[bool]] = None,
                 __props__=None):
        """
        ## Example Usage

        ```python
        import pulumi
        import pulumi_googleworkspace as googleworkspace

        example = googleworkspace.get_user(primary_email="user.with.gmail.license@example.com")
        alias = googleworkspace.User("alias",
            primary_email="alias@example.com",
            password="34819d7beeabb9260a5c854bc85b3e44",
            hash_function="MD5",
            name=googleworkspace.UserNameArgs(
                family_name="Scott",
                given_name="Michael",
            ))
        test = googleworkspace.GmailSendAsAlias("test",
            primary_email=example.primary_email,
            send_as_email=alias.primary_email)
        ```

        ## Import

        ```sh
         $ pulumi import googleworkspace:index/gmailSendAsAlias:GmailSendAsAlias alias user@example.com:alias@anotherexample.com
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] display_name: A name that appears in the 'From:' header for mail sent using this alias. For custom 'from' addresses, when this is empty, Gmail will populate the 'From:' header with the name that is used for the primary address associated with the account. If the admin has disabled the ability for users to update their name format, requests to update this field for the primary login will silently fail.
        :param pulumi.Input[bool] is_default: Whether this address is selected as the default 'From:' address in situations such as composing a new message or sending
               a vacation auto-reply. Every Gmail account has exactly one default send-as address, so the only legal value that clients
               may write to this field is true. Changing this from false to true for an address will result in this field becoming
               false for the other previous default address. Toggling an existing alias' default to false is not possible, another
               alias must be added/imported and toggled to true to remove the default from an existing alias. To avoid drift with
               Terraform, please change the previous default's config to false AFTER a new default is applied and perform a refresh to
               synchronize with remote state.
        :param pulumi.Input[str] primary_email: User's primary email address.
        :param pulumi.Input[str] reply_to_address: An optional email address that is included in a 'Reply-To:' header for mail sent using this alias. If this is empty, Gmail will not generate a 'Reply-To:' header.
        :param pulumi.Input[str] send_as_email: The email address that appears in the 'From:' header for mail sent using this alias.
        :param pulumi.Input[str] signature: An optional HTML signature that is included in messages composed with this alias in the Gmail web UI. This signature is added to new emails only.
        :param pulumi.Input[pulumi.InputType['GmailSendAsAliasSmtpMsaArgs']] smtp_msa: An optional SMTP service that will be used as an outbound relay for mail sent using this alias. If this is empty, outbound mail will be sent directly from Gmail's servers to the destination SMTP service. This setting only applies to custom 'from' aliases.
        :param pulumi.Input[bool] treat_as_alias: Defaults to `true`. Whether Gmail should treat this address as an alias for the user's primary email address. This setting only applies to custom 'from' aliases. See https://support.google.com/a/answer/1710338 for help on making this decision
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: GmailSendAsAliasArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        ## Example Usage

        ```python
        import pulumi
        import pulumi_googleworkspace as googleworkspace

        example = googleworkspace.get_user(primary_email="user.with.gmail.license@example.com")
        alias = googleworkspace.User("alias",
            primary_email="alias@example.com",
            password="34819d7beeabb9260a5c854bc85b3e44",
            hash_function="MD5",
            name=googleworkspace.UserNameArgs(
                family_name="Scott",
                given_name="Michael",
            ))
        test = googleworkspace.GmailSendAsAlias("test",
            primary_email=example.primary_email,
            send_as_email=alias.primary_email)
        ```

        ## Import

        ```sh
         $ pulumi import googleworkspace:index/gmailSendAsAlias:GmailSendAsAlias alias user@example.com:alias@anotherexample.com
        ```

        :param str resource_name: The name of the resource.
        :param GmailSendAsAliasArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(GmailSendAsAliasArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 is_default: Optional[pulumi.Input[bool]] = None,
                 primary_email: Optional[pulumi.Input[str]] = None,
                 reply_to_address: Optional[pulumi.Input[str]] = None,
                 send_as_email: Optional[pulumi.Input[str]] = None,
                 signature: Optional[pulumi.Input[str]] = None,
                 smtp_msa: Optional[pulumi.Input[pulumi.InputType['GmailSendAsAliasSmtpMsaArgs']]] = None,
                 treat_as_alias: Optional[pulumi.Input[bool]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = GmailSendAsAliasArgs.__new__(GmailSendAsAliasArgs)

            __props__.__dict__["display_name"] = display_name
            __props__.__dict__["is_default"] = is_default
            if primary_email is None and not opts.urn:
                raise TypeError("Missing required property 'primary_email'")
            __props__.__dict__["primary_email"] = primary_email
            __props__.__dict__["reply_to_address"] = reply_to_address
            if send_as_email is None and not opts.urn:
                raise TypeError("Missing required property 'send_as_email'")
            __props__.__dict__["send_as_email"] = send_as_email
            __props__.__dict__["signature"] = signature
            __props__.__dict__["smtp_msa"] = smtp_msa
            __props__.__dict__["treat_as_alias"] = treat_as_alias
            __props__.__dict__["is_primary"] = None
            __props__.__dict__["verification_status"] = None
        super(GmailSendAsAlias, __self__).__init__(
            'googleworkspace:index/gmailSendAsAlias:GmailSendAsAlias',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            display_name: Optional[pulumi.Input[str]] = None,
            is_default: Optional[pulumi.Input[bool]] = None,
            is_primary: Optional[pulumi.Input[bool]] = None,
            primary_email: Optional[pulumi.Input[str]] = None,
            reply_to_address: Optional[pulumi.Input[str]] = None,
            send_as_email: Optional[pulumi.Input[str]] = None,
            signature: Optional[pulumi.Input[str]] = None,
            smtp_msa: Optional[pulumi.Input[pulumi.InputType['GmailSendAsAliasSmtpMsaArgs']]] = None,
            treat_as_alias: Optional[pulumi.Input[bool]] = None,
            verification_status: Optional[pulumi.Input[str]] = None) -> 'GmailSendAsAlias':
        """
        Get an existing GmailSendAsAlias resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] display_name: A name that appears in the 'From:' header for mail sent using this alias. For custom 'from' addresses, when this is empty, Gmail will populate the 'From:' header with the name that is used for the primary address associated with the account. If the admin has disabled the ability for users to update their name format, requests to update this field for the primary login will silently fail.
        :param pulumi.Input[bool] is_default: Whether this address is selected as the default 'From:' address in situations such as composing a new message or sending
               a vacation auto-reply. Every Gmail account has exactly one default send-as address, so the only legal value that clients
               may write to this field is true. Changing this from false to true for an address will result in this field becoming
               false for the other previous default address. Toggling an existing alias' default to false is not possible, another
               alias must be added/imported and toggled to true to remove the default from an existing alias. To avoid drift with
               Terraform, please change the previous default's config to false AFTER a new default is applied and perform a refresh to
               synchronize with remote state.
        :param pulumi.Input[bool] is_primary: Whether this address is the primary address used to login to the account. Every Gmail account has exactly one primary address, and it cannot be deleted from the collection of send-as aliases.
        :param pulumi.Input[str] primary_email: User's primary email address.
        :param pulumi.Input[str] reply_to_address: An optional email address that is included in a 'Reply-To:' header for mail sent using this alias. If this is empty, Gmail will not generate a 'Reply-To:' header.
        :param pulumi.Input[str] send_as_email: The email address that appears in the 'From:' header for mail sent using this alias.
        :param pulumi.Input[str] signature: An optional HTML signature that is included in messages composed with this alias in the Gmail web UI. This signature is added to new emails only.
        :param pulumi.Input[pulumi.InputType['GmailSendAsAliasSmtpMsaArgs']] smtp_msa: An optional SMTP service that will be used as an outbound relay for mail sent using this alias. If this is empty, outbound mail will be sent directly from Gmail's servers to the destination SMTP service. This setting only applies to custom 'from' aliases.
        :param pulumi.Input[bool] treat_as_alias: Defaults to `true`. Whether Gmail should treat this address as an alias for the user's primary email address. This setting only applies to custom 'from' aliases. See https://support.google.com/a/answer/1710338 for help on making this decision
        :param pulumi.Input[str] verification_status: Indicates whether this address has been verified for use as a send-as alias.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _GmailSendAsAliasState.__new__(_GmailSendAsAliasState)

        __props__.__dict__["display_name"] = display_name
        __props__.__dict__["is_default"] = is_default
        __props__.__dict__["is_primary"] = is_primary
        __props__.__dict__["primary_email"] = primary_email
        __props__.__dict__["reply_to_address"] = reply_to_address
        __props__.__dict__["send_as_email"] = send_as_email
        __props__.__dict__["signature"] = signature
        __props__.__dict__["smtp_msa"] = smtp_msa
        __props__.__dict__["treat_as_alias"] = treat_as_alias
        __props__.__dict__["verification_status"] = verification_status
        return GmailSendAsAlias(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[Optional[str]]:
        """
        A name that appears in the 'From:' header for mail sent using this alias. For custom 'from' addresses, when this is empty, Gmail will populate the 'From:' header with the name that is used for the primary address associated with the account. If the admin has disabled the ability for users to update their name format, requests to update this field for the primary login will silently fail.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter(name="isDefault")
    def is_default(self) -> pulumi.Output[Optional[bool]]:
        """
        Whether this address is selected as the default 'From:' address in situations such as composing a new message or sending
        a vacation auto-reply. Every Gmail account has exactly one default send-as address, so the only legal value that clients
        may write to this field is true. Changing this from false to true for an address will result in this field becoming
        false for the other previous default address. Toggling an existing alias' default to false is not possible, another
        alias must be added/imported and toggled to true to remove the default from an existing alias. To avoid drift with
        Terraform, please change the previous default's config to false AFTER a new default is applied and perform a refresh to
        synchronize with remote state.
        """
        return pulumi.get(self, "is_default")

    @property
    @pulumi.getter(name="isPrimary")
    def is_primary(self) -> pulumi.Output[bool]:
        """
        Whether this address is the primary address used to login to the account. Every Gmail account has exactly one primary address, and it cannot be deleted from the collection of send-as aliases.
        """
        return pulumi.get(self, "is_primary")

    @property
    @pulumi.getter(name="primaryEmail")
    def primary_email(self) -> pulumi.Output[str]:
        """
        User's primary email address.
        """
        return pulumi.get(self, "primary_email")

    @property
    @pulumi.getter(name="replyToAddress")
    def reply_to_address(self) -> pulumi.Output[Optional[str]]:
        """
        An optional email address that is included in a 'Reply-To:' header for mail sent using this alias. If this is empty, Gmail will not generate a 'Reply-To:' header.
        """
        return pulumi.get(self, "reply_to_address")

    @property
    @pulumi.getter(name="sendAsEmail")
    def send_as_email(self) -> pulumi.Output[str]:
        """
        The email address that appears in the 'From:' header for mail sent using this alias.
        """
        return pulumi.get(self, "send_as_email")

    @property
    @pulumi.getter
    def signature(self) -> pulumi.Output[Optional[str]]:
        """
        An optional HTML signature that is included in messages composed with this alias in the Gmail web UI. This signature is added to new emails only.
        """
        return pulumi.get(self, "signature")

    @property
    @pulumi.getter(name="smtpMsa")
    def smtp_msa(self) -> pulumi.Output[Optional['outputs.GmailSendAsAliasSmtpMsa']]:
        """
        An optional SMTP service that will be used as an outbound relay for mail sent using this alias. If this is empty, outbound mail will be sent directly from Gmail's servers to the destination SMTP service. This setting only applies to custom 'from' aliases.
        """
        return pulumi.get(self, "smtp_msa")

    @property
    @pulumi.getter(name="treatAsAlias")
    def treat_as_alias(self) -> pulumi.Output[Optional[bool]]:
        """
        Defaults to `true`. Whether Gmail should treat this address as an alias for the user's primary email address. This setting only applies to custom 'from' aliases. See https://support.google.com/a/answer/1710338 for help on making this decision
        """
        return pulumi.get(self, "treat_as_alias")

    @property
    @pulumi.getter(name="verificationStatus")
    def verification_status(self) -> pulumi.Output[str]:
        """
        Indicates whether this address has been verified for use as a send-as alias.
        """
        return pulumi.get(self, "verification_status")

