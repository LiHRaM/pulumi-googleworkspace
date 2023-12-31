// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Googleworkspace.Inputs
{

    public sealed class UserLocationGetArgs : global::Pulumi.ResourceArgs
    {
        [Input("area")]
        public Input<string>? Area { get; set; }

        [Input("buildingId")]
        public Input<string>? BuildingId { get; set; }

        [Input("customType")]
        public Input<string>? CustomType { get; set; }

        [Input("deskCode")]
        public Input<string>? DeskCode { get; set; }

        [Input("floorName")]
        public Input<string>? FloorName { get; set; }

        [Input("floorSection")]
        public Input<string>? FloorSection { get; set; }

        [Input("type", required: true)]
        public Input<string> Type { get; set; } = null!;

        public UserLocationGetArgs()
        {
        }
        public static new UserLocationGetArgs Empty => new UserLocationGetArgs();
    }
}
