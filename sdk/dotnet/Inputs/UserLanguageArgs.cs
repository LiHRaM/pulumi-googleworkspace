// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Googleworkspace.Inputs
{

    public sealed class UserLanguageArgs : global::Pulumi.ResourceArgs
    {
        [Input("customLanguage")]
        public Input<string>? CustomLanguage { get; set; }

        [Input("languageCode")]
        public Input<string>? LanguageCode { get; set; }

        [Input("preference")]
        public Input<string>? Preference { get; set; }

        public UserLanguageArgs()
        {
        }
        public static new UserLanguageArgs Empty => new UserLanguageArgs();
    }
}
