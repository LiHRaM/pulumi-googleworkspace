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
    public sealed class GetUserPosixAccountResult
    {
        public readonly string AccountId;
        public readonly string Gecos;
        public readonly string Gid;
        public readonly string HomeDirectory;
        public readonly string OperatingSystemType;
        public readonly bool Primary;
        public readonly string Shell;
        public readonly string SystemId;
        public readonly string Uid;
        public readonly string Username;

        [OutputConstructor]
        private GetUserPosixAccountResult(
            string accountId,

            string gecos,

            string gid,

            string homeDirectory,

            string operatingSystemType,

            bool primary,

            string shell,

            string systemId,

            string uid,

            string username)
        {
            AccountId = accountId;
            Gecos = gecos;
            Gid = gid;
            HomeDirectory = homeDirectory;
            OperatingSystemType = operatingSystemType;
            Primary = primary;
            Shell = shell;
            SystemId = systemId;
            Uid = uid;
            Username = username;
        }
    }
}
