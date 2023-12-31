// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

/**
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as googleworkspace from "@pulumi/googleworkspace";
 *
 * const example = googleworkspace.getDomain({
 *     domainName: "example.com",
 * });
 * export const domainVerified = example.then(example => example.verified);
 * ```
 */
export function getDomain(args: GetDomainArgs, opts?: pulumi.InvokeOptions): Promise<GetDomainResult> {
    if (!opts) {
        opts = {}
    }

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
    return pulumi.runtime.invoke("googleworkspace:index/getDomain:getDomain", {
        "domainName": args.domainName,
    }, opts);
}

/**
 * A collection of arguments for invoking getDomain.
 */
export interface GetDomainArgs {
    /**
     * The domain name of the customer.
     */
    domainName: string;
}

/**
 * A collection of values returned by getDomain.
 */
export interface GetDomainResult {
    /**
     * Creation time of the domain. Expressed in Unix time format.
     */
    readonly creationTime: number;
    /**
     * asps.list of domain alias objects.
     */
    readonly domainAliases: string[];
    /**
     * The domain name of the customer.
     */
    readonly domainName: string;
    /**
     * ETag of the resource.
     */
    readonly etag: string;
    /**
     * The ID of this resource.
     */
    readonly id: string;
    /**
     * Indicates if the domain is a primary domain.
     */
    readonly isPrimary: boolean;
    /**
     * Indicates the verification state of a domain.
     */
    readonly verified: boolean;
}

export function getDomainOutput(args: GetDomainOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetDomainResult> {
    return pulumi.output(args).apply(a => getDomain(a, opts))
}

/**
 * A collection of arguments for invoking getDomain.
 */
export interface GetDomainOutputArgs {
    /**
     * The domain name of the customer.
     */
    domainName: pulumi.Input<string>;
}
