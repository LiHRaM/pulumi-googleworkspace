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
    /// Group resource manages Google Workspace Groups. Group resides under the `https://www.googleapis.com/auth/admin.directory.group` client scope.
    /// 
    /// ## Example Usage
    /// 
    /// ```csharp
    /// using System.Collections.Generic;
    /// using Pulumi;
    /// using Googleworkspace = Pulumi.Googleworkspace;
    /// 
    /// return await Deployment.RunAsync(() =&gt; 
    /// {
    ///     var sales = new Googleworkspace.Group("sales", new()
    ///     {
    ///         Aliases = new[]
    ///         {
    ///             "paper-sales@example.com",
    ///             "sales-dept@example.com",
    ///         },
    ///         Description = "Sales Group",
    ///         Email = "sales@example.com",
    ///     });
    /// 
    /// });
    /// ```
    /// 
    /// ## Import
    /// 
    /// ```sh
    ///  $ pulumi import googleworkspace:index/group:Group sales 01abcde23fg4h5i
    /// ```
    /// 
    /// # or with email as id
    /// 
    /// ```sh
    ///  $ pulumi import googleworkspace:index/group:Group sales sales@example.com
    /// ```
    /// </summary>
    [GoogleworkspaceResourceType("googleworkspace:index/group:Group")]
    public partial class Group : global::Pulumi.CustomResource
    {
        /// <summary>
        /// Value is true if this group was created by an administrator rather than a user.
        /// </summary>
        [Output("adminCreated")]
        public Output<bool> AdminCreated { get; private set; } = null!;

        /// <summary>
        /// asps.list of group's email addresses.
        /// </summary>
        [Output("aliases")]
        public Output<ImmutableArray<string>> Aliases { get; private set; } = null!;

        /// <summary>
        /// An extended description to help users determine the purpose of a group.For example, you can include information about who should join the group,the types of messages to send to the group, links to FAQs about the group, or related groups.
        /// </summary>
        [Output("description")]
        public Output<string?> Description { get; private set; } = null!;

        /// <summary>
        /// The number of users that are direct members of the group.If a group is a member (child) of this group (the parent),members of the child group are not counted in the directMembersCount property of the parent group.
        /// </summary>
        [Output("directMembersCount")]
        public Output<int> DirectMembersCount { get; private set; } = null!;

        /// <summary>
        /// The group's email address. If your account has multiple domains,select the appropriate domain for the email address. The email must be unique.
        /// </summary>
        [Output("email")]
        public Output<string> Email { get; private set; } = null!;

        /// <summary>
        /// ETag of the resource.
        /// </summary>
        [Output("etag")]
        public Output<string> Etag { get; private set; } = null!;

        /// <summary>
        /// The group's display name.
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        /// <summary>
        /// asps.list of the group's non-editable alias email addresses that are outside of the account's primary domain or subdomains. These are functioning email addresses used by the group.
        /// </summary>
        [Output("nonEditableAliases")]
        public Output<ImmutableArray<string>> NonEditableAliases { get; private set; } = null!;


        /// <summary>
        /// Create a Group resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Group(string name, GroupArgs args, CustomResourceOptions? options = null)
            : base("googleworkspace:index/group:Group", name, args ?? new GroupArgs(), MakeResourceOptions(options, ""))
        {
        }

        private Group(string name, Input<string> id, GroupState? state = null, CustomResourceOptions? options = null)
            : base("googleworkspace:index/group:Group", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing Group resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static Group Get(string name, Input<string> id, GroupState? state = null, CustomResourceOptions? options = null)
        {
            return new Group(name, id, state, options);
        }
    }

    public sealed class GroupArgs : global::Pulumi.ResourceArgs
    {
        [Input("aliases")]
        private InputList<string>? _aliases;

        /// <summary>
        /// asps.list of group's email addresses.
        /// </summary>
        public InputList<string> Aliases
        {
            get => _aliases ?? (_aliases = new InputList<string>());
            set => _aliases = value;
        }

        /// <summary>
        /// An extended description to help users determine the purpose of a group.For example, you can include information about who should join the group,the types of messages to send to the group, links to FAQs about the group, or related groups.
        /// </summary>
        [Input("description")]
        public Input<string>? Description { get; set; }

        /// <summary>
        /// The group's email address. If your account has multiple domains,select the appropriate domain for the email address. The email must be unique.
        /// </summary>
        [Input("email", required: true)]
        public Input<string> Email { get; set; } = null!;

        /// <summary>
        /// The group's display name.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        public GroupArgs()
        {
        }
        public static new GroupArgs Empty => new GroupArgs();
    }

    public sealed class GroupState : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// Value is true if this group was created by an administrator rather than a user.
        /// </summary>
        [Input("adminCreated")]
        public Input<bool>? AdminCreated { get; set; }

        [Input("aliases")]
        private InputList<string>? _aliases;

        /// <summary>
        /// asps.list of group's email addresses.
        /// </summary>
        public InputList<string> Aliases
        {
            get => _aliases ?? (_aliases = new InputList<string>());
            set => _aliases = value;
        }

        /// <summary>
        /// An extended description to help users determine the purpose of a group.For example, you can include information about who should join the group,the types of messages to send to the group, links to FAQs about the group, or related groups.
        /// </summary>
        [Input("description")]
        public Input<string>? Description { get; set; }

        /// <summary>
        /// The number of users that are direct members of the group.If a group is a member (child) of this group (the parent),members of the child group are not counted in the directMembersCount property of the parent group.
        /// </summary>
        [Input("directMembersCount")]
        public Input<int>? DirectMembersCount { get; set; }

        /// <summary>
        /// The group's email address. If your account has multiple domains,select the appropriate domain for the email address. The email must be unique.
        /// </summary>
        [Input("email")]
        public Input<string>? Email { get; set; }

        /// <summary>
        /// ETag of the resource.
        /// </summary>
        [Input("etag")]
        public Input<string>? Etag { get; set; }

        /// <summary>
        /// The group's display name.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        [Input("nonEditableAliases")]
        private InputList<string>? _nonEditableAliases;

        /// <summary>
        /// asps.list of the group's non-editable alias email addresses that are outside of the account's primary domain or subdomains. These are functioning email addresses used by the group.
        /// </summary>
        public InputList<string> NonEditableAliases
        {
            get => _nonEditableAliases ?? (_nonEditableAliases = new InputList<string>());
            set => _nonEditableAliases = value;
        }

        public GroupState()
        {
        }
        public static new GroupState Empty => new GroupState();
    }
}
