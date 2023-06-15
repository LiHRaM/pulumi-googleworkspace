// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import { input as inputs, output as outputs } from "./types";
import * as utilities from "./utilities";

export function getPrivileges(opts?: pulumi.InvokeOptions): Promise<GetPrivilegesResult> {
    if (!opts) {
        opts = {}
    }

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
    return pulumi.runtime.invoke("googleworkspace:index/getPrivileges:getPrivileges", {
    }, opts);
}

/**
 * A collection of values returned by getPrivileges.
 */
export interface GetPrivilegesResult {
    /**
     * ETag of the resource.
     */
    readonly etag: string;
    /**
     * The provider-assigned unique ID for this managed resource.
     */
    readonly id: string;
    /**
     * A list of Privilege resources. The API returns a tree-like structure with parent-child privileges, the provider flattens this list.
     */
    readonly items: outputs.GetPrivilegesItem[];
}