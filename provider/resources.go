// Copyright 2016-2018, Pulumi Corporation.
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//     http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

package googleworkspace

import (
	"fmt"
	"path/filepath"

	googleworkspace "github.com/hashicorp/terraform-provider-googleworkspace/shim"
	"github.com/lihram/pulumi-googleworkspace/provider/pkg/version"
	"github.com/pulumi/pulumi-terraform-bridge/v3/pkg/tfbridge"
	shim "github.com/pulumi/pulumi-terraform-bridge/v3/pkg/tfshim"
	shimv2 "github.com/pulumi/pulumi-terraform-bridge/v3/pkg/tfshim/sdk-v2"
	"github.com/pulumi/pulumi/sdk/v3/go/common/resource"
)

// all of the token components used below.
const (
	// This variable controls the default name of the package in the package
	// registries for nodejs and python:
	mainPkg = "googleworkspace"
	// modules:
	mainMod = "index" // the googleworkspace module
)

// preConfigureCallback is called before the providerConfigure function of the underlying provider.
// It should validate that the provider can be configured, and provide actionable errors in the case
// it cannot be. Configuration variables can be read from `vars` using the `stringValue` function -
// for example `stringValue(vars, "accessKey")`.
func preConfigureCallback(vars resource.PropertyMap, c shim.ResourceConfig) error {
	return nil
}

