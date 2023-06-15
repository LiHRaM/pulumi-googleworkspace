// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Googleworkspace.Inputs
{

    public sealed class SchemaFieldArgs : global::Pulumi.ResourceArgs
    {
        [Input("displayName")]
        public Input<string>? DisplayName { get; set; }

        [Input("etag")]
        public Input<string>? Etag { get; set; }

        [Input("fieldId")]
        public Input<string>? FieldId { get; set; }

        [Input("fieldName", required: true)]
        public Input<string> FieldName { get; set; } = null!;

        [Input("fieldType", required: true)]
        public Input<string> FieldType { get; set; } = null!;

        [Input("indexed")]
        public Input<bool>? Indexed { get; set; }

        [Input("multiValued")]
        public Input<bool>? MultiValued { get; set; }

        [Input("numericIndexingSpec")]
        public Input<Inputs.SchemaFieldNumericIndexingSpecArgs>? NumericIndexingSpec { get; set; }

        [Input("readAccessType")]
        public Input<string>? ReadAccessType { get; set; }

        public SchemaFieldArgs()
        {
        }
        public static new SchemaFieldArgs Empty => new SchemaFieldArgs();
    }
}
