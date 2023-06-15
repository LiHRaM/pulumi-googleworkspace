// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Googleworkspace
{
    public static class GetSchema
    {
        /// <summary>
        /// {{% examples %}}
        /// ## Example Usage
        /// {{% example %}}
        /// 
        /// ```csharp
        /// using System.Collections.Generic;
        /// using Pulumi;
        /// using Googleworkspace = Pulumi.Googleworkspace;
        /// 
        /// return await Deployment.RunAsync(() =&gt; 
        /// {
        ///     var birthday = Googleworkspace.GetSchema.Invoke(new()
        ///     {
        ///         SchemaName = "birthday",
        ///     });
        /// 
        ///     return new Dictionary&lt;string, object?&gt;
        ///     {
        ///         ["schemaDisplayName"] = birthday.Apply(getSchemaResult =&gt; getSchemaResult.DisplayName),
        ///     };
        /// });
        /// ```
        /// {{% /example %}}
        /// {{% /examples %}}
        /// </summary>
        public static Task<GetSchemaResult> InvokeAsync(GetSchemaArgs? args = null, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetSchemaResult>("googleworkspace:index/getSchema:getSchema", args ?? new GetSchemaArgs(), options.WithDefaults());

        /// <summary>
        /// {{% examples %}}
        /// ## Example Usage
        /// {{% example %}}
        /// 
        /// ```csharp
        /// using System.Collections.Generic;
        /// using Pulumi;
        /// using Googleworkspace = Pulumi.Googleworkspace;
        /// 
        /// return await Deployment.RunAsync(() =&gt; 
        /// {
        ///     var birthday = Googleworkspace.GetSchema.Invoke(new()
        ///     {
        ///         SchemaName = "birthday",
        ///     });
        /// 
        ///     return new Dictionary&lt;string, object?&gt;
        ///     {
        ///         ["schemaDisplayName"] = birthday.Apply(getSchemaResult =&gt; getSchemaResult.DisplayName),
        ///     };
        /// });
        /// ```
        /// {{% /example %}}
        /// {{% /examples %}}
        /// </summary>
        public static Output<GetSchemaResult> Invoke(GetSchemaInvokeArgs? args = null, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.Invoke<GetSchemaResult>("googleworkspace:index/getSchema:getSchema", args ?? new GetSchemaInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetSchemaArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// The unique identifier of the schema.
        /// </summary>
        [Input("schemaId")]
        public string? SchemaId { get; set; }

        /// <summary>
        /// The schema's name.
        /// </summary>
        [Input("schemaName")]
        public string? SchemaName { get; set; }

        public GetSchemaArgs()
        {
        }
        public static new GetSchemaArgs Empty => new GetSchemaArgs();
    }

    public sealed class GetSchemaInvokeArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// The unique identifier of the schema.
        /// </summary>
        [Input("schemaId")]
        public Input<string>? SchemaId { get; set; }

        /// <summary>
        /// The schema's name.
        /// </summary>
        [Input("schemaName")]
        public Input<string>? SchemaName { get; set; }

        public GetSchemaInvokeArgs()
        {
        }
        public static new GetSchemaInvokeArgs Empty => new GetSchemaInvokeArgs();
    }


    [OutputType]
    public sealed class GetSchemaResult
    {
        /// <summary>
        /// Display name for the schema.
        /// </summary>
        public readonly string DisplayName;
        /// <summary>
        /// ETag of the resource.
        /// </summary>
        public readonly string Etag;
        /// <summary>
        /// A list of fields in the schema.
        /// </summary>
        public readonly ImmutableArray<Outputs.GetSchemaFieldResult> Fields;
        /// <summary>
        /// The ID of this resource.
        /// </summary>
        public readonly string Id;
        /// <summary>
        /// The unique identifier of the schema.
        /// </summary>
        public readonly string SchemaId;
        /// <summary>
        /// The schema's name.
        /// </summary>
        public readonly string SchemaName;

        [OutputConstructor]
        private GetSchemaResult(
            string displayName,

            string etag,

            ImmutableArray<Outputs.GetSchemaFieldResult> fields,

            string id,

            string schemaId,

            string schemaName)
        {
            DisplayName = displayName;
            Etag = etag;
            Fields = fields;
            Id = id;
            SchemaId = schemaId;
            SchemaName = schemaName;
        }
    }
}
