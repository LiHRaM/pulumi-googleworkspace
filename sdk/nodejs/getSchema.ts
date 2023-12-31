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
 * const birthday = googleworkspace.getSchema({
 *     schemaName: "birthday",
 * });
 * export const schemaDisplayName = birthday.then(birthday => birthday.displayName);
 * ```
 */
export function getSchema(args?: GetSchemaArgs, opts?: pulumi.InvokeOptions): Promise<GetSchemaResult> {
    args = args || {};
    if (!opts) {
        opts = {}
    }

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
    return pulumi.runtime.invoke("googleworkspace:index/getSchema:getSchema", {
        "schemaId": args.schemaId,
        "schemaName": args.schemaName,
    }, opts);
}

/**
 * A collection of arguments for invoking getSchema.
 */
export interface GetSchemaArgs {
    /**
     * The unique identifier of the schema.
     */
    schemaId?: string;
    /**
     * The schema's name.
     */
    schemaName?: string;
}

/**
 * A collection of values returned by getSchema.
 */
export interface GetSchemaResult {
    /**
     * Display name for the schema.
     */
    readonly displayName: string;
    /**
     * ETag of the resource.
     */
    readonly etag: string;
    /**
     * A list of fields in the schema.
     */
    readonly fields: outputs.GetSchemaField[];
    /**
     * The ID of this resource.
     */
    readonly id: string;
    /**
     * The unique identifier of the schema.
     */
    readonly schemaId: string;
    /**
     * The schema's name.
     */
    readonly schemaName: string;
}

export function getSchemaOutput(args?: GetSchemaOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetSchemaResult> {
    return pulumi.output(args).apply(a => getSchema(a, opts))
}

/**
 * A collection of arguments for invoking getSchema.
 */
export interface GetSchemaOutputArgs {
    /**
     * The unique identifier of the schema.
     */
    schemaId?: pulumi.Input<string>;
    /**
     * The schema's name.
     */
    schemaName?: pulumi.Input<string>;
}
