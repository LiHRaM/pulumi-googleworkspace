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
    public sealed class GetChromePolicySchemaDefinitionResult
    {
        public readonly ImmutableArray<Outputs.GetChromePolicySchemaDefinitionEnumTypeResult> EnumTypes;
        public readonly string MessageType;
        public readonly string Name;
        public readonly string Package;
        public readonly string Syntax;

        [OutputConstructor]
        private GetChromePolicySchemaDefinitionResult(
            ImmutableArray<Outputs.GetChromePolicySchemaDefinitionEnumTypeResult> enumTypes,

            string messageType,

            string name,

            string package,

            string syntax)
        {
            EnumTypes = enumTypes;
            MessageType = messageType;
            Name = name;
            Package = package;
            Syntax = syntax;
        }
    }
}
