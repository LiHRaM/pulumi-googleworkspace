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
    public sealed class UserWebsite
    {
        public readonly string? CustomType;
        public readonly bool? Primary;
        public readonly string Type;
        public readonly string Value;

        [OutputConstructor]
        private UserWebsite(
            string? customType,

            bool? primary,

            string type,

            string value)
        {
            CustomType = customType;
            Primary = primary;
            Type = type;
            Value = value;
        }
    }
}
