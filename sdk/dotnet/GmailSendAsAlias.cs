// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Googleworkspace
{
    /// <summary>
    /// ## Example Usage
    /// 
    /// ```csharp
    /// using System.Collections.Generic;
    /// using Pulumi;
    /// using Googleworkspace = Pulumi.Googleworkspace;
    /// 
    /// return await Deployment.RunAsync(() =&gt; 
    /// {
    ///     var example = Googleworkspace.GetUser.Invoke(new()
    ///     {
    ///         PrimaryEmail = "user.with.gmail.license@example.com",
    ///     });
    /// 
    ///     var @alias = new Googleworkspace.User("alias", new()
    ///     {
    ///         PrimaryEmail = "alias@example.com",
    ///         Password = "34819d7beeabb9260a5c854bc85b3e44",
    ///         HashFunction = "MD5",
    ///         Name = new Googleworkspace.Inputs.UserNameArgs
    ///         {
    ///             FamilyName = "Scott",
    ///             GivenName = "Michael",
    ///         },
    ///     });
    /// 
    ///     var test = new Googleworkspace.GmailSendAsAlias("test", new()
    ///     {
    ///         PrimaryEmail = example.Apply(getUserResult =&gt; getUserResult.PrimaryEmail),
    ///         SendAsEmail = @alias.PrimaryEmail,
    ///     });
    /// 
    /// });
    /// ```
    /// 
    /// ## Import
    /// 
    /// ```sh
    ///  $ pulumi import googleworkspace:index/gmailSendAsAlias:GmailSendAsAlias alias user@example.com:alias@anotherexample.com
    /// ```
    /// </summary>
    [GoogleworkspaceResourceType("googleworkspace:index/gmailSendAsAlias:GmailSendAsAlias")]
    public partial class GmailSendAsAlias : global::Pulumi.CustomResource
    {
        /// <summary>
        /// A name that appears in the 'From:' header for mail sent using this alias. For custom 'from' addresses, when this is empty, Gmail will populate the 'From:' header with the name that is used for the primary address associated with the account. If the admin has disabled the ability for users to update their name format, requests to update this field for the primary login will silently fail.
        /// </summary>
        [Output("displayName")]
        public Output<string?> DisplayName { get; private set; } = null!;

        /// <summary>
        /// Whether this address is selected as the default 'From:' address in situations such as composing a new message or sending
        /// a vacation auto-reply. Every Gmail account has exactly one default send-as address, so the only legal value that clients
        /// may write to this field is true. Changing this from false to true for an address will result in this field becoming
        /// false for the other previous default address. Toggling an existing alias' default to false is not possible, another
        /// alias must be added/imported and toggled to true to remove the default from an existing alias. To avoid drift with
        /// Terraform, please change the previous default's config to false AFTER a new default is applied and perform a refresh to
        /// synchronize with remote state.
        /// </summary>
        [Output("isDefault")]
        public Output<bool?> IsDefault { get; private set; } = null!;

        /// <summary>
        /// Whether this address is the primary address used to login to the account. Every Gmail account has exactly one primary address, and it cannot be deleted from the collection of send-as aliases.
        /// </summary>
        [Output("isPrimary")]
        public Output<bool> IsPrimary { get; private set; } = null!;

        /// <summary>
        /// User's primary email address.
        /// </summary>
        [Output("primaryEmail")]
        public Output<string> PrimaryEmail { get; private set; } = null!;

        /// <summary>
        /// An optional email address that is included in a 'Reply-To:' header for mail sent using this alias. If this is empty, Gmail will not generate a 'Reply-To:' header.
        /// </summary>
        [Output("replyToAddress")]
        public Output<string?> ReplyToAddress { get; private set; } = null!;

        /// <summary>
        /// The email address that appears in the 'From:' header for mail sent using this alias.
        /// </summary>
        [Output("sendAsEmail")]
        public Output<string> SendAsEmail { get; private set; } = null!;

        /// <summary>
        /// An optional HTML signature that is included in messages composed with this alias in the Gmail web UI. This signature is added to new emails only.
        /// </summary>
        [Output("signature")]
        public Output<string?> Signature { get; private set; } = null!;

        /// <summary>
        /// An optional SMTP service that will be used as an outbound relay for mail sent using this alias. If this is empty, outbound mail will be sent directly from Gmail's servers to the destination SMTP service. This setting only applies to custom 'from' aliases.
        /// </summary>
        [Output("smtpMsa")]
        public Output<Outputs.GmailSendAsAliasSmtpMsa?> SmtpMsa { get; private set; } = null!;

        /// <summary>
        /// Defaults to `true`. Whether Gmail should treat this address as an alias for the user's primary email address. This setting only applies to custom 'from' aliases. See https://support.google.com/a/answer/1710338 for help on making this decision
        /// </summary>
        [Output("treatAsAlias")]
        public Output<bool?> TreatAsAlias { get; private set; } = null!;

        /// <summary>
        /// Indicates whether this address has been verified for use as a send-as alias.
        /// </summary>
        [Output("verificationStatus")]
        public Output<string> VerificationStatus { get; private set; } = null!;


        /// <summary>
        /// Create a GmailSendAsAlias resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public GmailSendAsAlias(string name, GmailSendAsAliasArgs args, CustomResourceOptions? options = null)
            : base("googleworkspace:index/gmailSendAsAlias:GmailSendAsAlias", name, args ?? new GmailSendAsAliasArgs(), MakeResourceOptions(options, ""))
        {
        }

        private GmailSendAsAlias(string name, Input<string> id, GmailSendAsAliasState? state = null, CustomResourceOptions? options = null)
            : base("googleworkspace:index/gmailSendAsAlias:GmailSendAsAlias", name, state, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing GmailSendAsAlias resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static GmailSendAsAlias Get(string name, Input<string> id, GmailSendAsAliasState? state = null, CustomResourceOptions? options = null)
        {
            return new GmailSendAsAlias(name, id, state, options);
        }
    }

    public sealed class GmailSendAsAliasArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// A name that appears in the 'From:' header for mail sent using this alias. For custom 'from' addresses, when this is empty, Gmail will populate the 'From:' header with the name that is used for the primary address associated with the account. If the admin has disabled the ability for users to update their name format, requests to update this field for the primary login will silently fail.
        /// </summary>
        [Input("displayName")]
        public Input<string>? DisplayName { get; set; }

        /// <summary>
        /// Whether this address is selected as the default 'From:' address in situations such as composing a new message or sending
        /// a vacation auto-reply. Every Gmail account has exactly one default send-as address, so the only legal value that clients
        /// may write to this field is true. Changing this from false to true for an address will result in this field becoming
        /// false for the other previous default address. Toggling an existing alias' default to false is not possible, another
        /// alias must be added/imported and toggled to true to remove the default from an existing alias. To avoid drift with
        /// Terraform, please change the previous default's config to false AFTER a new default is applied and perform a refresh to
        /// synchronize with remote state.
        /// </summary>
        [Input("isDefault")]
        public Input<bool>? IsDefault { get; set; }

        /// <summary>
        /// User's primary email address.
        /// </summary>
        [Input("primaryEmail", required: true)]
        public Input<string> PrimaryEmail { get; set; } = null!;

        /// <summary>
        /// An optional email address that is included in a 'Reply-To:' header for mail sent using this alias. If this is empty, Gmail will not generate a 'Reply-To:' header.
        /// </summary>
        [Input("replyToAddress")]
        public Input<string>? ReplyToAddress { get; set; }

        /// <summary>
        /// The email address that appears in the 'From:' header for mail sent using this alias.
        /// </summary>
        [Input("sendAsEmail", required: true)]
        public Input<string> SendAsEmail { get; set; } = null!;

        /// <summary>
        /// An optional HTML signature that is included in messages composed with this alias in the Gmail web UI. This signature is added to new emails only.
        /// </summary>
        [Input("signature")]
        public Input<string>? Signature { get; set; }

        /// <summary>
        /// An optional SMTP service that will be used as an outbound relay for mail sent using this alias. If this is empty, outbound mail will be sent directly from Gmail's servers to the destination SMTP service. This setting only applies to custom 'from' aliases.
        /// </summary>
        [Input("smtpMsa")]
        public Input<Inputs.GmailSendAsAliasSmtpMsaArgs>? SmtpMsa { get; set; }

        /// <summary>
        /// Defaults to `true`. Whether Gmail should treat this address as an alias for the user's primary email address. This setting only applies to custom 'from' aliases. See https://support.google.com/a/answer/1710338 for help on making this decision
        /// </summary>
        [Input("treatAsAlias")]
        public Input<bool>? TreatAsAlias { get; set; }

        public GmailSendAsAliasArgs()
        {
        }
        public static new GmailSendAsAliasArgs Empty => new GmailSendAsAliasArgs();
    }

    public sealed class GmailSendAsAliasState : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// A name that appears in the 'From:' header for mail sent using this alias. For custom 'from' addresses, when this is empty, Gmail will populate the 'From:' header with the name that is used for the primary address associated with the account. If the admin has disabled the ability for users to update their name format, requests to update this field for the primary login will silently fail.
        /// </summary>
        [Input("displayName")]
        public Input<string>? DisplayName { get; set; }

        /// <summary>
        /// Whether this address is selected as the default 'From:' address in situations such as composing a new message or sending
        /// a vacation auto-reply. Every Gmail account has exactly one default send-as address, so the only legal value that clients
        /// may write to this field is true. Changing this from false to true for an address will result in this field becoming
        /// false for the other previous default address. Toggling an existing alias' default to false is not possible, another
        /// alias must be added/imported and toggled to true to remove the default from an existing alias. To avoid drift with
        /// Terraform, please change the previous default's config to false AFTER a new default is applied and perform a refresh to
        /// synchronize with remote state.
        /// </summary>
        [Input("isDefault")]
        public Input<bool>? IsDefault { get; set; }

        /// <summary>
        /// Whether this address is the primary address used to login to the account. Every Gmail account has exactly one primary address, and it cannot be deleted from the collection of send-as aliases.
        /// </summary>
        [Input("isPrimary")]
        public Input<bool>? IsPrimary { get; set; }

        /// <summary>
        /// User's primary email address.
        /// </summary>
        [Input("primaryEmail")]
        public Input<string>? PrimaryEmail { get; set; }

        /// <summary>
        /// An optional email address that is included in a 'Reply-To:' header for mail sent using this alias. If this is empty, Gmail will not generate a 'Reply-To:' header.
        /// </summary>
        [Input("replyToAddress")]
        public Input<string>? ReplyToAddress { get; set; }

        /// <summary>
        /// The email address that appears in the 'From:' header for mail sent using this alias.
        /// </summary>
        [Input("sendAsEmail")]
        public Input<string>? SendAsEmail { get; set; }

        /// <summary>
        /// An optional HTML signature that is included in messages composed with this alias in the Gmail web UI. This signature is added to new emails only.
        /// </summary>
        [Input("signature")]
        public Input<string>? Signature { get; set; }

        /// <summary>
        /// An optional SMTP service that will be used as an outbound relay for mail sent using this alias. If this is empty, outbound mail will be sent directly from Gmail's servers to the destination SMTP service. This setting only applies to custom 'from' aliases.
        /// </summary>
        [Input("smtpMsa")]
        public Input<Inputs.GmailSendAsAliasSmtpMsaGetArgs>? SmtpMsa { get; set; }

        /// <summary>
        /// Defaults to `true`. Whether Gmail should treat this address as an alias for the user's primary email address. This setting only applies to custom 'from' aliases. See https://support.google.com/a/answer/1710338 for help on making this decision
        /// </summary>
        [Input("treatAsAlias")]
        public Input<bool>? TreatAsAlias { get; set; }

        /// <summary>
        /// Indicates whether this address has been verified for use as a send-as alias.
        /// </summary>
        [Input("verificationStatus")]
        public Input<string>? VerificationStatus { get; set; }

        public GmailSendAsAliasState()
        {
        }
        public static new GmailSendAsAliasState Empty => new GmailSendAsAliasState();
    }
}
