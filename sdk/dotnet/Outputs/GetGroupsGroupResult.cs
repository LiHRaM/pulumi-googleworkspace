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
    public sealed class GetGroupsGroupResult
    {
        /// <summary>
        /// Value is true if this group was created by an administrator rather than a user.
        /// </summary>
        public readonly bool AdminCreated;
        /// <summary>
        /// asps.list of group's email addresses.
        /// </summary>
        public readonly ImmutableArray<string> Aliases;
        /// <summary>
        /// An extended description to help users determine the purpose of a group.For example, you can include information about who should join the group,the types of messages to send to the group, links to FAQs about the group, or related groups.
        /// </summary>
        public readonly string Description;
        /// <summary>
        /// The number of users that are direct members of the group.If a group is a member (child) of this group (the parent),members of the child group are not counted in the directMembersCount property of the parent group.
        /// </summary>
        public readonly int DirectMembersCount;
        public readonly string Email;
        /// <summary>
        /// ETag of the resource.
        /// </summary>
        public readonly string Etag;
        /// <summary>
        /// The ID of this resource.
        /// </summary>
        public readonly string Id;
        /// <summary>
        /// The group's display name.
        /// </summary>
        public readonly string Name;
        /// <summary>
        /// asps.list of the group's non-editable alias email addresses that are outside of the account's primary domain or subdomains. These are functioning email addresses used by the group.
        /// </summary>
        public readonly ImmutableArray<string> NonEditableAliases;

        [OutputConstructor]
        private GetGroupsGroupResult(
            bool adminCreated,

            ImmutableArray<string> aliases,

            string description,

            int directMembersCount,

            string email,

            string etag,

            string id,

            string name,

            ImmutableArray<string> nonEditableAliases)
        {
            AdminCreated = adminCreated;
            Aliases = aliases;
            Description = description;
            DirectMembersCount = directMembersCount;
            Email = email;
            Etag = etag;
            Id = id;
            Name = name;
            NonEditableAliases = nonEditableAliases;
        }
    }
}