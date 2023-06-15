// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package googleworkspace

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Group Members resource manages Google Workspace Groups Members. Group Members resides under the `https://www.googleapis.com/auth/admin.directory.group` client scope.
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
// 		salesGroup, err := googleworkspace.NewGroup(ctx, "salesGroup", &googleworkspace.GroupArgs{
// 			Email: pulumi.String("sales@example.com"),
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		michael, err := googleworkspace.NewUser(ctx, "michael", &googleworkspace.UserArgs{
// 			PrimaryEmail: pulumi.String("michael.scott@example.com"),
// 			Password:     pulumi.String("34819d7beeabb9260a5c854bc85b3e44"),
// 			HashFunction: pulumi.String("MD5"),
// 			Name: &UserNameArgs{
// 				FamilyName: pulumi.String("Scott"),
// 				GivenName:  pulumi.String("Michael"),
// 			},
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		frank, err := googleworkspace.NewUser(ctx, "frank", &googleworkspace.UserArgs{
// 			PrimaryEmail: pulumi.String("frank.scott@example.com"),
// 			Password:     pulumi.String("2095312189753de6ad47dfe20cbe97ec"),
// 			HashFunction: pulumi.String("MD5"),
// 			Name: &UserNameArgs{
// 				FamilyName: pulumi.String("Scott"),
// 				GivenName:  pulumi.String("Frank"),
// 			},
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		_, err = googleworkspace.NewGroupMembers(ctx, "salesGroupMembers", &googleworkspace.GroupMembersArgs{
// 			GroupId: salesGroup.ID(),
// 			Members: GroupMembersMemberArray{
// 				&GroupMembersMemberArgs{
// 					Email: michael.PrimaryEmail,
// 					Role:  pulumi.String("MANAGER"),
// 				},
// 				&GroupMembersMemberArgs{
// 					Email: frank.PrimaryEmail,
// 					Role:  pulumi.String("MEMBER"),
// 				},
// 			},
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
//  $ pulumi import googleworkspace:index/groupMembers:GroupMembers sales groups/01abcde23fg4h5i
// ```
type GroupMembers struct {
	pulumi.CustomResourceState

	// ETag of the resource.
	Etag pulumi.StringOutput `pulumi:"etag"`
	// Identifies the group in the API request. The value can be the group's email address, group alias, or the unique group
	// ID.
	GroupId pulumi.StringOutput `pulumi:"groupId"`
	// The members of the group
	Members GroupMembersMemberArrayOutput `pulumi:"members"`
}

// NewGroupMembers registers a new resource with the given unique name, arguments, and options.
func NewGroupMembers(ctx *pulumi.Context,
	name string, args *GroupMembersArgs, opts ...pulumi.ResourceOption) (*GroupMembers, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.GroupId == nil {
		return nil, errors.New("invalid value for required argument 'GroupId'")
	}
	var resource GroupMembers
	err := ctx.RegisterResource("googleworkspace:index/groupMembers:GroupMembers", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetGroupMembers gets an existing GroupMembers resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetGroupMembers(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *GroupMembersState, opts ...pulumi.ResourceOption) (*GroupMembers, error) {
	var resource GroupMembers
	err := ctx.ReadResource("googleworkspace:index/groupMembers:GroupMembers", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering GroupMembers resources.
type groupMembersState struct {
	// ETag of the resource.
	Etag *string `pulumi:"etag"`
	// Identifies the group in the API request. The value can be the group's email address, group alias, or the unique group
	// ID.
	GroupId *string `pulumi:"groupId"`
	// The members of the group
	Members []GroupMembersMember `pulumi:"members"`
}

type GroupMembersState struct {
	// ETag of the resource.
	Etag pulumi.StringPtrInput
	// Identifies the group in the API request. The value can be the group's email address, group alias, or the unique group
	// ID.
	GroupId pulumi.StringPtrInput
	// The members of the group
	Members GroupMembersMemberArrayInput
}

func (GroupMembersState) ElementType() reflect.Type {
	return reflect.TypeOf((*groupMembersState)(nil)).Elem()
}

type groupMembersArgs struct {
	// Identifies the group in the API request. The value can be the group's email address, group alias, or the unique group
	// ID.
	GroupId string `pulumi:"groupId"`
	// The members of the group
	Members []GroupMembersMember `pulumi:"members"`
}

// The set of arguments for constructing a GroupMembers resource.
type GroupMembersArgs struct {
	// Identifies the group in the API request. The value can be the group's email address, group alias, or the unique group
	// ID.
	GroupId pulumi.StringInput
	// The members of the group
	Members GroupMembersMemberArrayInput
}

func (GroupMembersArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*groupMembersArgs)(nil)).Elem()
}

type GroupMembersInput interface {
	pulumi.Input

	ToGroupMembersOutput() GroupMembersOutput
	ToGroupMembersOutputWithContext(ctx context.Context) GroupMembersOutput
}

func (*GroupMembers) ElementType() reflect.Type {
	return reflect.TypeOf((**GroupMembers)(nil)).Elem()
}

func (i *GroupMembers) ToGroupMembersOutput() GroupMembersOutput {
	return i.ToGroupMembersOutputWithContext(context.Background())
}

func (i *GroupMembers) ToGroupMembersOutputWithContext(ctx context.Context) GroupMembersOutput {
	return pulumi.ToOutputWithContext(ctx, i).(GroupMembersOutput)
}

// GroupMembersArrayInput is an input type that accepts GroupMembersArray and GroupMembersArrayOutput values.
// You can construct a concrete instance of `GroupMembersArrayInput` via:
//
//          GroupMembersArray{ GroupMembersArgs{...} }
type GroupMembersArrayInput interface {
	pulumi.Input

	ToGroupMembersArrayOutput() GroupMembersArrayOutput
	ToGroupMembersArrayOutputWithContext(context.Context) GroupMembersArrayOutput
}

type GroupMembersArray []GroupMembersInput

func (GroupMembersArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*GroupMembers)(nil)).Elem()
}

func (i GroupMembersArray) ToGroupMembersArrayOutput() GroupMembersArrayOutput {
	return i.ToGroupMembersArrayOutputWithContext(context.Background())
}

func (i GroupMembersArray) ToGroupMembersArrayOutputWithContext(ctx context.Context) GroupMembersArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(GroupMembersArrayOutput)
}

// GroupMembersMapInput is an input type that accepts GroupMembersMap and GroupMembersMapOutput values.
// You can construct a concrete instance of `GroupMembersMapInput` via:
//
//          GroupMembersMap{ "key": GroupMembersArgs{...} }
type GroupMembersMapInput interface {
	pulumi.Input

	ToGroupMembersMapOutput() GroupMembersMapOutput
	ToGroupMembersMapOutputWithContext(context.Context) GroupMembersMapOutput
}

type GroupMembersMap map[string]GroupMembersInput

func (GroupMembersMap) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*GroupMembers)(nil)).Elem()
}

func (i GroupMembersMap) ToGroupMembersMapOutput() GroupMembersMapOutput {
	return i.ToGroupMembersMapOutputWithContext(context.Background())
}

func (i GroupMembersMap) ToGroupMembersMapOutputWithContext(ctx context.Context) GroupMembersMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(GroupMembersMapOutput)
}

type GroupMembersOutput struct{ *pulumi.OutputState }

func (GroupMembersOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**GroupMembers)(nil)).Elem()
}

