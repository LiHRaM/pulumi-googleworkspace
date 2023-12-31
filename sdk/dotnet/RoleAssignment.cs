// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Googleworkspace
{
    /// <summary>
    /// ## Import
    /// 
    /// ```sh
    ///  $ pulumi import googleworkspace:index/roleAssignment:RoleAssignment dwight 12345678901234567
    /// ```
    /// </summary>
    [GoogleworkspaceResourceType("googleworkspace:index/roleAssignment:RoleAssignment")]
    public partial class RoleAssignment : global::Pulumi.CustomResource
    {
        /// <summary>
        /// The unique ID of the user this role is assigned to.
        /// </summary>
        [Output("assignedTo")]
        public Output<string> AssignedTo { get; private set; } = null!;

        /// <summary>
        /// ETag of the resource.
        /// </summary>
        [Output("etag")]
        public Output<string> Etag { get; private set; } = null!;

        /// <summary>
        /// If the role is restricted to an organization unit, this contains the ID for the organization unit the exercise of this
        /// role is restricted to.
        /// </summary>
        [Output("orgUnitId")]
        public Output<string?> OrgUnitId { get; private set; } = null!;

        /// <summary>
        /// The ID of the role that is assigned.
        /// </summary>
        [Output("roleId")]
        public Output<string> RoleId { get; private set; } = null!;

        /// <summary>
        /// The scope in which this role is assigned. Valid values are : - `CUSTOMER` - `ORG_UNIT`
        /// </summary>
        [Output("scopeType")]
        public Output<string?> ScopeType { get; private set; } = null!;


        /// <summary>
        /// Create a RoleAssignment resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public RoleAssignment(string name, RoleAssignmentArgs args, CustomResourceOptions? options = null)
            : base("googleworkspace:index/roleAssignment:RoleAssignment", name, args ?? new RoleAssignmentArgs(), MakeResourceOptions(options, ""))
        {
        }

        private RoleAssignment(string name, Input<string> id, RoleAssignmentState? state = null, CustomResourceOptions? options = null)
            : base("googleworkspace:index/roleAssignment:RoleAssignment", name, state, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing RoleAssignment resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static RoleAssignment Get(string name, Input<string> id, RoleAssignmentState? state = null, CustomResourceOptions? options = null)
        {
            return new RoleAssignment(name, id, state, options);
        }
    }

    public sealed class RoleAssignmentArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The unique ID of the user this role is assigned to.
        /// </summary>
        [Input("assignedTo", required: true)]
        public Input<string> AssignedTo { get; set; } = null!;

        /// <summary>
        /// If the role is restricted to an organization unit, this contains the ID for the organization unit the exercise of this
        /// role is restricted to.
        /// </summary>
        [Input("orgUnitId")]
        public Input<string>? OrgUnitId { get; set; }

        /// <summary>
        /// The ID of the role that is assigned.
        /// </summary>
        [Input("roleId", required: true)]
        public Input<string> RoleId { get; set; } = null!;

        /// <summary>
        /// The scope in which this role is assigned. Valid values are : - `CUSTOMER` - `ORG_UNIT`
        /// </summary>
        [Input("scopeType")]
        public Input<string>? ScopeType { get; set; }

        public RoleAssignmentArgs()
        {
        }
        public static new RoleAssignmentArgs Empty => new RoleAssignmentArgs();
    }

    public sealed class RoleAssignmentState : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The unique ID of the user this role is assigned to.
        /// </summary>
        [Input("assignedTo")]
        public Input<string>? AssignedTo { get; set; }

        /// <summary>
        /// ETag of the resource.
        /// </summary>
        [Input("etag")]
        public Input<string>? Etag { get; set; }

        /// <summary>
        /// If the role is restricted to an organization unit, this contains the ID for the organization unit the exercise of this
        /// role is restricted to.
        /// </summary>
        [Input("orgUnitId")]
        public Input<string>? OrgUnitId { get; set; }

        /// <summary>
        /// The ID of the role that is assigned.
        /// </summary>
        [Input("roleId")]
        public Input<string>? RoleId { get; set; }

        /// <summary>
        /// The scope in which this role is assigned. Valid values are : - `CUSTOMER` - `ORG_UNIT`
        /// </summary>
        [Input("scopeType")]
        public Input<string>? ScopeType { get; set; }

        public RoleAssignmentState()
        {
        }
        public static new RoleAssignmentState Empty => new RoleAssignmentState();
    }
}
