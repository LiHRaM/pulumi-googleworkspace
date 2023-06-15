// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Googleworkspace.Outputs
{

    [OutputType]
    public sealed class GetSchemaFieldResult
    {
        /// <summary>
        /// Display name for the schema.
        /// </summary>
        public readonly string DisplayName;
        /// <summary>
        /// ETag of the resource.
        /// </summary>
        public readonly string Etag;
        public readonly string FieldId;
        public readonly string FieldName;
        public readonly string FieldType;
        public readonly bool Indexed;
        public readonly bool MultiValued;
        public readonly ImmutableArray<Outputs.GetSchemaFieldNumericIndexingSpecResult> NumericIndexingSpecs;
        public readonly string ReadAccessType;

        [OutputConstructor]
        private GetSchemaFieldResult(
            string displayName,

            string etag,

            string fieldId,

            string fieldName,

            string fieldType,

            bool indexed,

            bool multiValued,

            ImmutableArray<Outputs.GetSchemaFieldNumericIndexingSpecResult> numericIndexingSpecs,

            string readAccessType)
        {
            DisplayName = displayName;
            Etag = etag;
            FieldId = fieldId;
            FieldName = fieldName;
            FieldType = fieldType;
            Indexed = indexed;
            MultiValued = multiValued;
            NumericIndexingSpecs = numericIndexingSpecs;
            ReadAccessType = readAccessType;
        }
    }
}
