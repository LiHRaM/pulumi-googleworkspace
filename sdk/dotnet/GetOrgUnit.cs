// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Googleworkspace
{
    public static class GetOrgUnit
    {
        /// <summary>
        /// {{% examples %}}
        /// ## Example Usage
        /// {{% example %}}
        /// 
        /// ```csharp
        /// using System.Collections.Generic;
        /// using Pulumi;
        /// using Googleworkspace = Pulumi.Googleworkspace;
        /// 
        /// return await Deployment.RunAsync(() =&gt; 
        /// {
        ///     var org = Googleworkspace.GetOrgUnit.Invoke(new()
        ///     {
        ///         OrgUnitId = "id:01ab2c3d4efg56h",
        ///     });
        /// 
        /// });
        /// ```
        /// {{% /example %}}
        /// {{% /examples %}}
        /// </summary>
        public static Task<GetOrgUnitResult> InvokeAsync(GetOrgUnitArgs? args = null, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetOrgUnitResult>("googleworkspace:index/getOrgUnit:getOrgUnit", args ?? new GetOrgUnitArgs(), options.WithDefaults());

        /// <summary>
        /// {{% examples %}}
        /// ## Example Usage
        /// {{% example %}}
        /// 
        /// ```csharp
        /// using System.Collections.Generic;
        /// using Pulumi;
        /// using Googleworkspace = Pulumi.Googleworkspace;
        /// 
        /// return await Deployment.RunAsync(() =&gt; 
        /// {
        ///     var org = Googleworkspace.GetOrgUnit.Invoke(new()
        ///     {
        ///         OrgUnitId = "id:01ab2c3d4efg56h",
        ///     });
        /// 
        /// });
        /// ```
        /// {{% /example %}}
        /// {{% /examples %}}
        /// </summary>
        public static Output<GetOrgUnitResult> Invoke(GetOrgUnitInvokeArgs? args = null, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.Invoke<GetOrgUnitResult>("googleworkspace:index/getOrgUnit:getOrgUnit", args ?? new GetOrgUnitInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetOrgUnitArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// The unique ID of the organizational unit.
        /// </summary>
        [Input("orgUnitId")]
        public string? OrgUnitId { get; set; }

        /// <summary>
        /// The full path to the organizational unit. The orgUnitPath is a derived property. When listed, it is derived from parentOrgunitPath and organizational unit's name. For example, for an organizational unit named 'apps' under parent organization '/engineering', the orgUnitPath is '/engineering/apps'. In order to edit an orgUnitPath, either update the name of the organization or the parentOrgunitPath. A user's organizational unit determines which Google Workspace services the user has access to. If the user is moved to a new organization, the user's access changes. For more information about organization structures, see the [administration help center](https://support.google.com/a/answer/4352075). For more information about moving a user to a different organization, see [chromeosdevices.update a user](https://developers.google.com/admin-sdk/directory/v1/guides/manage-users#update_user).
        /// </summary>
        [Input("orgUnitPath")]
        public string? OrgUnitPath { get; set; }

        public GetOrgUnitArgs()
        {
        }
        public static new GetOrgUnitArgs Empty => new GetOrgUnitArgs();
    }

    public sealed class GetOrgUnitInvokeArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// The unique ID of the organizational unit.
        /// </summary>
        [Input("orgUnitId")]
        public Input<string>? OrgUnitId { get; set; }

        /// <summary>
        /// The full path to the organizational unit. The orgUnitPath is a derived property. When listed, it is derived from parentOrgunitPath and organizational unit's name. For example, for an organizational unit named 'apps' under parent organization '/engineering', the orgUnitPath is '/engineering/apps'. In order to edit an orgUnitPath, either update the name of the organization or the parentOrgunitPath. A user's organizational unit determines which Google Workspace services the user has access to. If the user is moved to a new organization, the user's access changes. For more information about organization structures, see the [administration help center](https://support.google.com/a/answer/4352075). For more information about moving a user to a different organization, see [chromeosdevices.update a user](https://developers.google.com/admin-sdk/directory/v1/guides/manage-users#update_user).
        /// </summary>
        [Input("orgUnitPath")]
        public Input<string>? OrgUnitPath { get; set; }

        public GetOrgUnitInvokeArgs()
        {
        }
        public static new GetOrgUnitInvokeArgs Empty => new GetOrgUnitInvokeArgs();
    }


    [OutputType]
    public sealed class GetOrgUnitResult
    {
        /// <summary>
        /// Determines if a sub-organizational unit can inherit the settings of the parent organization. False means a sub-organizational unit inherits the settings of the nearest parent organizational unit. For more information on inheritance and users in an organization structure, see the [administration help center](https://support.google.com/a/answer/4352075).
        /// </summary>
        public readonly bool BlockInheritance;
        /// <summary>
        /// Description of the organizational unit.
        /// </summary>
        public readonly string Description;
        /// <summary>
        /// ETag of the resource.
        /// </summary>
        public readonly string Etag;
        /// <summary>
        /// The ID of this resource.
        /// </summary>
        public readonly string Id;
        /// <summary>
        /// The organizational unit's path name. For example, an organizational unit's name within the /corp/support/sales*support parent path is sales*support.
        /// </summary>
        public readonly string Name;
        /// <summary>
        /// The unique ID of the organizational unit.
        /// </summary>
        public readonly string OrgUnitId;
        /// <summary>
        /// The full path to the organizational unit. The orgUnitPath is a derived property. When listed, it is derived from parentOrgunitPath and organizational unit's name. For example, for an organizational unit named 'apps' under parent organization '/engineering', the orgUnitPath is '/engineering/apps'. In order to edit an orgUnitPath, either update the name of the organization or the parentOrgunitPath. A user's organizational unit determines which Google Workspace services the user has access to. If the user is moved to a new organization, the user's access changes. For more information about organization structures, see the [administration help center](https://support.google.com/a/answer/4352075). For more information about moving a user to a different organization, see [chromeosdevices.update a user](https://developers.google.com/admin-sdk/directory/v1/guides/manage-users#update_user).
        /// </summary>
        public readonly string OrgUnitPath;
        /// <summary>
        /// The unique ID of the parent organizational unit.
        /// </summary>
        public readonly string ParentOrgUnitId;
        /// <summary>
        /// The organizational unit's parent path. For example, /corp/sales is the parent path for /corp/sales/sales_support organizational unit.
        /// </summary>
        public readonly string ParentOrgUnitPath;

        [OutputConstructor]
        private GetOrgUnitResult(
            bool blockInheritance,

            string description,

            string etag,

            string id,

            string name,

            string orgUnitId,

            string orgUnitPath,

            string parentOrgUnitId,

            string parentOrgUnitPath)
        {
            BlockInheritance = blockInheritance;
            Description = description;
            Etag = etag;
            Id = id;
            Name = name;
            OrgUnitId = orgUnitId;
            OrgUnitPath = orgUnitPath;
            ParentOrgUnitId = parentOrgUnitId;
            ParentOrgUnitPath = parentOrgUnitPath;
        }
    }
}
