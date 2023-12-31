# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['DomainArgs', 'Domain']

@pulumi.input_type
class DomainArgs:
    def __init__(__self__, *,
                 domain_name: pulumi.Input[str]):
        """
        The set of arguments for constructing a Domain resource.
        :param pulumi.Input[str] domain_name: The domain name of the customer.
        """
        pulumi.set(__self__, "domain_name", domain_name)

    @property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> pulumi.Input[str]:
        """
        The domain name of the customer.
        """
        return pulumi.get(self, "domain_name")

    @domain_name.setter
    def domain_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "domain_name", value)


@pulumi.input_type
class _DomainState:
    def __init__(__self__, *,
                 creation_time: Optional[pulumi.Input[int]] = None,
                 domain_aliases: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 domain_name: Optional[pulumi.Input[str]] = None,
                 etag: Optional[pulumi.Input[str]] = None,
                 is_primary: Optional[pulumi.Input[bool]] = None,
                 verified: Optional[pulumi.Input[bool]] = None):
        """
        Input properties used for looking up and filtering Domain resources.
        :param pulumi.Input[int] creation_time: Creation time of the domain. Expressed in Unix time format.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] domain_aliases: asps.list of domain alias objects.
        :param pulumi.Input[str] domain_name: The domain name of the customer.
        :param pulumi.Input[str] etag: ETag of the resource.
        :param pulumi.Input[bool] is_primary: Indicates if the domain is a primary domain.
        :param pulumi.Input[bool] verified: Indicates the verification state of a domain.
        """
        if creation_time is not None:
            pulumi.set(__self__, "creation_time", creation_time)
        if domain_aliases is not None:
            pulumi.set(__self__, "domain_aliases", domain_aliases)
        if domain_name is not None:
            pulumi.set(__self__, "domain_name", domain_name)
        if etag is not None:
            pulumi.set(__self__, "etag", etag)
        if is_primary is not None:
            pulumi.set(__self__, "is_primary", is_primary)
        if verified is not None:
            pulumi.set(__self__, "verified", verified)

    @property
    @pulumi.getter(name="creationTime")
    def creation_time(self) -> Optional[pulumi.Input[int]]:
        """
        Creation time of the domain. Expressed in Unix time format.
        """
        return pulumi.get(self, "creation_time")

    @creation_time.setter
    def creation_time(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "creation_time", value)

    @property
    @pulumi.getter(name="domainAliases")
    def domain_aliases(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        asps.list of domain alias objects.
        """
        return pulumi.get(self, "domain_aliases")

    @domain_aliases.setter
    def domain_aliases(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "domain_aliases", value)

    @property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> Optional[pulumi.Input[str]]:
        """
        The domain name of the customer.
        """
        return pulumi.get(self, "domain_name")

    @domain_name.setter
    def domain_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "domain_name", value)

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
    @pulumi.getter(name="isPrimary")
    def is_primary(self) -> Optional[pulumi.Input[bool]]:
        """
        Indicates if the domain is a primary domain.
        """
        return pulumi.get(self, "is_primary")

    @is_primary.setter
    def is_primary(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "is_primary", value)

    @property
    @pulumi.getter
    def verified(self) -> Optional[pulumi.Input[bool]]:
        """
        Indicates the verification state of a domain.
        """
        return pulumi.get(self, "verified")

    @verified.setter
    def verified(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "verified", value)


class Domain(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 domain_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Domain resource manages Google Workspace Domains. Domain resides under the `https://www.googleapis.com/auth/admin.directory.domain` client scope.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_googleworkspace as googleworkspace

        example = googleworkspace.Domain("example", domain_name="example.com")
        ```

        ## Import

        ```sh
         $ pulumi import googleworkspace:index/domain:Domain example example.com
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] domain_name: The domain name of the customer.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: DomainArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Domain resource manages Google Workspace Domains. Domain resides under the `https://www.googleapis.com/auth/admin.directory.domain` client scope.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_googleworkspace as googleworkspace

        example = googleworkspace.Domain("example", domain_name="example.com")
        ```

        ## Import

        ```sh
         $ pulumi import googleworkspace:index/domain:Domain example example.com
        ```

        :param str resource_name: The name of the resource.
        :param DomainArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(DomainArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 domain_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = DomainArgs.__new__(DomainArgs)

            if domain_name is None and not opts.urn:
                raise TypeError("Missing required property 'domain_name'")
            __props__.__dict__["domain_name"] = domain_name
            __props__.__dict__["creation_time"] = None
            __props__.__dict__["domain_aliases"] = None
            __props__.__dict__["etag"] = None
            __props__.__dict__["is_primary"] = None
            __props__.__dict__["verified"] = None
        super(Domain, __self__).__init__(
            'googleworkspace:index/domain:Domain',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            creation_time: Optional[pulumi.Input[int]] = None,
            domain_aliases: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            domain_name: Optional[pulumi.Input[str]] = None,
            etag: Optional[pulumi.Input[str]] = None,
            is_primary: Optional[pulumi.Input[bool]] = None,
            verified: Optional[pulumi.Input[bool]] = None) -> 'Domain':
        """
        Get an existing Domain resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[int] creation_time: Creation time of the domain. Expressed in Unix time format.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] domain_aliases: asps.list of domain alias objects.
        :param pulumi.Input[str] domain_name: The domain name of the customer.
        :param pulumi.Input[str] etag: ETag of the resource.
        :param pulumi.Input[bool] is_primary: Indicates if the domain is a primary domain.
        :param pulumi.Input[bool] verified: Indicates the verification state of a domain.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _DomainState.__new__(_DomainState)

        __props__.__dict__["creation_time"] = creation_time
        __props__.__dict__["domain_aliases"] = domain_aliases
        __props__.__dict__["domain_name"] = domain_name
        __props__.__dict__["etag"] = etag
        __props__.__dict__["is_primary"] = is_primary
        __props__.__dict__["verified"] = verified
        return Domain(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="creationTime")
    def creation_time(self) -> pulumi.Output[int]:
        """
        Creation time of the domain. Expressed in Unix time format.
        """
        return pulumi.get(self, "creation_time")

    @property
    @pulumi.getter(name="domainAliases")
    def domain_aliases(self) -> pulumi.Output[Sequence[str]]:
        """
        asps.list of domain alias objects.
        """
        return pulumi.get(self, "domain_aliases")

    @property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> pulumi.Output[str]:
        """
        The domain name of the customer.
        """
        return pulumi.get(self, "domain_name")

    @property
    @pulumi.getter
    def etag(self) -> pulumi.Output[str]:
        """
        ETag of the resource.
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter(name="isPrimary")
    def is_primary(self) -> pulumi.Output[bool]:
        """
        Indicates if the domain is a primary domain.
        """
        return pulumi.get(self, "is_primary")

    @property
    @pulumi.getter
    def verified(self) -> pulumi.Output[bool]:
        """
        Indicates the verification state of a domain.
        """
        return pulumi.get(self, "verified")

