// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

/**
 * Group Member resource manages Google Workspace Groups Members. Group Member resides under the `https://www.googleapis.com/auth/admin.directory.group` client scope.
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as googleworkspace from "@pulumi/googleworkspace";
 *
 * const sales = new googleworkspace.Group("sales", {email: "sales@example.com"});
 * const michael = new googleworkspace.User("michael", {
 *     primaryEmail: "michael.scott@example.com",
 *     password: "34819d7beeabb9260a5c854bc85b3e44",
 *     hashFunction: "MD5",
 *     name: {
 *         familyName: "Scott",
 *         givenName: "Michael",
 *     },
 * });
 * const manager = new googleworkspace.GroupMember("manager", {
 *     groupId: sales.id,
 *     email: michael.primaryEmail,
 *     role: "MANAGER",
 * });
 * ```
 *
 * ## Import
 *
 * ```sh
 *  $ pulumi import googleworkspace:index/groupMember:GroupMember manager groups/01abcde23fg4h5i/members/123456789012345678901
 * ```
 */
export class GroupMember extends pulumi.CustomResource {
    /**
     * Get an existing GroupMember resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: GroupMemberState, opts?: pulumi.CustomResourceOptions): GroupMember {
        return new GroupMember(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'googleworkspace:index/groupMember:GroupMember';

    /**
     * Returns true if the given object is an instance of GroupMember.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is GroupMember {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === GroupMember.__pulumiType;
    }

    /**
     * Defines mail delivery preferences of member. Acceptable values are: - `ALL_MAIL`: All messages, delivered as soon as
     * they arrive. - `DAILY`: No more than one message a day. - `DIGEST`: Up to 25 messages bundled into a single message. -
     * `DISABLED`: Remove subscription. - `NONE`: No messages.
     */
    public readonly deliverySettings!: pulumi.Output<string | undefined>;
    /**
     * The member's email address. A member can be a user or another group. This property is required when adding a member to a
     * group. The email must be unique and cannot be an alias of another group. If the email address is changed, the API
     * automatically reflects the email address changes.
     */
    public readonly email!: pulumi.Output<string>;
    /**
     * ETag of the resource.
     */
    public /*out*/ readonly etag!: pulumi.Output<string>;
    /**
     * Identifies the group in the API request. The value can be the group's email address, group alias, or the unique group
     * ID.
     */
    public readonly groupId!: pulumi.Output<string>;
    /**
     * The unique ID of the group member. A member id can be used as a member request URI's memberKey.
     */
    public /*out*/ readonly memberId!: pulumi.Output<string>;
    /**
     * The member's role in a group. The API returns an error for cycles in group memberships. For example, if group1 is a
     * member of group2, group2 cannot be a member of group1. Acceptable values are: - `MANAGER`: This role is only available
     * if the Google Groups for Business is enabled using the Admin Console. A `MANAGER` role can do everything done by an
     * `OWNER` role except make a member an `OWNER` or delete the group. A group can have multiple `MANAGER` members. -
     * `MEMBER`: This role can subscribe to a group, view discussion archives, and view the group's membership list. - `OWNER`:
     * This role can send messages to the group, add or remove members, change member roles, change group's settings, and
     * delete the group. An OWNER must be a member of the group. A group can have more than one OWNER.
     */
    public readonly role!: pulumi.Output<string | undefined>;
    /**
     * Status of member.
     */
    public /*out*/ readonly status!: pulumi.Output<string>;
    /**
     * The type of group member. Acceptable values are: - `CUSTOMER`: The member represents all users in a domain. An email
     * address is not returned and the ID returned is the customer ID. - `GROUP`: The member is another group. - `USER`: The
     * member is a user.
     */
    public readonly type!: pulumi.Output<string | undefined>;

