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
    'GetChromePolicySchemaResult',
    'AwaitableGetChromePolicySchemaResult',
    'get_chrome_policy_schema',
    'get_chrome_policy_schema_output',
]

@pulumi.output_type
class GetChromePolicySchemaResult:
    """
    A collection of values returned by getChromePolicySchema.
    """
    def __init__(__self__, access_restrictions=None, additional_target_key_names=None, definitions=None, field_descriptions=None, id=None, notices=None, policy_description=None, schema_name=None, support_uri=None):
        if access_restrictions and not isinstance(access_restrictions, list):
            raise TypeError("Expected argument 'access_restrictions' to be a list")
        pulumi.set(__self__, "access_restrictions", access_restrictions)
        if additional_target_key_names and not isinstance(additional_target_key_names, list):
            raise TypeError("Expected argument 'additional_target_key_names' to be a list")
        pulumi.set(__self__, "additional_target_key_names", additional_target_key_names)
        if definitions and not isinstance(definitions, list):
            raise TypeError("Expected argument 'definitions' to be a list")
        pulumi.set(__self__, "definitions", definitions)
        if field_descriptions and not isinstance(field_descriptions, str):
            raise TypeError("Expected argument 'field_descriptions' to be a str")
        pulumi.set(__self__, "field_descriptions", field_descriptions)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if notices and not isinstance(notices, list):
            raise TypeError("Expected argument 'notices' to be a list")
        pulumi.set(__self__, "notices", notices)
        if policy_description and not isinstance(policy_description, str):
            raise TypeError("Expected argument 'policy_description' to be a str")
        pulumi.set(__self__, "policy_description", policy_description)
        if schema_name and not isinstance(schema_name, str):
            raise TypeError("Expected argument 'schema_name' to be a str")
        pulumi.set(__self__, "schema_name", schema_name)
        if support_uri and not isinstance(support_uri, str):
            raise TypeError("Expected argument 'support_uri' to be a str")
        pulumi.set(__self__, "support_uri", support_uri)

    @property
    @pulumi.getter(name="accessRestrictions")
    def access_restrictions(self) -> Sequence[str]:
        """
        Specific access restrictions related to this policy.
        """
        return pulumi.get(self, "access_restrictions")

    @property
    @pulumi.getter(name="additionalTargetKeyNames")
    def additional_target_key_names(self) -> Sequence['outputs.GetChromePolicySchemaAdditionalTargetKeyNameResult']:
        """
        Additional key names that will be used to identify the target of the policy value. When specifying a policyTargetKey, each of the additional keys specified here will have to be included in the additionalTargetKeys map.
        """
        return pulumi.get(self, "additional_target_key_names")

    @property
    @pulumi.getter
    def definitions(self) -> Sequence['outputs.GetChromePolicySchemaDefinitionResult']:
        """
        Schema definition using proto descriptor.
        """
        return pulumi.get(self, "definitions")

    @property
    @pulumi.getter(name="fieldDescriptions")
    def field_descriptions(self) -> str:
        """
        Detailed description of each field that is part of the schema, represented as a JSON string.
        """
        return pulumi.get(self, "field_descriptions")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def notices(self) -> Sequence['outputs.GetChromePolicySchemaNoticeResult']:
        """
        Special notice messages related to setting certain values in certain fields in the schema.
        """
        return pulumi.get(self, "notices")

    @property
    @pulumi.getter(name="policyDescription")
    def policy_description(self) -> str:
        """
        Description about the policy schema for user consumption.
        """
        return pulumi.get(self, "policy_description")

    @property
    @pulumi.getter(name="schemaName")
    def schema_name(self) -> str:
        """
        The full qualified name of the policy schema
        """
        return pulumi.get(self, "schema_name")

    @property
    @pulumi.getter(name="supportUri")
    def support_uri(self) -> str:
        """
        URI to related support article for this schema.
        """
        return pulumi.get(self, "support_uri")


class AwaitableGetChromePolicySchemaResult(GetChromePolicySchemaResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetChromePolicySchemaResult(
            access_restrictions=self.access_restrictions,
            additional_target_key_names=self.additional_target_key_names,
            definitions=self.definitions,
            field_descriptions=self.field_descriptions,
            id=self.id,
            notices=self.notices,
            policy_description=self.policy_description,
            schema_name=self.schema_name,
            support_uri=self.support_uri)


def get_chrome_policy_schema(schema_name: Optional[str] = None,
                             opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetChromePolicySchemaResult:
    """
    ## Example Usage

    ```python
    import pulumi
    import pulumi_googleworkspace as googleworkspace

    example = googleworkspace.get_chrome_policy_schema(schema_name="chrome.printers.AllowForUsers")
    pulumi.export("fieldDescriptions", example.field_descriptions)
    ```


    :param str schema_name: The full qualified name of the policy schema
    """
    __args__ = dict()
    __args__['schemaName'] = schema_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('googleworkspace:index/getChromePolicySchema:getChromePolicySchema', __args__, opts=opts, typ=GetChromePolicySchemaResult).value

    return AwaitableGetChromePolicySchemaResult(
        access_restrictions=__ret__.access_restrictions,
        additional_target_key_names=__ret__.additional_target_key_names,
        definitions=__ret__.definitions,
        field_descriptions=__ret__.field_descriptions,
        id=__ret__.id,
        notices=__ret__.notices,
        policy_description=__ret__.policy_description,
        schema_name=__ret__.schema_name,
        support_uri=__ret__.support_uri)


@_utilities.lift_output_func(get_chrome_policy_schema)
def get_chrome_policy_schema_output(schema_name: Optional[pulumi.Input[str]] = None,
                                    opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetChromePolicySchemaResult]:
    """
    ## Example Usage

    ```python
    import pulumi
    import pulumi_googleworkspace as googleworkspace

    example = googleworkspace.get_chrome_policy_schema(schema_name="chrome.printers.AllowForUsers")
    pulumi.export("fieldDescriptions", example.field_descriptions)
    ```


    :param str schema_name: The full qualified name of the policy schema
    """
    ...