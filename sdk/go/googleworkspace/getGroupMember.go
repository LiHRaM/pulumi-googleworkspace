// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package googleworkspace

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

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
// 		sales, err := googleworkspace.LookupGroup(ctx, &GetGroupArgs{
// 			Email: pulumi.StringRef("sales@example.com"),
// 		}, nil)
// 		if err != nil {
// 			return err
// 		}
// 		my_group_member, err := googleworkspace.LookupGroupMember(ctx, &GetGroupMemberArgs{
// 			GroupId: sales.Id,
// 			Email:   pulumi.StringRef("michael.scott@example.com"),
// 		}, nil)
// 		if err != nil {
// 			return err
// 		}
// 		ctx.Export("groupMemberRole", my_group_member.Role)
// 		return nil
// 	})
// }
// ```
func LookupGroupMember(ctx *pulumi.Context, args *LookupGroupMemberArgs, opts ...pulumi.InvokeOption) (*LookupGroupMemberResult, error) {
	var rv LookupGroupMemberResult
	err := ctx.Invoke("googleworkspace:index/getGroupMember:getGroupMember", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getGroupMember.
type LookupGroupMemberArgs struct {
	Email    *string `pulumi:"email"`
	GroupId  string  `pulumi:"groupId"`
	MemberId *string `pulumi:"memberId"`
}

// A collection of values returned by getGroupMember.
type LookupGroupMemberResult struct {
	DeliverySettings string `pulumi:"deliverySettings"`
	Email            string `pulumi:"email"`
	Etag             string `pulumi:"etag"`
	GroupId          string `pulumi:"groupId"`
	Id               string `pulumi:"id"`
	MemberId         string `pulumi:"memberId"`
	Role             string `pulumi:"role"`
	Status           string `pulumi:"status"`
	Type             string `pulumi:"type"`
}

func LookupGroupMemberOutput(ctx *pulumi.Context, args LookupGroupMemberOutputArgs, opts ...pulumi.InvokeOption) LookupGroupMemberResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupGroupMemberResult, error) {
			args := v.(LookupGroupMemberArgs)
			r, err := LookupGroupMember(ctx, &args, opts...)
			var s LookupGroupMemberResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(LookupGroupMemberResultOutput)
}

// A collection of arguments for invoking getGroupMember.
type LookupGroupMemberOutputArgs struct {
	Email    pulumi.StringPtrInput `pulumi:"email"`
	GroupId  pulumi.StringInput    `pulumi:"groupId"`
	MemberId pulumi.StringPtrInput `pulumi:"memberId"`
}

func (LookupGroupMemberOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupGroupMemberArgs)(nil)).Elem()
}

// A collection of values returned by getGroupMember.
type LookupGroupMemberResultOutput struct{ *pulumi.OutputState }

func (LookupGroupMemberResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupGroupMemberResult)(nil)).Elem()
}

func (o LookupGroupMemberResultOutput) ToLookupGroupMemberResultOutput() LookupGroupMemberResultOutput {
	return o
}

func (o LookupGroupMemberResultOutput) ToLookupGroupMemberResultOutputWithContext(ctx context.Context) LookupGroupMemberResultOutput {
	return o
}

func (o LookupGroupMemberResultOutput) DeliverySettings() pulumi.StringOutput {
	return o.ApplyT(func(v LookupGroupMemberResult) string { return v.DeliverySettings }).(pulumi.StringOutput)
}

func (o LookupGroupMemberResultOutput) Email() pulumi.StringOutput {
	return o.ApplyT(func(v LookupGroupMemberResult) string { return v.Email }).(pulumi.StringOutput)
}

func (o LookupGroupMemberResultOutput) Etag() pulumi.StringOutput {
	return o.ApplyT(func(v LookupGroupMemberResult) string { return v.Etag }).(pulumi.StringOutput)
}

func (o LookupGroupMemberResultOutput) GroupId() pulumi.StringOutput {
	return o.ApplyT(func(v LookupGroupMemberResult) string { return v.GroupId }).(pulumi.StringOutput)
}

func (o LookupGroupMemberResultOutput) Id() pulumi.StringOutput {
	return o.ApplyT(func(v LookupGroupMemberResult) string { return v.Id }).(pulumi.StringOutput)
}

func (o LookupGroupMemberResultOutput) MemberId() pulumi.StringOutput {
	return o.ApplyT(func(v LookupGroupMemberResult) string { return v.MemberId }).(pulumi.StringOutput)
}

func (o LookupGroupMemberResultOutput) Role() pulumi.StringOutput {
	return o.ApplyT(func(v LookupGroupMemberResult) string { return v.Role }).(pulumi.StringOutput)
}

func (o LookupGroupMemberResultOutput) Status() pulumi.StringOutput {
	return o.ApplyT(func(v LookupGroupMemberResult) string { return v.Status }).(pulumi.StringOutput)
}

func (o LookupGroupMemberResultOutput) Type() pulumi.StringOutput {
	return o.ApplyT(func(v LookupGroupMemberResult) string { return v.Type }).(pulumi.StringOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupGroupMemberResultOutput{})
}
