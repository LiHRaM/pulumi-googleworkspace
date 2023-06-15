// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Googleworkspace.Inputs
{

    public sealed class UserCustomSchemaArgs : global::Pulumi.ResourceArgs
    {
        [Input("schemaName", required: true)]
        public Input<string> SchemaName { get; set; } = null!;

        [Input("schemaValues", required: true)]
        private InputMap<string>? _schemaValues;
        public InputMap<string> SchemaValues
        {
            get => _schemaValues ?? (_schemaValues = new InputMap<string>());
            set => _schemaValues = value;
        }

        public UserCustomSchemaArgs()
        {
        }
        public static new UserCustomSchemaArgs Empty => new UserCustomSchemaArgs();
    }
}
