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
    /// Domain resource manages Google Workspace Domains. Domain resides under the `https://www.googleapis.com/auth/admin.directory.domain` client scope.
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
    ///     var example = new Googleworkspace.Domain("example", new()
    ///     {
    ///         DomainName = "example.com",
    ///     });
    /// 
    /// });
    /// ```
    /// 
    /// ## Import
    /// 
    /// ```sh
    ///  $ pulumi import googleworkspace:index/domain:Domain example example.com
    /// ```
    /// </summary>
    [GoogleworkspaceResourceType("googleworkspace:index/domain:Domain")]
    public partial class Domain : global::Pulumi.CustomResource
    {
        /// <summary>
        /// Creation time of the domain. Expressed in Unix time format.
        /// </summary>
        [Output("creationTime")]
        public Output<int> CreationTime { get; private set; } = null!;

        /// <summary>
        /// asps.list of domain alias objects.
        /// </summary>
        [Output("domainAliases")]
        public Output<ImmutableArray<string>> DomainAliases { get; private set; } = null!;

        /// <summary>
        /// The domain name of the customer.
        /// </summary>
        [Output("domainName")]
        public Output<string> DomainName { get; private set; } = null!;

        /// <summary>
        /// ETag of the resource.
        /// </summary>
        [Output("etag")]
        public Output<string> Etag { get; private set; } = null!;

        /// <summary>
        /// Indicates if the domain is a primary domain.
        /// </summary>
        [Output("isPrimary")]
        public Output<bool> IsPrimary { get; private set; } = null!;

        /// <summary>
        /// Indicates the verification state of a domain.
        /// </summary>
        [Output("verified")]
        public Output<bool> Verified { get; private set; } = null!;


        /// <summary>
        /// Create a Domain resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Domain(string name, DomainArgs args, CustomResourceOptions? options = null)
            : base("googleworkspace:index/domain:Domain", name, args ?? new DomainArgs(), MakeResourceOptions(options, ""))
        {
        }

        private Domain(string name, Input<string> id, DomainState? state = null, CustomResourceOptions? options = null)
            : base("googleworkspace:index/domain:Domain", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing Domain resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static Domain Get(string name, Input<string> id, DomainState? state = null, CustomResourceOptions? options = null)
        {
            return new Domain(name, id, state, options);
        }
    }

    public sealed class DomainArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The domain name of the customer.
        /// </summary>
        [Input("domainName", required: true)]
        public Input<string> DomainName { get; set; } = null!;

        public DomainArgs()
        {
        }
        public static new DomainArgs Empty => new DomainArgs();
    }

    public sealed class DomainState : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// Creation time of the domain. Expressed in Unix time format.
        /// </summary>
        [Input("creationTime")]
        public Input<int>? CreationTime { get; set; }

        [Input("domainAliases")]
        private InputList<string>? _domainAliases;

        /// <summary>
        /// asps.list of domain alias objects.
        /// </summary>
        public InputList<string> DomainAliases
        {
            get => _domainAliases ?? (_domainAliases = new InputList<string>());
            set => _domainAliases = value;
        }

        /// <summary>
        /// The domain name of the customer.
        /// </summary>
        [Input("domainName")]
        public Input<string>? DomainName { get; set; }

        /// <summary>
        /// ETag of the resource.
        /// </summary>
        [Input("etag")]
        public Input<string>? Etag { get; set; }

        /// <summary>
        /// Indicates if the domain is a primary domain.
        /// </summary>
        [Input("isPrimary")]
        public Input<bool>? IsPrimary { get; set; }

        /// <summary>
        /// Indicates the verification state of a domain.
        /// </summary>
        [Input("verified")]
        public Input<bool>? Verified { get; set; }

        public DomainState()
        {
        }
        public static new DomainState Empty => new DomainState();
    }
}
