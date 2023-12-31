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
    public sealed class GetUserLocationResult
    {
        public readonly string Area;
        public readonly string BuildingId;
        public readonly string CustomType;
        public readonly string DeskCode;
        public readonly string FloorName;
        public readonly string FloorSection;
        public readonly string Type;

        [OutputConstructor]
        private GetUserLocationResult(
            string area,

            string buildingId,

            string customType,

            string deskCode,

            string floorName,

            string floorSection,

            string type)
        {
            Area = area;
            BuildingId = buildingId;
            CustomType = customType;
            DeskCode = deskCode;
            FloorName = floorName;
            FloorSection = floorSection;
            Type = type;
        }
    }
}
