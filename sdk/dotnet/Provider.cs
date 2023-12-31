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
    /// The provider type for the googleworkspace package. By default, resources use package-wide configuration
    /// settings, however an explicit `Provider` instance may be created and passed during resource
    /// construction to achieve fine-grained programmatic control over provider settings. See the
    /// [documentation](https://www.pulumi.com/docs/reference/programming-model/#providers) for more information.
    /// </summary>
    [GoogleworkspaceResourceType("pulumi:providers:googleworkspace")]
    public partial class Provider : global::Pulumi.ProviderResource
    {
        /// <summary>
        /// A temporary [OAuth 2.0 access token] obtained from the Google Authorization server, i.e. the `Authorization: Bearer`
        /// token used to authenticate HTTP requests to Google Admin SDK APIs. This is an alternative to `credentials`, and ignores
        /// the `oauth_scopes` field. If both are specified, `access_token` will be used over the `credentials` field.
        /// </summary>
        [Output("accessToken")]
        public Output<string?> AccessToken { get; private set; } = null!;

        /// <summary>
        /// Either the path to or the contents of a service account key file in JSON format you can manage key files using the Cloud
        /// Console). If not provided, the application default credentials will be used.
        /// </summary>
        [Output("credentials")]
        public Output<string?> Credentials { get; private set; } = null!;

        /// <summary>
        /// The customer id provided with your Google Workspace subscription. It is found in the admin console under Account
        /// Settings.
        /// </summary>
        [Output("customerId")]
        public Output<string?> CustomerId { get; private set; } = null!;

        /// <summary>
        /// The impersonated user's email with access to the Admin APIs can access the Admin SDK Directory API.
        /// `impersonated_user_email` is required for all services except group and user management.
        /// </summary>
        [Output("impersonatedUserEmail")]
        public Output<string?> ImpersonatedUserEmail { get; private set; } = null!;

        /// <summary>
        /// The service account used to create the provided `access_token` if authenticating using the `access_token` method and
        /// needing to impersonate a user. This service account will require the GCP role `Service Account Token Creator` if needing
        /// to impersonate a user.
        /// </summary>
        [Output("serviceAccount")]
        public Output<string?> ServiceAccount { get; private set; } = null!;


        /// <summary>
        /// Create a Provider resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Provider(string name, ProviderArgs? args = null, CustomResourceOptions? options = null)
            : base("googleworkspace", name, args ?? new ProviderArgs(), MakeResourceOptions(options, ""))
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
    }

    public sealed class ProviderArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// A temporary [OAuth 2.0 access token] obtained from the Google Authorization server, i.e. the `Authorization: Bearer`
        /// token used to authenticate HTTP requests to Google Admin SDK APIs. This is an alternative to `credentials`, and ignores
        /// the `oauth_scopes` field. If both are specified, `access_token` will be used over the `credentials` field.
        /// </summary>
        [Input("accessToken")]
        public Input<string>? AccessToken { get; set; }

        /// <summary>
        /// Either the path to or the contents of a service account key file in JSON format you can manage key files using the Cloud
        /// Console). If not provided, the application default credentials will be used.
        /// </summary>
        [Input("credentials")]
        public Input<string>? Credentials { get; set; }

        /// <summary>
        /// The customer id provided with your Google Workspace subscription. It is found in the admin console under Account
        /// Settings.
        /// </summary>
        [Input("customerId")]
        public Input<string>? CustomerId { get; set; }

        /// <summary>
        /// The impersonated user's email with access to the Admin APIs can access the Admin SDK Directory API.
        /// `impersonated_user_email` is required for all services except group and user management.
        /// </summary>
        [Input("impersonatedUserEmail")]
        public Input<string>? ImpersonatedUserEmail { get; set; }

        [Input("oauthScopes", json: true)]
        private InputList<string>? _oauthScopes;

        /// <summary>
        /// The list of the scopes required for your application (for a list of possible scopes, see [Authorize
        /// requests](https://developers.google.com/admin-sdk/directory/v1/guides/authorizing))
        /// </summary>
        public InputList<string> OauthScopes
        {
            get => _oauthScopes ?? (_oauthScopes = new InputList<string>());
            set => _oauthScopes = value;
        }

        /// <summary>
        /// The service account used to create the provided `access_token` if authenticating using the `access_token` method and
        /// needing to impersonate a user. This service account will require the GCP role `Service Account Token Creator` if needing
        /// to impersonate a user.
        /// </summary>
        [Input("serviceAccount")]
        public Input<string>? ServiceAccount { get; set; }

        public ProviderArgs()
        {
        }
        public static new ProviderArgs Empty => new ProviderArgs();
    }
}
