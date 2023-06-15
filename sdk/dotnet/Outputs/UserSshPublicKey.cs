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
    public sealed class UserSshPublicKey
    {
        public readonly string? ExpirationTimeUsec;
        public readonly string? Fingerprint;
        public readonly string Key;

        [OutputConstructor]
        private UserSshPublicKey(
            string? expirationTimeUsec,

            string? fingerprint,

            string key)
        {
            ExpirationTimeUsec = expirationTimeUsec;
            Fingerprint = fingerprint;
            Key = key;
        }
    }
}
