// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import { input as inputs, output as outputs } from "./types";
import * as utilities from "./utilities";

/**
 * Schema resource manages Google Workspace Schemas. Schema resides under the `https://www.googleapis.com/auth/admin.directory.userschema` client scope.
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as googleworkspace from "@pulumi/googleworkspace";
 *
 * const birthday = new googleworkspace.Schema("birthday", {
 *     fields: [{
 *         fieldName: "birthday",
 *         fieldType: "DATE",
 *     }],
 *     schemaName: "birthday",
 * });
 * ```
 *
 * ## Import
 *
 * ```sh
 *  $ pulumi import googleworkspace:index/schema:Schema birthday Ab0C_DEFGhIJKLmNopQ1Rs==
 * ```
 */
export class Schema extends pulumi.CustomResource {
    /**
     * Get an existing Schema resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: SchemaState, opts?: pulumi.CustomResourceOptions): Schema {
        return new Schema(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'googleworkspace:index/schema:Schema';

    /**
     * Returns true if the given object is an instance of Schema.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Schema {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Schema.__pulumiType;
    }

    /**
     * Display name for the schema.
     */
    public readonly displayName!: pulumi.Output<string>;
    /**
     * ETag of the resource.
     */
    public /*out*/ readonly etag!: pulumi.Output<string>;
    /**
     * A list of fields in the schema.
     */
    public readonly fields!: pulumi.Output<outputs.SchemaField[]>;
    /**
     * The unique identifier of the schema.
     */
    public /*out*/ readonly schemaId!: pulumi.Output<string>;
    /**
     * The schema's name.
     */
    public readonly schemaName!: pulumi.Output<string>;

    /**
     * Create a Schema resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: SchemaArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: SchemaArgs | SchemaState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as SchemaState | undefined;
            resourceInputs["displayName"] = state ? state.displayName : undefined;
            resourceInputs["etag"] = state ? state.etag : undefined;
            resourceInputs["fields"] = state ? state.fields : undefined;
            resourceInputs["schemaId"] = state ? state.schemaId : undefined;
            resourceInputs["schemaName"] = state ? state.schemaName : undefined;
        } else {
            const args = argsOrState as SchemaArgs | undefined;
            if ((!args || args.fields === undefined) && !opts.urn) {
                throw new Error("Missing required property 'fields'");
            }
            if ((!args || args.schemaName === undefined) && !opts.urn) {
                throw new Error("Missing required property 'schemaName'");
            }
            resourceInputs["displayName"] = args ? args.displayName : undefined;
            resourceInputs["fields"] = args ? args.fields : undefined;
            resourceInputs["schemaName"] = args ? args.schemaName : undefined;
            resourceInputs["etag"] = undefined /*out*/;
            resourceInputs["schemaId"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(Schema.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering Schema resources.
 */
export interface SchemaState {
    /**
     * Display name for the schema.
     */
    displayName?: pulumi.Input<string>;
    /**
     * ETag of the resource.
     */
    etag?: pulumi.Input<string>;
    /**
     * A list of fields in the schema.
     */
    fields?: pulumi.Input<pulumi.Input<inputs.SchemaField>[]>;
    /**
     * The unique identifier of the schema.
     */
    schemaId?: pulumi.Input<string>;
    /**
     * The schema's name.
     */
    schemaName?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a Schema resource.
 */
export interface SchemaArgs {
    /**
     * Display name for the schema.
     */
    displayName?: pulumi.Input<string>;
    /**
     * A list of fields in the schema.
     */
    fields: pulumi.Input<pulumi.Input<inputs.SchemaField>[]>;
    /**
     * The schema's name.
     */
    schemaName: pulumi.Input<string>;
}
