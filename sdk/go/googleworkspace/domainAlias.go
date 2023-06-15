// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package googleworkspace

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Domain Alias resource manages Google Workspace Domain Aliases. Domain Alias resides under the `https://www.googleapis.com/auth/admin.directory.domain` client scope.
//
// ## Example Usage
//
// ```go
// package main
//
// import (
// 	"github.com/pulumi/pulumi-googleworkspace/sdk/go/googleworkspace"
// 	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
// )
//
// func main() {
// 	pulumi.Run(func(ctx *pulumi.Context) error {
// 		_, err := googleworkspace.NewDomainAlias(ctx, "example", &googleworkspace.DomainAliasArgs{
// 			DomainAliasName:  pulumi.String("alias-example.com"),
// 			ParentDomainName: pulumi.String("example.com"),
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		return nil
// 	})
// }
// ```
//
// ## Import
//
// ```sh
//  $ pulumi import googleworkspace:index/domainAlias:DomainAlias example alias-example.com
// ```
type DomainAlias struct {
	pulumi.CustomResourceState

	// Creation time of the domain alias.
	CreationTime pulumi.IntOutput `pulumi:"creationTime"`
	// The domain alias name.
	DomainAliasName pulumi.StringOutput `pulumi:"domainAliasName"`
	// ETag of the resource.
	Etag pulumi.StringOutput `pulumi:"etag"`
	// The parent domain name that the domain alias is associated with. This can either be a primary or secondary domain name within a customer.
	ParentDomainName pulumi.StringPtrOutput `pulumi:"parentDomainName"`
	// Indicates the verification state of a domain alias.
	Verified pulumi.BoolOutput `pulumi:"verified"`
}

// NewDomainAlias registers a new resource with the given unique name, arguments, and options.
func NewDomainAlias(ctx *pulumi.Context,
	name string, args *DomainAliasArgs, opts ...pulumi.ResourceOption) (*DomainAlias, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.DomainAliasName == nil {
		return nil, errors.New("invalid value for required argument 'DomainAliasName'")
	}
	var resource DomainAlias
	err := ctx.RegisterResource("googleworkspace:index/domainAlias:DomainAlias", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetDomainAlias gets an existing DomainAlias resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetDomainAlias(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *DomainAliasState, opts ...pulumi.ResourceOption) (*DomainAlias, error) {
	var resource DomainAlias
	err := ctx.ReadResource("googleworkspace:index/domainAlias:DomainAlias", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering DomainAlias resources.
type domainAliasState struct {
	// Creation time of the domain alias.
	CreationTime *int `pulumi:"creationTime"`
	// The domain alias name.
	DomainAliasName *string `pulumi:"domainAliasName"`
	// ETag of the resource.
	Etag *string `pulumi:"etag"`
	// The parent domain name that the domain alias is associated with. This can either be a primary or secondary domain name within a customer.
	ParentDomainName *string `pulumi:"parentDomainName"`
	// Indicates the verification state of a domain alias.
	Verified *bool `pulumi:"verified"`
}

type DomainAliasState struct {
	// Creation time of the domain alias.
	CreationTime pulumi.IntPtrInput
	// The domain alias name.
	DomainAliasName pulumi.StringPtrInput
	// ETag of the resource.
	Etag pulumi.StringPtrInput
	// The parent domain name that the domain alias is associated with. This can either be a primary or secondary domain name within a customer.
	ParentDomainName pulumi.StringPtrInput
	// Indicates the verification state of a domain alias.
	Verified pulumi.BoolPtrInput
}

func (DomainAliasState) ElementType() reflect.Type {
	return reflect.TypeOf((*domainAliasState)(nil)).Elem()
}

type domainAliasArgs struct {
	// The domain alias name.
	DomainAliasName string `pulumi:"domainAliasName"`
	// The parent domain name that the domain alias is associated with. This can either be a primary or secondary domain name within a customer.
	ParentDomainName *string `pulumi:"parentDomainName"`
}

// The set of arguments for constructing a DomainAlias resource.
type DomainAliasArgs struct {
	// The domain alias name.
	DomainAliasName pulumi.StringInput
	// The parent domain name that the domain alias is associated with. This can either be a primary or secondary domain name within a customer.
	ParentDomainName pulumi.StringPtrInput
}

func (DomainAliasArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*domainAliasArgs)(nil)).Elem()
}

type DomainAliasInput interface {
	pulumi.Input

	ToDomainAliasOutput() DomainAliasOutput
	ToDomainAliasOutputWithContext(ctx context.Context) DomainAliasOutput
}

func (*DomainAlias) ElementType() reflect.Type {
	return reflect.TypeOf((**DomainAlias)(nil)).Elem()
}

func (i *DomainAlias) ToDomainAliasOutput() DomainAliasOutput {
	return i.ToDomainAliasOutputWithContext(context.Background())
}

func (i *DomainAlias) ToDomainAliasOutputWithContext(ctx context.Context) DomainAliasOutput {
	return pulumi.ToOutputWithContext(ctx, i).(DomainAliasOutput)
}

// DomainAliasArrayInput is an input type that accepts DomainAliasArray and DomainAliasArrayOutput values.
// You can construct a concrete instance of `DomainAliasArrayInput` via:
//
//          DomainAliasArray{ DomainAliasArgs{...} }
type DomainAliasArrayInput interface {
	pulumi.Input

	ToDomainAliasArrayOutput() DomainAliasArrayOutput
	ToDomainAliasArrayOutputWithContext(context.Context) DomainAliasArrayOutput
}

type DomainAliasArray []DomainAliasInput

func (DomainAliasArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*DomainAlias)(nil)).Elem()
}

