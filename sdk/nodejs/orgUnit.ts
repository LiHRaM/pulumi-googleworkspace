// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

/**
 * OrgUnit resource manages Google Workspace OrgUnits. Org Unit resides under the `https://www.googleapis.com/auth/admin.directory.orgunit` client scope.
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as googleworkspace from "@pulumi/googleworkspace";
 *
 * const org = new googleworkspace.OrgUnit("org", {
 *     description: "paper company",
 *     parentOrgUnitPath: "/",
 * });
 * ```
 *
 * ## Import
 *
 * ```sh
 *  $ pulumi import googleworkspace:index/orgUnit:OrgUnit org "id:01ab2c3d4efg56h"
 * ```
 */
export class OrgUnit extends pulumi.CustomResource {
    /**
     * Get an existing OrgUnit resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: OrgUnitState, opts?: pulumi.CustomResourceOptions): OrgUnit {
        return new OrgUnit(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'googleworkspace:index/orgUnit:OrgUnit';

    /**
     * Returns true if the given object is an instance of OrgUnit.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is OrgUnit {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === OrgUnit.__pulumiType;
    }

    /**
     * Defaults to `false`. Determines if a sub-organizational unit can inherit the settings of the parent organization. False means a sub-organizational unit inherits the settings of the nearest parent organizational unit. For more information on inheritance and users in an organization structure, see the [administration help center](https://support.google.com/a/answer/4352075).
     */
    public readonly blockInheritance!: pulumi.Output<boolean | undefined>;
    /**
     * Description of the organizational unit.
     */
    public readonly description!: pulumi.Output<string | undefined>;
    /**
     * ETag of the resource.
     */
    public /*out*/ readonly etag!: pulumi.Output<string>;
    /**
     * The organizational unit's path name. For example, an organizational unit's name within the /corp/support/sales*support parent path is sales*support.
     */
    public readonly name!: pulumi.Output<string>;
    /**
     * The unique ID of the organizational unit.
     */
    public /*out*/ readonly orgUnitId!: pulumi.Output<string>;
    /**
     * The full path to the organizational unit. The orgUnitPath is a derived property. When listed, it is derived from parentOrgunitPath and organizational unit's name. For example, for an organizational unit named 'apps' under parent organization '/engineering', the orgUnitPath is '/engineering/apps'. In order to edit an orgUnitPath, either update the name of the organization or the parentOrgunitPath. A user's organizational unit determines which Google Workspace services the user has access to. If the user is moved to a new organization, the user's access changes. For more information about organization structures, see the [administration help center](https://support.google.com/a/answer/4352075). For more information about moving a user to a different organization, see [chromeosdevices.update a user](https://developers.google.com/admin-sdk/directory/v1/guides/manage-users#update_user).
     */
    public /*out*/ readonly orgUnitPath!: pulumi.Output<string>;
    /**
     * The unique ID of the parent organizational unit.
     */
    public readonly parentOrgUnitId!: pulumi.Output<string>;
    /**
     * The organizational unit's parent path. For example, /corp/sales is the parent path for /corp/sales/sales_support organizational unit.
     */
    public readonly parentOrgUnitPath!: pulumi.Output<string>;

    /**
     * Create a OrgUnit resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args?: OrgUnitArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: OrgUnitArgs | OrgUnitState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as OrgUnitState | undefined;
            resourceInputs["blockInheritance"] = state ? state.blockInheritance : undefined;
            resourceInputs["description"] = state ? state.description : undefined;
            resourceInputs["etag"] = state ? state.etag : undefined;
            resourceInputs["name"] = state ? state.name : undefined;
            resourceInputs["orgUnitId"] = state ? state.orgUnitId : undefined;
            resourceInputs["orgUnitPath"] = state ? state.orgUnitPath : undefined;
            resourceInputs["parentOrgUnitId"] = state ? state.parentOrgUnitId : undefined;
            resourceInputs["parentOrgUnitPath"] = state ? state.parentOrgUnitPath : undefined;
        } else {
            const args = argsOrState as OrgUnitArgs | undefined;
            resourceInputs["blockInheritance"] = args ? args.blockInheritance : undefined;
            resourceInputs["description"] = args ? args.description : undefined;
            resourceInputs["name"] = args ? args.name : undefined;
            resourceInputs["parentOrgUnitId"] = args ? args.parentOrgUnitId : undefined;
            resourceInputs["parentOrgUnitPath"] = args ? args.parentOrgUnitPath : undefined;
            resourceInputs["etag"] = undefined /*out*/;
            resourceInputs["orgUnitId"] = undefined /*out*/;
            resourceInputs["orgUnitPath"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(OrgUnit.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering OrgUnit resources.
 */
export interface OrgUnitState {
    /**
     * Defaults to `false`. Determines if a sub-organizational unit can inherit the settings of the parent organization. False means a sub-organizational unit inherits the settings of the nearest parent organizational unit. For more information on inheritance and users in an organization structure, see the [administration help center](https://support.google.com/a/answer/4352075).
     */
    blockInheritance?: pulumi.Input<boolean>;
    /**
     * Description of the organizational unit.
     */
    description?: pulumi.Input<string>;
    /**
     * ETag of the resource.
     */
    etag?: pulumi.Input<string>;
    /**
     * The organizational unit's path name. For example, an organizational unit's name within the /corp/support/sales*support parent path is sales*support.
     */
    name?: pulumi.Input<string>;
    /**
     * The unique ID of the organizational unit.
     */
    orgUnitId?: pulumi.Input<string>;
    /**
     * The full path to the organizational unit. The orgUnitPath is a derived property. When listed, it is derived from parentOrgunitPath and organizational unit's name. For example, for an organizational unit named 'apps' under parent organization '/engineering', the orgUnitPath is '/engineering/apps'. In order to edit an orgUnitPath, either update the name of the organization or the parentOrgunitPath. A user's organizational unit determines which Google Workspace services the user has access to. If the user is moved to a new organization, the user's access changes. For more information about organization structures, see the [administration help center](https://support.google.com/a/answer/4352075). For more information about moving a user to a different organization, see [chromeosdevices.update a user](https://developers.google.com/admin-sdk/directory/v1/guides/manage-users#update_user).
     */
    orgUnitPath?: pulumi.Input<string>;
    /**
     * The unique ID of the parent organizational unit.
     */
    parentOrgUnitId?: pulumi.Input<string>;
    /**
     * The organizational unit's parent path. For example, /corp/sales is the parent path for /corp/sales/sales_support organizational unit.
     */
    parentOrgUnitPath?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a OrgUnit resource.
 */
export interface OrgUnitArgs {
    /**
     * Defaults to `false`. Determines if a sub-organizational unit can inherit the settings of the parent organization. False means a sub-organizational unit inherits the settings of the nearest parent organizational unit. For more information on inheritance and users in an organization structure, see the [administration help center](https://support.google.com/a/answer/4352075).
     */
    blockInheritance?: pulumi.Input<boolean>;
    /**
     * Description of the organizational unit.
     */
    description?: pulumi.Input<string>;
    /**
     * The organizational unit's path name. For example, an organizational unit's name within the /corp/support/sales*support parent path is sales*support.
     */
    name?: pulumi.Input<string>;
    /**
     * The unique ID of the parent organizational unit.
     */
    parentOrgUnitId?: pulumi.Input<string>;
    /**
     * The organizational unit's parent path. For example, /corp/sales is the parent path for /corp/sales/sales_support organizational unit.
     */
    parentOrgUnitPath?: pulumi.Input<string>;
}
