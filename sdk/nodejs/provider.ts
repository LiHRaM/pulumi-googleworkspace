// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

/**
 * The provider type for the googleworkspace package. By default, resources use package-wide configuration
 * settings, however an explicit `Provider` instance may be created and passed during resource
 * construction to achieve fine-grained programmatic control over provider settings. See the
 * [documentation](https://www.pulumi.com/docs/reference/programming-model/#providers) for more information.
 */
export class Provider extends pulumi.ProviderResource {
    /** @internal */
    public static readonly __pulumiType = 'googleworkspace';

    /**
     * Returns true if the given object is an instance of Provider.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Provider {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Provider.__pulumiType;
    }

    /**
     * A temporary [OAuth 2.0 access token] obtained from the Google Authorization server, i.e. the `Authorization: Bearer`
     * token used to authenticate HTTP requests to Google Admin SDK APIs. This is an alternative to `credentials`, and ignores
     * the `oauth_scopes` field. If both are specified, `access_token` will be used over the `credentials` field.
     */
    public readonly accessToken!: pulumi.Output<string | undefined>;
    /**
     * Either the path to or the contents of a service account key file in JSON format you can manage key files using the Cloud
     * Console). If not provided, the application default credentials will be used.
     */
    public readonly credentials!: pulumi.Output<string | undefined>;
    /**
     * The customer id provided with your Google Workspace subscription. It is found in the admin console under Account
     * Settings.
     */
    public readonly customerId!: pulumi.Output<string | undefined>;
    /**
     * The impersonated user's email with access to the Admin APIs can access the Admin SDK Directory API.
     * `impersonated_user_email` is required for all services except group and user management.
     */
    public readonly impersonatedUserEmail!: pulumi.Output<string | undefined>;
    /**
     * The service account used to create the provided `access_token` if authenticating using the `access_token` method and
     * needing to impersonate a user. This service account will require the GCP role `Service Account Token Creator` if needing
     * to impersonate a user.
     */
    public readonly serviceAccount!: pulumi.Output<string | undefined>;

    /**
     * Create a Provider resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args?: ProviderArgs, opts?: pulumi.ResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        {
            resourceInputs["accessToken"] = args ? args.accessToken : undefined;
            resourceInputs["credentials"] = args ? args.credentials : undefined;
            resourceInputs["customerId"] = args ? args.customerId : undefined;
            resourceInputs["impersonatedUserEmail"] = args ? args.impersonatedUserEmail : undefined;
            resourceInputs["oauthScopes"] = pulumi.output(args ? args.oauthScopes : undefined).apply(JSON.stringify);
            resourceInputs["serviceAccount"] = args ? args.serviceAccount : undefined;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(Provider.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * The set of arguments for constructing a Provider resource.
 */
export interface ProviderArgs {
    /**
     * A temporary [OAuth 2.0 access token] obtained from the Google Authorization server, i.e. the `Authorization: Bearer`
     * token used to authenticate HTTP requests to Google Admin SDK APIs. This is an alternative to `credentials`, and ignores
     * the `oauth_scopes` field. If both are specified, `access_token` will be used over the `credentials` field.
     */
    accessToken?: pulumi.Input<string>;
    /**
     * Either the path to or the contents of a service account key file in JSON format you can manage key files using the Cloud
     * Console). If not provided, the application default credentials will be used.
     */
    credentials?: pulumi.Input<string>;
    /**
     * The customer id provided with your Google Workspace subscription. It is found in the admin console under Account
     * Settings.
     */
    customerId?: pulumi.Input<string>;
    /**
     * The impersonated user's email with access to the Admin APIs can access the Admin SDK Directory API.
     * `impersonated_user_email` is required for all services except group and user management.
     */
    impersonatedUserEmail?: pulumi.Input<string>;
    /**
     * The list of the scopes required for your application (for a list of possible scopes, see [Authorize
     * requests](https://developers.google.com/admin-sdk/directory/v1/guides/authorizing))
     */
    oauthScopes?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * The service account used to create the provided `access_token` if authenticating using the `access_token` method and
     * needing to impersonate a user. This service account will require the GCP role `Service Account Token Creator` if needing
     * to impersonate a user.
     */
    serviceAccount?: pulumi.Input<string>;
}