func (i DomainAliasArray) ToDomainAliasArrayOutput() DomainAliasArrayOutput {
	return i.ToDomainAliasArrayOutputWithContext(context.Background())
}

func (i DomainAliasArray) ToDomainAliasArrayOutputWithContext(ctx context.Context) DomainAliasArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(DomainAliasArrayOutput)
}

// DomainAliasMapInput is an input type that accepts DomainAliasMap and DomainAliasMapOutput values.
// You can construct a concrete instance of `DomainAliasMapInput` via:
//
//          DomainAliasMap{ "key": DomainAliasArgs{...} }
type DomainAliasMapInput interface {
	pulumi.Input

	ToDomainAliasMapOutput() DomainAliasMapOutput
	ToDomainAliasMapOutputWithContext(context.Context) DomainAliasMapOutput
}

type DomainAliasMap map[string]DomainAliasInput

func (DomainAliasMap) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*DomainAlias)(nil)).Elem()
}

func (i DomainAliasMap) ToDomainAliasMapOutput() DomainAliasMapOutput {
	return i.ToDomainAliasMapOutputWithContext(context.Background())
}

func (i DomainAliasMap) ToDomainAliasMapOutputWithContext(ctx context.Context) DomainAliasMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(DomainAliasMapOutput)
}

type DomainAliasOutput struct{ *pulumi.OutputState }

func (DomainAliasOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**DomainAlias)(nil)).Elem()
}

func (o DomainAliasOutput) ToDomainAliasOutput() DomainAliasOutput {
	return o
}

func (o DomainAliasOutput) ToDomainAliasOutputWithContext(ctx context.Context) DomainAliasOutput {
	return o
}

// Creation time of the domain alias.
func (o DomainAliasOutput) CreationTime() pulumi.IntOutput {
	return o.ApplyT(func(v *DomainAlias) pulumi.IntOutput { return v.CreationTime }).(pulumi.IntOutput)
}

// The domain alias name.
func (o DomainAliasOutput) DomainAliasName() pulumi.StringOutput {
	return o.ApplyT(func(v *DomainAlias) pulumi.StringOutput { return v.DomainAliasName }).(pulumi.StringOutput)
}

// ETag of the resource.
func (o DomainAliasOutput) Etag() pulumi.StringOutput {
	return o.ApplyT(func(v *DomainAlias) pulumi.StringOutput { return v.Etag }).(pulumi.StringOutput)
}

// The parent domain name that the domain alias is associated with. This can either be a primary or secondary domain name within a customer.
func (o DomainAliasOutput) ParentDomainName() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *DomainAlias) pulumi.StringPtrOutput { return v.ParentDomainName }).(pulumi.StringPtrOutput)
}

// Indicates the verification state of a domain alias.
func (o DomainAliasOutput) Verified() pulumi.BoolOutput {
	return o.ApplyT(func(v *DomainAlias) pulumi.BoolOutput { return v.Verified }).(pulumi.BoolOutput)
}

type DomainAliasArrayOutput struct{ *pulumi.OutputState }

func (DomainAliasArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*DomainAlias)(nil)).Elem()
}

func (o DomainAliasArrayOutput) ToDomainAliasArrayOutput() DomainAliasArrayOutput {
	return o
}

func (o DomainAliasArrayOutput) ToDomainAliasArrayOutputWithContext(ctx context.Context) DomainAliasArrayOutput {
	return o
}

func (o DomainAliasArrayOutput) Index(i pulumi.IntInput) DomainAliasOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) *DomainAlias {
		return vs[0].([]*DomainAlias)[vs[1].(int)]
	}).(DomainAliasOutput)
}

type DomainAliasMapOutput struct{ *pulumi.OutputState }

func (DomainAliasMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*DomainAlias)(nil)).Elem()
}

func (o DomainAliasMapOutput) ToDomainAliasMapOutput() DomainAliasMapOutput {
	return o
}

func (o DomainAliasMapOutput) ToDomainAliasMapOutputWithContext(ctx context.Context) DomainAliasMapOutput {
	return o
}

func (o DomainAliasMapOutput) MapIndex(k pulumi.StringInput) DomainAliasOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) *DomainAlias {
		return vs[0].(map[string]*DomainAlias)[vs[1].(string)]
	}).(DomainAliasOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*DomainAliasInput)(nil)).Elem(), &DomainAlias{})
	pulumi.RegisterInputType(reflect.TypeOf((*DomainAliasArrayInput)(nil)).Elem(), DomainAliasArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*DomainAliasMapInput)(nil)).Elem(), DomainAliasMap{})
	pulumi.RegisterOutputType(DomainAliasOutput{})
	pulumi.RegisterOutputType(DomainAliasArrayOutput{})
	pulumi.RegisterOutputType(DomainAliasMapOutput{})
}