func (o GroupMembersOutput) ToGroupMembersOutput() GroupMembersOutput {
	return o
}

func (o GroupMembersOutput) ToGroupMembersOutputWithContext(ctx context.Context) GroupMembersOutput {
	return o
}

// ETag of the resource.
func (o GroupMembersOutput) Etag() pulumi.StringOutput {
	return o.ApplyT(func(v *GroupMembers) pulumi.StringOutput { return v.Etag }).(pulumi.StringOutput)
}

// Identifies the group in the API request. The value can be the group's email address, group alias, or the unique group
// ID.
func (o GroupMembersOutput) GroupId() pulumi.StringOutput {
	return o.ApplyT(func(v *GroupMembers) pulumi.StringOutput { return v.GroupId }).(pulumi.StringOutput)
}

// The members of the group
func (o GroupMembersOutput) Members() GroupMembersMemberArrayOutput {
	return o.ApplyT(func(v *GroupMembers) GroupMembersMemberArrayOutput { return v.Members }).(GroupMembersMemberArrayOutput)
}

type GroupMembersArrayOutput struct{ *pulumi.OutputState }

func (GroupMembersArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*GroupMembers)(nil)).Elem()
}

func (o GroupMembersArrayOutput) ToGroupMembersArrayOutput() GroupMembersArrayOutput {
	return o
}

func (o GroupMembersArrayOutput) ToGroupMembersArrayOutputWithContext(ctx context.Context) GroupMembersArrayOutput {
	return o
}

func (o GroupMembersArrayOutput) Index(i pulumi.IntInput) GroupMembersOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) *GroupMembers {
		return vs[0].([]*GroupMembers)[vs[1].(int)]
	}).(GroupMembersOutput)
}

type GroupMembersMapOutput struct{ *pulumi.OutputState }

func (GroupMembersMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*GroupMembers)(nil)).Elem()
}

func (o GroupMembersMapOutput) ToGroupMembersMapOutput() GroupMembersMapOutput {
	return o
}

func (o GroupMembersMapOutput) ToGroupMembersMapOutputWithContext(ctx context.Context) GroupMembersMapOutput {
	return o
}

func (o GroupMembersMapOutput) MapIndex(k pulumi.StringInput) GroupMembersOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) *GroupMembers {
		return vs[0].(map[string]*GroupMembers)[vs[1].(string)]
	}).(GroupMembersOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*GroupMembersInput)(nil)).Elem(), &GroupMembers{})
	pulumi.RegisterInputType(reflect.TypeOf((*GroupMembersArrayInput)(nil)).Elem(), GroupMembersArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*GroupMembersMapInput)(nil)).Elem(), GroupMembersMap{})
	pulumi.RegisterOutputType(GroupMembersOutput{})
	pulumi.RegisterOutputType(GroupMembersArrayOutput{})
	pulumi.RegisterOutputType(GroupMembersMapOutput{})
}
