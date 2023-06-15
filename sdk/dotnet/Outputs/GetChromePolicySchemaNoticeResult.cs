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
    public sealed class GetChromePolicySchemaNoticeResult
    {
        public readonly bool AcknowledgementRequired;
        public readonly string Field;
        public readonly string NoticeMessage;
        public readonly string NoticeValue;

        [OutputConstructor]
        private GetChromePolicySchemaNoticeResult(
            bool acknowledgementRequired,

            string field,

            string noticeMessage,

            string noticeValue)
        {
            AcknowledgementRequired = acknowledgementRequired;
            Field = field;
            NoticeMessage = noticeMessage;
            NoticeValue = noticeValue;
        }
    }
}
