// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import { input as inputs, output as outputs } from "./types";
import * as utilities from "./utilities";

/**
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as googleworkspace from "@pulumi/googleworkspace";
 *
 * const dwight = googleworkspace.getUser({
 *     primaryEmail: "dwight.schrute@example.com",
 * });
 * export const isUserAdmin = dwight.then(dwight => dwight.isAdmin);
 * ```
 */
export function getUser(args?: GetUserArgs, opts?: pulumi.InvokeOptions): Promise<GetUserResult> {
    args = args || {};
    if (!opts) {
        opts = {}
    }

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
    return pulumi.runtime.invoke("googleworkspace:index/getUser:getUser", {
        "id": args.id,
        "primaryEmail": args.primaryEmail,
    }, opts);
}

/**
 * A collection of arguments for invoking getUser.
 */
export interface GetUserArgs {
    /**
     * The unique ID for the user.
     */
    id?: string;
    /**
     * The user's primary email address. The primaryEmail must be unique and cannot be an alias of another user.
     */
    primaryEmail?: string;
}

/**
 * A collection of values returned by getUser.
 */
export interface GetUserResult {
    /**
     * A list of the user's addresses. The maximum allowed data size is 10Kb.
     */
    readonly addresses: outputs.GetUserAddress[];
    /**
     * This property is true if the user has completed an initial login and accepted the Terms of Service agreement.
     */
    readonly agreedToTerms: boolean;
    /**
     * asps.list of the user's alias email addresses.
     */
    readonly aliases: string[];
    /**
     * Indicates if user is archived.
     */
    readonly archived: boolean;
    /**
     * Indicates if the user is forced to change their password at next login. This setting doesn't apply when the user signs in via a third-party identity provider.
     */
    readonly changePasswordAtNextLogin: boolean;
    /**
     * The time the user's account was created. The value is in ISO 8601 date and time format. The time is the complete date plus hours, minutes, and seconds in the form YYYY-MM-DDThh:mm:ssTZD. For example, 2010-04-05T17:30:04+01:00.
     */
    readonly creationTime: string;
    /**
     * Custom fields of the user.
     */
    readonly customSchemas: outputs.GetUserCustomSchema[];
    /**
     * The customer ID to retrieve all account users. You can use the alias myCustomer to represent your account's customerId. As a reseller administrator, you can use the resold customer account's customerId. To get a customerId, use the account's primary domain in the domain parameter of a users.list request.
     */
    readonly customerId: string;
    /**
     * The time the user's account was deleted. The value is in ISO 8601 date and time format The time is the complete date plus hours, minutes, and seconds in the form YYYY-MM-DDThh:mm:ssTZD. For example 2010-04-05T17:30:04+01:00.
     */
    readonly deletionTime: string;
    /**
     * A list of the user's email addresses. The maximum allowed data size is 10Kb.
     */
    readonly emails: outputs.GetUserEmail[];
    /**
     * ETag of the resource.
     */
    readonly etag: string;
    /**
     * A list of external IDs for the user, such as an employee or network ID. The maximum allowed data size is 2Kb.
     */
    readonly externalIds: outputs.GetUserExternalId[];
    /**
     * Stores the hash format of the password property. We recommend sending the password property value as a base 16 bit hexadecimal-encoded hash value. Set the hashFunction values as either the SHA-1, MD5, or crypt hash format.
     */
    readonly hashFunction: string;
    /**
     * The unique ID for the user.
     */
    readonly id: string;
    /**
     * The user's Instant Messenger (IM) accounts. A user account can have multiple ims properties. But, only one of these ims properties can be the primary IM contact. The maximum allowed data size is 2Kb.
     */
    readonly ims: outputs.GetUserIm[];
    /**
     * Indicates if the user's profile is visible in the Google Workspace global address list when the contact sharing feature is enabled for the domain.
     */
    readonly includeInGlobalAddressList: boolean;
    /**
     * If true, the user's IP address is added to the allow list.
     */
    readonly ipAllowlist: boolean;
    /**
     * Indicates a user with super admininistrator privileges.
     */
    readonly isAdmin: boolean;
    /**
     * Indicates if the user is a delegated administrator.
     */
    readonly isDelegatedAdmin: boolean;
    /**
     * Is 2-step verification enforced.
     */
    readonly isEnforcedIn2StepVerification: boolean;
    /**
     * Is enrolled in 2-step verification.
     */
    readonly isEnrolledIn2StepVerification: boolean;
    /**
     * Indicates if the user's Google mailbox is created. This property is only applicable if the user has been assigned a Gmail license.
     */
    readonly isMailboxSetup: boolean;
    /**
     * A list of the user's keywords. The maximum allowed data size is 1Kb.
     */
    readonly keywords: outputs.GetUserKeyword[];
    /**
     * A list of the user's languages. The maximum allowed data size is 1Kb.
     */
    readonly languages: outputs.GetUserLanguage[];
    /**
     * The last time the user logged into the user's account. The value is in ISO 8601 date and time format. The time is the complete date plus hours, minutes, and seconds in the form YYYY-MM-DDThh:mm:ssTZD. For example, 2010-04-05T17:30:04+01:00.
     */
    readonly lastLoginTime: string;
    /**
     * A list of the user's locations. The maximum allowed data size is 10Kb.
     */
    readonly locations: outputs.GetUserLocation[];
    /**
     * Holds the given and family names of the user, and the read-only fullName value. The maximum number of characters in the givenName and in the familyName values is 60. In addition, name values support unicode/UTF-8 characters, and can contain spaces, letters (a-z), numbers (0-9), dashes (-), forward slashes (/), and periods (.). Maximum allowed data size for this field is 1Kb.
     */
    readonly names: outputs.GetUserName[];
    /**
     * asps.list of the user's non-editable alias email addresses. These are typically outside the account's primary domain or sub-domain.
     */
    readonly nonEditableAliases: string[];
    /**
     * The full path of the parent organization associated with the user. If the parent organization is the top-level, it is represented as a forward slash (/).
     */
    readonly orgUnitPath: string;
    /**
     * A list of organizations the user belongs to. The maximum allowed data size is 10Kb.
     */
    readonly organizations: outputs.GetUserOrganization[];
    /**
     * Stores the password for the user account. A password can contain any combination of ASCII characters. A minimum of 8 characters is required. The maximum length is 100 characters. As the API does not return the value of password, this field is write-only, and the value stored in the state will be what is provided in the configuration. The field is required on create and will be empty on import.
     */
    readonly password: string;
    /**
     * A list of the user's phone numbers. The maximum allowed data size is 1Kb.
     */
    readonly phones: outputs.GetUserPhone[];
    /**
     * A list of POSIX account information for the user.
     */
    readonly posixAccounts: outputs.GetUserPosixAccount[];
    /**
     * The user's primary email address. The primaryEmail must be unique and cannot be an alias of another user.
     */
    readonly primaryEmail: string;
    /**
     * Recovery email of the user.
     */
    readonly recoveryEmail: string;
    /**
     * Recovery phone of the user. The phone number must be in the E.164 format, starting with the plus sign (+). Example: +16506661212.
     */
    readonly recoveryPhone: string;
    /**
     * A list of the user's relationships to other users. The maximum allowed data size for this field is 2Kb.
     */
    readonly relations: outputs.GetUserRelation[];
    /**
     * A list of SSH public keys. The maximum allowed data size is 10Kb.
     */
    readonly sshPublicKeys: outputs.GetUserSshPublicKey[];
    /**
     * Indicates if user is suspended.
     */
    readonly suspended: boolean;
    /**
     * Has the reason a user account is suspended either by the administrator or by Google at the time of suspension. The property is returned only if the suspended property is true.
     */
    readonly suspensionReason: string;
    /**
     * ETag of the user's photo
     */
    readonly thumbnailPhotoEtag: string;
    /**
     * Photo Url of the user.
     */
    readonly thumbnailPhotoUrl: string;
    /**
     * A list of the user's websites. The maximum allowed data size is 2Kb.
     */
    readonly websites: outputs.GetUserWebsite[];
}

export function getUserOutput(args?: GetUserOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetUserResult> {
    return pulumi.output(args).apply(a => getUser(a, opts))
}

/**
 * A collection of arguments for invoking getUser.
 */
export interface GetUserOutputArgs {
    /**
     * The unique ID for the user.
     */
    id?: pulumi.Input<string>;
    /**
     * The user's primary email address. The primaryEmail must be unique and cannot be an alias of another user.
     */
    primaryEmail?: pulumi.Input<string>;
}
