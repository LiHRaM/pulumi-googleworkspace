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
    public sealed class GetUsersUserLanguageResult
    {
        public readonly string CustomLanguage;
        public readonly string LanguageCode;
        public readonly string Preference;

        [OutputConstructor]
        private GetUsersUserLanguageResult(
            string customLanguage,

            string languageCode,

            string preference)
        {
            CustomLanguage = customLanguage;
            LanguageCode = languageCode;
            Preference = preference;
        }
    }
}
