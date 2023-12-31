// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Googleworkspace.Inputs
{

    public sealed class UserSshPublicKeyGetArgs : global::Pulumi.ResourceArgs
    {
        [Input("expirationTimeUsec")]
        public Input<string>? ExpirationTimeUsec { get; set; }

        [Input("fingerprint")]
        public Input<string>? Fingerprint { get; set; }

        [Input("key", required: true)]
        public Input<string> Key { get; set; } = null!;

        public UserSshPublicKeyGetArgs()
        {
        }
        public static new UserSshPublicKeyGetArgs Empty => new UserSshPublicKeyGetArgs();
    }
}
