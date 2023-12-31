// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Googleworkspace.Inputs
{

    public sealed class UserAddressArgs : global::Pulumi.ResourceArgs
    {
        [Input("country")]
        public Input<string>? Country { get; set; }

        [Input("countryCode")]
        public Input<string>? CountryCode { get; set; }

        [Input("customType")]
        public Input<string>? CustomType { get; set; }

        [Input("extendedAddress")]
        public Input<string>? ExtendedAddress { get; set; }

        [Input("formatted")]
        public Input<string>? Formatted { get; set; }

        [Input("locality")]
        public Input<string>? Locality { get; set; }

        [Input("poBox")]
        public Input<string>? PoBox { get; set; }

        [Input("postalCode")]
        public Input<string>? PostalCode { get; set; }

        [Input("primary")]
        public Input<bool>? Primary { get; set; }

        [Input("region")]
        public Input<string>? Region { get; set; }

        [Input("sourceIsStructured")]
        public Input<bool>? SourceIsStructured { get; set; }

        [Input("streetAddress")]
        public Input<string>? StreetAddress { get; set; }

        [Input("type", required: true)]
        public Input<string> Type { get; set; } = null!;

        public UserAddressArgs()
        {
        }
        public static new UserAddressArgs Empty => new UserAddressArgs();
    }
}
