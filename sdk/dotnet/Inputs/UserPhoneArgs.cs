// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Googleworkspace.Inputs
{

    public sealed class UserPhoneArgs : global::Pulumi.ResourceArgs
    {
        [Input("customType")]
        public Input<string>? CustomType { get; set; }

        [Input("primary")]
        public Input<bool>? Primary { get; set; }

        [Input("type", required: true)]
        public Input<string> Type { get; set; } = null!;

        [Input("value", required: true)]
        public Input<string> Value { get; set; } = null!;

        public UserPhoneArgs()
        {
        }
        public static new UserPhoneArgs Empty => new UserPhoneArgs();
    }
}