    /**
     * Create a GroupMember resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: GroupMemberArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: GroupMemberArgs | GroupMemberState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as GroupMemberState | undefined;
            resourceInputs["deliverySettings"] = state ? state.deliverySettings : undefined;
            resourceInputs["email"] = state ? state.email : undefined;
            resourceInputs["etag"] = state ? state.etag : undefined;
            resourceInputs["groupId"] = state ? state.groupId : undefined;
            resourceInputs["memberId"] = state ? state.memberId : undefined;
            resourceInputs["role"] = state ? state.role : undefined;
            resourceInputs["status"] = state ? state.status : undefined;
            resourceInputs["type"] = state ? state.type : undefined;
        } else {
            const args = argsOrState as GroupMemberArgs | undefined;
            if ((!args || args.email === undefined) && !opts.urn) {
                throw new Error("Missing required property 'email'");
            }
            if ((!args || args.groupId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'groupId'");
            }
            resourceInputs["deliverySettings"] = args ? args.deliverySettings : undefined;
            resourceInputs["email"] = args ? args.email : undefined;
            resourceInputs["groupId"] = args ? args.groupId : undefined;
            resourceInputs["role"] = args ? args.role : undefined;
            resourceInputs["type"] = args ? args.type : undefined;
            resourceInputs["etag"] = undefined /*out*/;
            resourceInputs["memberId"] = undefined /*out*/;
            resourceInputs["status"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(GroupMember.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering GroupMember resources.
 */
export interface GroupMemberState {
    /**
     * Defines mail delivery preferences of member. Acceptable values are: - `ALL_MAIL`: All messages, delivered as soon as
     * they arrive. - `DAILY`: No more than one message a day. - `DIGEST`: Up to 25 messages bundled into a single message. -
     * `DISABLED`: Remove subscription. - `NONE`: No messages.
     */
    deliverySettings?: pulumi.Input<string>;
    /**
     * The member's email address. A member can be a user or another group. This property is required when adding a member to a
     * group. The email must be unique and cannot be an alias of another group. If the email address is changed, the API
     * automatically reflects the email address changes.
     */
    email?: pulumi.Input<string>;
    /**
     * ETag of the resource.
     */
    etag?: pulumi.Input<string>;
    /**
     * Identifies the group in the API request. The value can be the group's email address, group alias, or the unique group
     * ID.
     */
    groupId?: pulumi.Input<string>;
    /**
     * The unique ID of the group member. A member id can be used as a member request URI's memberKey.
     */
    memberId?: pulumi.Input<string>;
    /**
     * The member's role in a group. The API returns an error for cycles in group memberships. For example, if group1 is a
     * member of group2, group2 cannot be a member of group1. Acceptable values are: - `MANAGER`: This role is only available
     * if the Google Groups for Business is enabled using the Admin Console. A `MANAGER` role can do everything done by an
     * `OWNER` role except make a member an `OWNER` or delete the group. A group can have multiple `MANAGER` members. -
     * `MEMBER`: This role can subscribe to a group, view discussion archives, and view the group's membership list. - `OWNER`:
     * This role can send messages to the group, add or remove members, change member roles, change group's settings, and
     * delete the group. An OWNER must be a member of the group. A group can have more than one OWNER.
     */
    role?: pulumi.Input<string>;
    /**
     * Status of member.
     */
    status?: pulumi.Input<string>;
    /**
     * The type of group member. Acceptable values are: - `CUSTOMER`: The member represents all users in a domain. An email
     * address is not returned and the ID returned is the customer ID. - `GROUP`: The member is another group. - `USER`: The
     * member is a user.
     */
    type?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a GroupMember resource.
 */
export interface GroupMemberArgs {
    /**
     * Defines mail delivery preferences of member. Acceptable values are: - `ALL_MAIL`: All messages, delivered as soon as
     * they arrive. - `DAILY`: No more than one message a day. - `DIGEST`: Up to 25 messages bundled into a single message. -
     * `DISABLED`: Remove subscription. - `NONE`: No messages.
     */
    deliverySettings?: pulumi.Input<string>;
    /**
     * The member's email address. A member can be a user or another group. This property is required when adding a member to a
     * group. The email must be unique and cannot be an alias of another group. If the email address is changed, the API
     * automatically reflects the email address changes.
     */
    email: pulumi.Input<string>;
    /**
     * Identifies the group in the API request. The value can be the group's email address, group alias, or the unique group
     * ID.
     */
    groupId: pulumi.Input<string>;
    /**
     * The member's role in a group. The API returns an error for cycles in group memberships. For example, if group1 is a
     * member of group2, group2 cannot be a member of group1. Acceptable values are: - `MANAGER`: This role is only available
     * if the Google Groups for Business is enabled using the Admin Console. A `MANAGER` role can do everything done by an
     * `OWNER` role except make a member an `OWNER` or delete the group. A group can have multiple `MANAGER` members. -
     * `MEMBER`: This role can subscribe to a group, view discussion archives, and view the group's membership list. - `OWNER`:
     * This role can send messages to the group, add or remove members, change member roles, change group's settings, and
     * delete the group. An OWNER must be a member of the group. A group can have more than one OWNER.
     */
    role?: pulumi.Input<string>;
    /**
     * The type of group member. Acceptable values are: - `CUSTOMER`: The member represents all users in a domain. An email
     * address is not returned and the ID returned is the customer ID. - `GROUP`: The member is another group. - `USER`: The
     * member is a user.
     */
    type?: pulumi.Input<string>;
}