// Provider returns additional overlaid schema and metadata associated with the provider..
func Provider() tfbridge.ProviderInfo {
	// Instantiate the Terraform provider
	p := shimv2.NewProvider(googleworkspace.Provider())

	// Create a Pulumi provider mapping
	prov := tfbridge.ProviderInfo{
		P:    p,
		Name: "googleworkspace",
		// DisplayName is a way to be able to change the casing of the provider
		// name when being displayed on the Pulumi registry
		DisplayName: "",
		// The default publisher for all packages is Pulumi.
		// Change this to your personal name (or a company name) that you
		// would like to be shown in the Pulumi Registry if this package is published
		// there.
		Publisher: "Pulumi",
		// LogoURL is optional but useful to help identify your package in the Pulumi Registry
		// if this package is published there.
		//
		// You may host a logo on a domain you control or add an SVG logo for your package
		// in your repository and use the raw content URL for that file as your logo URL.
		LogoURL: "",
		// PluginDownloadURL is an optional URL used to download the Provider
		// for use in Pulumi programs
		// e.g https://github.com/org/pulumi-provider-name/releases/
		PluginDownloadURL: "",
		Description:       "A Pulumi package for creating and managing googleworkspace cloud resources.",
		// category/cloud tag helps with categorizing the package in the Pulumi Registry.
		// For all available categories, see `Keywords` in
		// https://www.pulumi.com/docs/guides/pulumi-packages/schema/#package.
		Keywords:   []string{"pulumi", "googleworkspace", "category/cloud"},
		License:    "Apache-2.0",
		Homepage:   "https://www.pulumi.com",
		Repository: "https://github.com/lihram/pulumi-googleworkspace",
		// The GitHub Org for the provider - defaults to `terraform-providers`. Note that this
		// should match the TF provider module's require directive, not any replace directives.
		GitHubOrg: "hashicorp",
		Config:    map[string]*tfbridge.SchemaInfo{
			// Add any required configuration here, or remove the example below if
			// no additional points are required.
			// "region": {
			// 	Type: tfbridge.MakeType("region", "Region"),
			// 	Default: &tfbridge.DefaultInfo{
			// 		EnvVars: []string{"AWS_REGION", "AWS_DEFAULT_REGION"},
			// 	},
			// },
		},
		PreConfigureCallback: preConfigureCallback,
		Resources: map[string]*tfbridge.ResourceInfo{
			// Map each resource in the Terraform provider to a Pulumi type. Two examples
			// are below - the single line form is the common case. The multi-line form is
			// needed only if you wish to override types or other default options.
			//
			// "aws_iam_role": {Tok: tfbridge.MakeResource(mainPkg, mainMod, "IamRole")}
			//
			// "aws_acm_certificate": {
			// 	Tok: tfbridge.MakeResource(mainPkg, mainMod, "Certificate"),
			// 	Fields: map[string]*tfbridge.SchemaInfo{
			// 		"tags": {Type: tfbridge.MakeType(mainPkg, "Tags")},
			// 	},
			// },
			"googleworkspace_chrome_policy":       {Tok: tfbridge.MakeResource(mainPkg, mainMod, "ChromePolicy")},
			"googleworkspace_domain":              {Tok: tfbridge.MakeResource(mainPkg, mainMod, "Domain")},
			"googleworkspace_domain_alias":        {Tok: tfbridge.MakeResource(mainPkg, mainMod, "DomainAlias")},
			"googleworkspace_gmail_send_as_alias": {Tok: tfbridge.MakeResource(mainPkg, mainMod, "GmailSendAsAlias")},
			"googleworkspace_group":               {Tok: tfbridge.MakeResource(mainPkg, mainMod, "Group")},
			"googleworkspace_group_member":        {Tok: tfbridge.MakeResource(mainPkg, mainMod, "GroupMember")},
			"googleworkspace_group_members":       {Tok: tfbridge.MakeResource(mainPkg, mainMod, "GroupMembers")},
			"googleworkspace_group_settings":      {Tok: tfbridge.MakeResource(mainPkg, mainMod, "GroupSettings")},
			"googleworkspace_org_unit":            {Tok: tfbridge.MakeResource(mainPkg, mainMod, "OrgUnit")},
			"googleworkspace_role":                {Tok: tfbridge.MakeResource(mainPkg, mainMod, "Role")},
			"googleworkspace_role_assignment":     {Tok: tfbridge.MakeResource(mainPkg, mainMod, "RoleAssignment")},
			"googleworkspace_schema":              {Tok: tfbridge.MakeResource(mainPkg, mainMod, "Schema")},
			"googleworkspace_user":                {Tok: tfbridge.MakeResource(mainPkg, mainMod, "User")},
		},
		DataSources: map[string]*tfbridge.DataSourceInfo{
			// Map each resource in the Terraform provider to a Pulumi function. An example
			// is below.
			// "aws_ami": {Tok: tfbridge.MakeDataSource(mainPkg, mainMod, "getAmi")},
			"googleworkspace_chrome_policy":        {Tok: tfbridge.MakeDataSource(mainPkg, mainMod, "getChromePolicy")},
			"googleworkspace_chrome_policy_schema": {Tok: tfbridge.MakeDataSource(mainPkg, mainMod, "getChromePolicySchema")},
			"googleworkspace_domain":               {Tok: tfbridge.MakeDataSource(mainPkg, mainMod, "getDomain")},
			"googleworkspace_domain_alias":         {Tok: tfbridge.MakeDataSource(mainPkg, mainMod, "getDomainAlias")},
			"googleworkspace_gmail_send_as_alias":  {Tok: tfbridge.MakeDataSource(mainPkg, mainMod, "getGmailSendAsAlias")},
			"googleworkspace_group":                {Tok: tfbridge.MakeDataSource(mainPkg, mainMod, "getGroup")},
			"googleworkspace_groups":               {Tok: tfbridge.MakeDataSource(mainPkg, mainMod, "getGroups")},
			"googleworkspace_group_member":         {Tok: tfbridge.MakeDataSource(mainPkg, mainMod, "getGroupMember")},
			"googleworkspace_group_members":        {Tok: tfbridge.MakeDataSource(mainPkg, mainMod, "getGroupMembers")},
			"googleworkspace_group_settings":       {Tok: tfbridge.MakeDataSource(mainPkg, mainMod, "getGroupSettings")},
			"googleworkspace_org_unit":             {Tok: tfbridge.MakeDataSource(mainPkg, mainMod, "getOrgUnit")},
			"googleworkspace_privileges":           {Tok: tfbridge.MakeDataSource(mainPkg, mainMod, "getPrivileges")},
			"googleworkspace_role":                 {Tok: tfbridge.MakeDataSource(mainPkg, mainMod, "getRole")},
			"googleworkspace_role_assignment":      {Tok: tfbridge.MakeDataSource(mainPkg, mainMod, "getRoleAssignment")},
			"googleworkspace_schema":               {Tok: tfbridge.MakeDataSource(mainPkg, mainMod, "getSchema")},
			"googleworkspace_user":                 {Tok: tfbridge.MakeDataSource(mainPkg, mainMod, "getUser")},
			"googleworkspace_users":                {Tok: tfbridge.MakeDataSource(mainPkg, mainMod, "getUsers")},
		},
		JavaScript: &tfbridge.JavaScriptInfo{
			// List any npm dependencies and their versions
			Dependencies: map[string]string{
				"@pulumi/pulumi": "^3.0.0",
			},
			DevDependencies: map[string]string{
				"@types/node": "^10.0.0", // so we can access strongly typed node definitions.
				"@types/mime": "^2.0.0",
			},
			// See the documentation for tfbridge.OverlayInfo for how to lay out this
			// section, or refer to the AWS provider. Delete this section if there are
			// no overlay files.
			//Overlay: &tfbridge.OverlayInfo{},
		},
		Python: &tfbridge.PythonInfo{
			// List any Python dependencies and their version ranges
			Requires: map[string]string{
				"pulumi": ">=3.0.0,<4.0.0",
			},
		},
		Golang: &tfbridge.GolangInfo{
			ImportBasePath: filepath.Join(
				fmt.Sprintf("github.com/pulumi/pulumi-%[1]s/sdk/", mainPkg),
				tfbridge.GetModuleMajorVersion(version.Version),
				"go",
				mainPkg,
			),
			GenerateResourceContainerTypes: true,
		},
		CSharp: &tfbridge.CSharpInfo{
			PackageReferences: map[string]string{
				"Pulumi": "3.*",
			},
		},
	}

	prov.SetAutonaming(255, "-")

	return prov
}
