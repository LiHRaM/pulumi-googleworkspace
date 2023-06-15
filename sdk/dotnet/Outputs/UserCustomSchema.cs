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
    public sealed class UserCustomSchema
    {
        public readonly string SchemaName;
        public readonly ImmutableDictionary<string, string> SchemaValues;

        [OutputConstructor]
        private UserCustomSchema(
            string schemaName,

            ImmutableDictionary<string, string> schemaValues)
        {
            SchemaName = schemaName;
            SchemaValues = schemaValues;
        }
    }
}
