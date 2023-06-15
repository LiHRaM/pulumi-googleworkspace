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
    'GetSchemaResult',
    'AwaitableGetSchemaResult',
    'get_schema',
    'get_schema_output',
]

@pulumi.output_type
class GetSchemaResult:
    """
    A collection of values returned by getSchema.
    """
    def __init__(__self__, display_name=None, etag=None, fields=None, id=None, schema_id=None, schema_name=None):
        if display_name and not isinstance(display_name, str):
            raise TypeError("Expected argument 'display_name' to be a str")
        pulumi.set(__self__, "display_name", display_name)
        if etag and not isinstance(etag, str):
            raise TypeError("Expected argument 'etag' to be a str")
        pulumi.set(__self__, "etag", etag)
        if fields and not isinstance(fields, list):
            raise TypeError("Expected argument 'fields' to be a list")
        pulumi.set(__self__, "fields", fields)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if schema_id and not isinstance(schema_id, str):
            raise TypeError("Expected argument 'schema_id' to be a str")
        pulumi.set(__self__, "schema_id", schema_id)
        if schema_name and not isinstance(schema_name, str):
            raise TypeError("Expected argument 'schema_name' to be a str")
        pulumi.set(__self__, "schema_name", schema_name)

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> str:
        """
        Display name for the schema.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter
    def etag(self) -> str:
        """
        ETag of the resource.
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter
    def fields(self) -> Sequence['outputs.GetSchemaFieldResult']:
        """
        A list of fields in the schema.
        """
        return pulumi.get(self, "fields")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The ID of this resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="schemaId")
    def schema_id(self) -> str:
        """
        The unique identifier of the schema.
        """
        return pulumi.get(self, "schema_id")

    @property
    @pulumi.getter(name="schemaName")
    def schema_name(self) -> str:
        """
        The schema's name.
        """
        return pulumi.get(self, "schema_name")


class AwaitableGetSchemaResult(GetSchemaResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetSchemaResult(
            display_name=self.display_name,
            etag=self.etag,
            fields=self.fields,
            id=self.id,
            schema_id=self.schema_id,
            schema_name=self.schema_name)


def get_schema(schema_id: Optional[str] = None,
               schema_name: Optional[str] = None,
               opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetSchemaResult:
    """
    ## Example Usage

    ```python
    import pulumi
    import pulumi_googleworkspace as googleworkspace

    birthday = googleworkspace.get_schema(schema_name="birthday")
    pulumi.export("schemaDisplayName", birthday.display_name)
    ```


    :param str schema_id: The unique identifier of the schema.
    :param str schema_name: The schema's name.
    """
    __args__ = dict()
    __args__['schemaId'] = schema_id
    __args__['schemaName'] = schema_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('googleworkspace:index/getSchema:getSchema', __args__, opts=opts, typ=GetSchemaResult).value

    return AwaitableGetSchemaResult(
        display_name=__ret__.display_name,
        etag=__ret__.etag,
        fields=__ret__.fields,
        id=__ret__.id,
        schema_id=__ret__.schema_id,
        schema_name=__ret__.schema_name)


@_utilities.lift_output_func(get_schema)
def get_schema_output(schema_id: Optional[pulumi.Input[Optional[str]]] = None,
                      schema_name: Optional[pulumi.Input[Optional[str]]] = None,
                      opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetSchemaResult]:
    """
    ## Example Usage

    ```python
    import pulumi
    import pulumi_googleworkspace as googleworkspace

    birthday = googleworkspace.get_schema(schema_name="birthday")
    pulumi.export("schemaDisplayName", birthday.display_name)
    ```


    :param str schema_id: The unique identifier of the schema.
    :param str schema_name: The schema's name.
    """
    ...
