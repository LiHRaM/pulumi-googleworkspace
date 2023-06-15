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
    public sealed class GetUserImResult
    {
        public readonly string CustomProtocol;
        public readonly string CustomType;
        public readonly string Im;
        public readonly bool Primary;
        public readonly string Protocol;
        public readonly string Type;

        [OutputConstructor]
        private GetUserImResult(
            string customProtocol,

            string customType,

            string im,

            bool primary,

            string protocol,

            string type)
        {
            CustomProtocol = customProtocol;
            CustomType = customType;
            Im = im;
            Primary = primary;
            Protocol = protocol;
            Type = type;
        }
    }
}
